#!/usr/bin/env python3
"""
Cowork Session Cleaner - Multi-platform
Manages Claude Cowork sessions on Windows and macOS
Auto-detects OS, username, and language
"""

import os
import sys
import json
import shutil
import platform
from pathlib import Path
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

LANGUAGE = os.getenv('LANG', 'en_US').split('_')[0]
if LANGUAGE not in ['es', 'en']:
    LANGUAGE = 'en'

TEXTS = {
    'en': {
        'title': 'Cowork Session Manager',
        'scanning': '🔍 Scanning Cowork sessions...',
        'not_found': '❌ Cowork sessions folder not found.',
        'sessions_count': 'session(s)',
        'active': 'active',
        'archived': 'ARCHIVED',
        'total_size': 'MB total',
        'what_to_do': 'What would you like to do?',
        'delete': '[D] Delete sessions',
        'show_archived': '[A] Show only ARCHIVED',
        'show_all': '[V] View ALL sessions',
        'quit': '[S] Quit',
        'action': 'Action',
        'select_numbers': 'Enter session numbers (e.g., 1,3,5 or 1-5 or all)',
        'select': 'Select',
        'confirm_delete': '⚠️  Are you sure you want to DELETE these sessions? (yes/no)',
        'deleted': '✅ Deleted',
        'completed': '✅ Completed. Deleted',
        'error_delete': '❌ Error deleting',
        'invalid_selection': '❌ Invalid selection.',
        'no_sessions': 'ℹ️  No sessions to show.',
        'restart_required': 'Restart Claude for changes to take effect.',
        'cancelled': '❌ Cancelled.',
        'goodbye': '👋 Goodbye.',
    },
    'es': {
        'title': 'Gestor de Sesiones Cowork',
        'scanning': '🔍 Escaneando sesiones de Cowork...',
        'not_found': '❌ Carpeta de sesiones Cowork no encontrada.',
        'sessions_count': 'sesión(es)',
        'active': 'activa',
        'archived': 'ARCHIVADA',
        'total_size': 'MB total',
        'what_to_do': '¿Qué deseas hacer?',
        'delete': '[D] Eliminar sesiones',
        'show_archived': '[A] Mostrar solo ARCHIVADAS',
        'show_all': '[V] Ver TODAS las sesiones',
        'quit': '[S] Salir',
        'action': 'Acción',
        'select_numbers': 'Ingresa números (ej: 1,3,5 o 1-5 o all)',
        'select': 'Selecciona',
        'confirm_delete': '⚠️  ¿Estás seguro de que quieres ELIMINAR estas sesiones? (sí/no)',
        'deleted': '✅ Eliminada',
        'completed': '✅ Completado. Se eliminaron',
        'error_delete': '❌ Error al eliminar',
        'invalid_selection': '❌ Selección inválida.',
        'no_sessions': 'ℹ️  No hay sesiones para mostrar.',
        'restart_required': 'Reinicia Claude para que los cambios tomen efecto.',
        'cancelled': '❌ Cancelado.',
        'goodbye': '👋 Hasta luego.',
    }
}

T = TEXTS[LANGUAGE]

# ============================================================================
# PLATFORM DETECTION
# ============================================================================

def get_os_type():
    """Detect operating system"""
    system = platform.system()
    if system == 'Darwin':
        return 'mac'
    elif system == 'Windows':
        return 'windows'
    elif system == 'Linux':
        return 'linux'
    else:
        return None

def get_cowork_sessions_path():
    """Get Cowork sessions path based on OS"""
    os_type = get_os_type()
    username = os.getenv('USER') if os_type == 'mac' else os.getenv('USERNAME')
    
    if os_type == 'mac':
        return Path.home() / 'Library' / 'Application Support' / 'Claude' / 'local-agent-mode-sessions'
    elif os_type == 'windows':
        return Path(f"C:\\Users\\{username}\\AppData\\Local\\Packages\\Claude_pzs8sxrjxfjjc\\LocalCache\\Roaming\\Claude\\local-agent-mode-sessions")
    else:
        return None

# ============================================================================
# SESSION MANAGEMENT
# ============================================================================

