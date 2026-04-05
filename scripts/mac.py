#!/usr/bin/env python3
"""
Cowork Session Cleaner - macOS Edition
Manages Claude Cowork sessions on macOS systems
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

def get_cowork_sessions_path():
    """Get the Cowork sessions path for macOS"""
    return Path.home() / 'Library' / 'Application Support' / 'Claude' / 'local-agent-mode-sessions'

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
    
    if not base_path.exists():
        print(f"❌ Cowork sessions folder not found at: {base_path}")
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
        print("ℹ️  No sessions to show.")
        return
    
    archived_count = sum(1 for s in sessions if s['archived'])
    active_count = len(sessions) - archived_count
    total_size = sum(s['size_mb'] for s in sessions)
    
    print("\n" + "="*90)
    print(f"  Cowork Session Manager")
    print(f"  {len(sessions)} session(s)  |  {active_count} active, {archived_count} archived  |  {total_size:.1f} MB total")
    print("="*90 + "\n")
    
    print(f"{'#':<4} {'Status':<10} {'Last Modified':<18} {'Size':<10} {'Title':<45}")
    print("-" * 90)
    
    for idx, session in enumerate(sessions, 1):
        status = "ARCHIVED" if session['archived'] else "active"
        print(f"{idx:<4} {status:<10} {session['mod_date']:<18} {session['size_mb']:>7.1f} MB  {session['title']:<45}")
    
    print()

def delete_sessions(sessions, indices):
    """Delete selected sessions"""
    if not indices:
        print("❌ No sessions selected.")
        return
    
    to_delete = [sessions[i-1] for i in indices if 0 < i <= len(sessions)]
    
    if not to_delete:
        print("❌ Invalid selection.")
        return
    
    print("\n" + "="*90)
    print(f"Sessions to DELETE ({len(to_delete)}):")
    print("="*90)
    for session in to_delete:
        status = "ARCHIVED" if session['archived'] else "active"
        print(f"  [{status}] {session['title']}")
        print(f"       {session['path']}")
    
    confirm = input("\n⚠️  Are you sure you want to DELETE these sessions? (yes/no): ").strip().lower()
    
    if confirm not in ['yes', 'y']:
        print("❌ Cancelled.")
        return
    
    deleted_count = 0
    for session in to_delete:
        try:
            shutil.rmtree(session['path'])
            print(f"✅ Deleted: {session['title']}")
            deleted_count += 1
        except Exception as e:
            print(f"❌ Error deleting '{session['title']}': {e}")
    
    print(f"\n✅ Completed. Deleted {deleted_count} session(s).")
    print("Restart Claude for changes to take effect.")

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
    print("\n🔍 Scanning Cowork sessions...\n")
    
    all_sessions = list_sessions()
    
    if not all_sessions:
        return
    
    while True:
        display_sessions(all_sessions)
        
        print("What would you like to do?")
        print("  [D] Delete sessions")
        print("  [A] Show only ARCHIVED")
        print("  [V] View ALL sessions")
        print("  [S] Quit")
        print()
        
        action = input("Action: ").strip().upper()
        
        if action == 'D':
            if not all_sessions:
                print("❌ No sessions to delete.")
                continue
            
            selection = input("\nEnter session numbers (e.g., 1,3,5 or 1-5 or all): ").strip()
            indices = parse_selection(selection, len(all_sessions))
            
            if indices:
                delete_sessions(all_sessions, indices)
                all_sessions = list_sessions()
            else:
                print("❌ Invalid selection.")
        
        elif action == 'A':
            archived = list_sessions(filter_type='archived')
            display_sessions(archived)
            
            if archived:
                selection = input("Enter session numbers to delete (e.g., 1,3,5 or all): ").strip()
                indices = parse_selection(selection, len(archived))
                
                if indices:
                    delete_sessions(archived, indices)
                    all_sessions = list_sessions()
        
        elif action == 'V':
            all_sessions = list_sessions()
        
        elif action == 'S':
            print("👋 Goodbye.")
            break
        
        else:
            print("❌ Action not recognized.")

if __name__ == '__main__':
    main()
