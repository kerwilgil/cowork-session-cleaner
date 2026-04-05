#!/usr/bin/env python3
"""
Cowork Session Cleaner - Installer
Sets up the tool to run from anywhere on your system
"""

import os
import sys
import platform
import shutil
import subprocess
from pathlib import Path

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

def get_install_dir():
    """Get the directory where the script will be installed"""
    os_type = get_os_type()
    
    if os_type == 'mac' or os_type == 'linux':
        return Path.home() / '.local' / 'bin'
    elif os_type == 'windows':
        return Path.home() / 'AppData' / 'Local' / 'Programs' / 'cowork'
    
    return None

def get_script_content_mac_linux():
    """Get the wrapper script content for macOS/Linux"""
    script_dir = Path(__file__).parent.resolve()
    return f"""#!/bin/bash
python3 "{script_dir}/cowork_cleaner.py" "$@"
"""

def get_batch_content_windows():
    """Get the wrapper batch script content for Windows"""
    script_dir = Path(__file__).parent.resolve()
    return f"""@echo off
python "{script_dir}\\cowork_cleaner.py" %*
"""

def install_mac_linux():
    """Install on macOS/Linux"""
    print("📦 Setting up for macOS/Linux...\n")
    
    install_dir = get_install_dir()
    install_dir.mkdir(parents=True, exist_ok=True)
    
    wrapper_path = install_dir / 'cowork'
    
    try:
        with open(wrapper_path, 'w') as f:
            f.write(get_script_content_mac_linux())
        
        os.chmod(wrapper_path, 0o755)
        print(f"✅ Wrapper script created at: {wrapper_path}")
    except Exception as e:
        print(f"❌ Error creating wrapper: {e}")
        return False
    
    # Check if ~/.local/bin is in PATH
    shell_profile = Path.home() / '.zshrc'
    if not shell_profile.exists():
        shell_profile = Path.home() / '.bash_profile'
    
    if not shell_profile.exists():
        shell_profile = Path.home() / '.bashrc'
    
    path_line = f'export PATH="{install_dir}:$PATH"'
    
    try:
        if shell_profile.exists():
            with open(shell_profile, 'r') as f:
                content = f.read()
            
            if str(install_dir) not in content:
                with open(shell_profile, 'a') as f:
                    f.write(f"\n# Cowork Session Cleaner\n{path_line}\n")
                print(f"✅ Added PATH to: {shell_profile}")
                print(f"⚠️  Run: source {shell_profile}")
            else:
                print(f"✅ PATH already configured in: {shell_profile}")
        else:
            print(f"⚠️  No shell profile found. Please add this to your shell config:")
            print(f"   {path_line}")
    except Exception as e:
        print(f"⚠️  Could not update shell profile: {e}")
        print(f"   Please add this to your shell config manually:")
        print(f"   {path_line}")
    
    return True

def install_windows():
    """Install on Windows"""
    print("📦 Setting up for Windows...\n")
    
    install_dir = get_install_dir()
    install_dir.mkdir(parents=True, exist_ok=True)
    
    batch_path = install_dir / 'cowork.bat'
    
    try:
        with open(batch_path, 'w') as f:
            f.write(get_batch_content_windows())
        print(f"✅ Batch script created at: {batch_path}")
    except Exception as e:
        print(f"❌ Error creating batch script: {e}")
        return False
    
    # Try to add to PATH using setx
    try:
        current_path = os.environ.get('PATH', '')
        if str(install_dir) not in current_path:
            subprocess.run(
                ['setx', 'PATH', f"{current_path};{install_dir}"],
                check=True,
                capture_output=True
            )
            print(f"✅ Added {install_dir} to PATH")
            print(f"⚠️  Close and reopen PowerShell for PATH changes to take effect")
        else:
            print(f"✅ {install_dir} is already in PATH")
    except Exception as e:
        print(f"⚠️  Could not add to PATH automatically: {e}")
        print(f"   Please add {install_dir} to your PATH manually:")
        print(f"   Settings > System > About > Advanced system settings")
        print(f"   > Environment Variables > PATH > New > {install_dir}")
    
    return True

def verify_installation():
    """Verify the installation"""
    print("\n🔍 Verifying installation...\n")
    
    os_type = get_os_type()
    
    try:
        if os_type == 'mac' or os_type == 'linux':
            result = subprocess.run(['cowork', '--version'], capture_output=True, timeout=5)
            if result.returncode == 0:
                print("✅ Installation verified!")
                return True
        elif os_type == 'windows':
            result = subprocess.run(['cowork', '--version'], capture_output=True, timeout=5, shell=True)
            if result.returncode == 0:
                print("✅ Installation verified!")
                return True
    except subprocess.TimeoutExpired:
        pass
    except FileNotFoundError:
        pass
    
    print("⚠️  Could not verify installation from command line.")
    print("   Try opening a new terminal/PowerShell window and running: cowork")
    return False

def main():
    """Main installer"""
    print("="*60)
    print("  Cowork Session Cleaner - Installer")
    print("="*60)
    print()
    
    os_type = get_os_type()
    
    if not os_type:
        print("❌ Unsupported operating system")
        sys.exit(1)
    
    print(f"Detected OS: {os_type.upper()}\n")
    
    if os_type == 'windows':
        success = install_windows()
    else:
        success = install_mac_linux()
    
    if success:
        print("\n✅ Installation complete!")
        print("\nYou can now use 'cowork' from any terminal/PowerShell window.\n")
    else:
        print("\n❌ Installation failed")
        sys.exit(1)

if __name__ == '__main__':
    main()