def get_session_title(session_path):
    """Extract session title from metadata"""
    try:
        metadata_file = session_path / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                return metadata.get('title', 'Untitled')
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
        mod_date = 'Unknown'
    
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
    
    if not base_path or not base_path.exists():
        print(f"{T['not_found']}")
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
        print(f"⚠️  Error reading sessions: {e}")
    
    return sorted(sessions, key=lambda x: x['mod_date'], reverse=True)

def display_sessions(sessions):
    """Display sessions in a formatted table"""
    if not sessions:
        print(f"{T['no_sessions']}")
        return
    
    archived_count = sum(1 for s in sessions if s['archived'])
    active_count = len(sessions) - archived_count
    total_size = sum(s['size_mb'] for s in sessions)
    
    print("\n" + "="*95)
    print(f"  {T['title']}")
    print(f"  {len(sessions)} {T['sessions_count']}  |  {active_count} {T['active']}, {archived_count} {T['archived']}  |  {total_size:.1f} {T['total_size']}")
    print("="*95 + "\n")
    
    print(f"{'#':<4} {'Status':<10} {'Last Modified':<18} {'Size':<10} {'Title':<45}")
    print("-" * 95)
    
    for idx, session in enumerate(sessions, 1):
        status = T['archived'] if session['archived'] else T['active']
        print(f"{idx:<4} {status:<10} {session['mod_date']:<18} {session['size_mb']:>7.1f} MB  {session['title']:<45}")
    
    print()

def delete_sessions(sessions, indices):
    """Delete selected sessions"""
    if not indices:
        print(f"{T['invalid_selection']}")
        return
    
    to_delete = [sessions[i-1] for i in indices if 0 < i <= len(sessions)]
    
    if not to_delete:
        print(f"{T['invalid_selection']}")
        return
    
    print("\n" + "="*95)
    print(f"Sessions to DELETE ({len(to_delete)}):")
    print("="*95)
    for session in to_delete:
        status = T['archived'] if session['archived'] else T['active']
        print(f"  [{status}] {session['title']}")
        print(f"       {session['path']}")
    
    confirm = input(f"\n{T['confirm_delete']}: ").strip().lower()
    
    if confirm not in ['yes', 'y', 'sí', 'si']:
        print(f"{T['cancelled']}")
        return
    
    deleted_count = 0
    for session in to_delete:
        try:
            shutil.rmtree(session['path'])
            print(f"{T['deleted']}: {session['title']}")
            deleted_count += 1
        except Exception as e:
            print(f"{T['error_delete']} '{session['title']}': {e}")
    
    print(f"\n{T['completed']} {deleted_count} {T['sessions_count']}.")

def parse_selection(selection_str, max_num):
    """Parse user selection (e.g., '1,3,5' or '1-5' or 'all')"""
    if selection_str.strip().lower() in ['all', 'todo']:
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

# ============================================================================
# MAIN MENU
# ============================================================================

def main():
    """Main menu"""
    print(f"\n{T['scanning']}\n")
    
    all_sessions = list_sessions()
    
    if not all_sessions:
        return
    
    while True:
        display_sessions(all_sessions)
        
        print(T['what_to_do'])
        print(f"  {T['delete']}")
        print(f"  {T['show_archived']}")
        print(f"  {T['show_all']}")
        print(f"  {T['quit']}")
        print()
        
        action = input(f"{T['action']}: ").strip().upper()
        
        if action == 'D':
            if not all_sessions:
                print(f"{T['invalid_selection']}")
                continue
            
            selection = input(f"\n{T['select_numbers']}: ").strip()
            indices = parse_selection(selection, len(all_sessions))
            
            if indices:
                delete_sessions(all_sessions, indices)
                all_sessions = list_sessions()
            else:
                print(f"{T['invalid_selection']}")
        
        elif action == 'A':
            archived = list_sessions(filter_type='archived')
            display_sessions(archived)
            
            if archived:
                selection = input(f"{T['select_numbers']}: ").strip()
                indices = parse_selection(selection, len(archived))
                
                if indices:
                    delete_sessions(archived, indices)
                    all_sessions = list_sessions()
        
        elif action == 'V':
            all_sessions = list_sessions()
        
        elif action == 'S':
            print(f"{T['goodbye']}")
            break
        
        else:
            print(f"{T['invalid_selection']}")

if __name__ == '__main__':
    main()
