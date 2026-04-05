#!/usr/bin/env python3
"""
Cowork Session Cleaner - Windows Edition
Manages Claude Cowork sessions on Windows systems
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

def get_cowork_sessions_path():
    """Get the Cowork sessions path for Windows"""
    username = os.getenv('USERNAME')
    base_path = Path(f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Claude_pzs8sxrjxfjjc\\LocalCache\\Roaming\\Claude\\local-agent-mode-sessions")
    return base_path

def get_session_title(session_path):
    """Extract session title from metadata"""
    try:
        metadata_file = session_path / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                return metadata.get('title', 'Sin título')
    except:
        pass
    return session_path.name

def is_session_archived(session_path):
    """Check if a session is archived"""
    try:
        metadata_file = session_path / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                return metadata.get('isArchived', False)
    except:
        pass
    return False

def get_session_info(session_path):
    """Get info about a session"""
    try:
        size = sum(f.stat().st_size for f in session_path.rglob('*') if f.is_file())
        size_mb = size / (1024 * 1024)
    except:
        size_mb = 0
    
    try:
        mod_time = session_path.stat().st_mtime
        mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M')
    except:
        mod_date = 'Desconocido'
    
    title = get_session_title(session_path)
    archived = is_session_archived(session_path)
    
    return {
        'path': session_path,
        'title': title,
        'archived': archived,
        'size_mb': size_mb,
        'mod_date': mod_date
    }

def list_sessions(filter_type=None):
    """List all Cowork sessions"""
    base_path = get_cowork_sessions_path()
    
    if not base_path.exists():
        print(f"❌ No se encontró la carpeta de Cowork en: {base_path}")
        return []
    
    sessions = []
    
    try:
        for org_folder in base_path.iterdir():
            if not org_folder.is_dir():
                continue
            
            for project_folder in org_folder.iterdir():
                if not project_folder.is_dir():
                    continue
                
                for session_folder in project_folder.iterdir():
                    if not session_folder.is_dir() or not session_folder.name.startswith('local_'):
                        continue
                    
                    info = get_session_info(session_folder)
                    
                    if filter_type == 'archived' and not info['archived']:
                        continue
                    if filter_type == 'active' and info['archived']:
                        continue
                    
                    sessions.append(info)
    except Exception as e:
        print(f"⚠️  Error al leer sesiones: {e}")
    
    return sorted(sessions, key=lambda x: x['mod_date'], reverse=True)

def display_sessions(sessions):
    """Display sessions in a formatted table"""
    if not sessions:
        print("ℹ️  No hay sesiones para mostrar.")
        return
    
    archived_count = sum(1 for s in sessions if s['archived'])
    active_count = len(sessions) - archived_count
    total_size = sum(s['size_mb'] for s in sessions)
    
    print("\n" + "="*90)
    print(f"  Gestor de Sesiones Cowork")
    print(f"  {len(sessions)} sesión(es)  |  {active_count} activa(s), {archived_count} archivada(s)  |  {total_size:.1f} MB total")
    print("="*90 + "\n")
    
    print(f"{'#':<4} {'Estado':<10} {'Última Mod.':<18} {'Tamaño':<10} {'Título':<45}")
    print("-" * 90)
    
    for idx, session in enumerate(sessions, 1):
        status = "ARCHIVADA" if session['archived'] else "activa"
        print(f"{idx:<4} {status:<10} {session['mod_date']:<18} {session['size_mb']:>7.1f} MB  {session['title']:<45}")
    
    print()

def delete_sessions(sessions, indices):
    """Delete selected sessions"""
    if not indices:
        print("❌ No se seleccionaron sesiones.")
        return
    
    to_delete = [sessions[i-1] for i in indices if 0 < i <= len(sessions)]
    
    if not to_delete:
        print("❌ Selección inválida.")
        return
    
    print("\n" + "="*90)
    print(f"Sesiones a ELIMINAR ({len(to_delete)}):")
    print("="*90)
    for session in to_delete:
        status = "ARCHIVADA" if session['archived'] else "activa"
        print(f"  [{status}] {session['title']}")
        print(f"       {session['path']}")
    
    confirm = input("\n⚠️  ¿Estás seguro de que quieres ELIMINAR estas sesiones? (sí/no): ").strip().lower()
    
    if confirm not in ['sí', 'si', 'yes', 'y']:
        print("❌ Cancelado.")
        return
    
    deleted_count = 0
    for session in to_delete:
        try:
            shutil.rmtree(session['path'])
            print(f"✅ Eliminada: {session['title']}")
            deleted_count += 1
        except Exception as e:
            print(f"❌ Error al eliminar '{session['title']}': {e}")
    
    print(f"\n✅ Completado. Se eliminaron {deleted_count} sesión(es).")

def parse_selection(selection_str, max_num):
    """Parse user selection (e.g., '1,3,5' or '1-5' or 'all')"""
    if selection_str.strip().lower() == 'all':
        return list(range(1, max_num + 1))
    
    indices = []
    for part in selection_str.split(','):
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                indices.extend(range(start, end + 1))
            except:
                pass
        else:
            try:
                indices.append(int(part))
            except:
                pass
    
    return sorted(set(indices))

def main():
    """Main menu"""
    print("\n🔍 Escaneando sesiones de Cowork...\n")
    
    all_sessions = list_sessions()
    
    if not all_sessions:
        return
    
    while True:
        display_sessions(all_sessions)
        
        print("¿Qué deseas hacer?")
        print("  [D] Eliminar sesiones")
        print("  [A] Mostrar solo ARCHIVADAS")
        print("  [V] Ver TODAS las sesiones")
        print("  [S] Salir")
        print()
        
        action = input("Acción: ").strip().upper()
        
        if action == 'D':
            if not all_sessions:
                print("❌ No hay sesiones para eliminar.")
                continue
            
            selection = input("\nIngresa números (ej: 1,3,5 o 1-5 o all): ").strip()
            indices = parse_selection(selection, len(all_sessions))
            
            if indices:
                delete_sessions(all_sessions, indices)
                all_sessions = list_sessions()
            else:
                print("❌ Selección inválida.")
        
        elif action == 'A':
            archived = list_sessions(filter_type='archived')
            display_sessions(archived)
            
            if archived:
                selection = input("Ingresa números a eliminar (ej: 1,3,5 o all): ").strip()
                indices = parse_selection(selection, len(archived))
                
                if indices:
                    delete_sessions(archived, indices)
                    all_sessions = list_sessions()
        
        elif action == 'V':
            all_sessions = list_sessions()
        
        elif action == 'S':
            print("👋 Hasta luego.")
            break
        
        else:
            print("❌ Acción no reconocida.")

if __name__ == '__main__':
    main()
