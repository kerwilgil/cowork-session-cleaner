# Installation Guide

**English** | [Español](#español-1)

## System Requirements

- **macOS 10.14+** or **Windows 10+**
- **Python 3.8+**
- Claude desktop app installed

## Install Python

If you don't have Python installed:

### macOS

Using Homebrew (recommended):
```bash
brew install python3
```

Or download from [python.org](https://www.python.org/downloads/)

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click "Download Python" (latest version)
3. Run the installer
4. **IMPORTANT:** Check the box "Add Python to PATH"
5. Click "Install Now"

Verify installation:
```powershell
python --version
```

## Installation Steps

### Step 1: Clone or Download

**Option A: Using Git**
```bash
git clone https://github.com/kerwil/cowork-session-cleaner.git
cd cowork-session-cleaner
```

**Option B: Download ZIP**
- Visit https://github.com/kerwil/cowork-session-cleaner
- Click "Code" > "Download ZIP"
- Extract to a folder
- Open terminal/PowerShell in that folder

### Step 2: Run the Installer

```bash
python3 install.py
```

This will:
- Detect your OS (Windows/Mac/Linux)
- Create necessary files
- Add the tool to your system PATH
- Allow you to run `cowork` from anywhere

### Step 3: Restart Terminal

Close and reopen your terminal/PowerShell to apply PATH changes.

### Step 4: Verify Installation

```bash
cowork
```

You should see the Cowork Session Manager menu.

---

## Troubleshooting

### "Python was not found"

**Windows:**
- Make sure you installed Python with "Add Python to PATH" checked
- Restart PowerShell after installing Python
- Try `python --version` instead of `python3`

**macOS/Linux:**
- Install Python using Homebrew: `brew install python3`
- Or download from [python.org](https://www.python.org/downloads/)

### "cowork: command not found"

1. Close your terminal completely
2. Reopen a new terminal window
3. Try again

If that doesn't work:
- **Windows:** Run `install.py` again with administrator privileges
- **macOS/Linux:** Run `source ~/.zshrc` or `source ~/.bash_profile`

### "Permission denied" (macOS/Linux)

Make sure the script is executable:
```bash
chmod +x ~/.local/bin/cowork
```

### Cowork sessions folder not found

The tool couldn't find your Cowork sessions. Make sure:
1. Claude desktop app is installed
2. You've used Cowork mode at least once
3. Your username is correctly detected

---

## Manual Installation (Advanced)

If the automatic installer doesn't work, you can set it up manually:

### macOS/Linux

1. Create a script in your PATH:
```bash
mkdir -p ~/.local/bin
nano ~/.local/bin/cowork
```

2. Paste this content:
```bash
#!/bin/bash
python3 "/path/to/cowork-session-cleaner/cowork_cleaner.py" "$@"
```

Replace `/path/to/` with the actual path.

3. Save and make executable:
```bash
chmod +x ~/.local/bin/cowork
```

4. Add to PATH (in ~/.zshrc or ~/.bash_profile):
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows

1. Create a batch file:
```powershell
notepad %APPDATA%\cowork.bat
```

2. Paste:
```batch
@echo off
python "C:\path\to\cowork-session-cleaner\cowork_cleaner.py" %*
```

3. Add the directory to PATH manually via Settings.

---

# Español

## Requisitos del Sistema

- **macOS 10.14+** o **Windows 10+**
- **Python 3.8+**
- App de Claude instalada

## Instalar Python

Si no tienes Python instalado:

### macOS

Con Homebrew (recomendado):
```bash
brew install python3
```

O descarga desde [python.org](https://www.python.org/downloads/)

### Windows

1. Ve a [python.org/downloads](https://www.python.org/downloads/)
2. Haz clic en "Download Python" (última versión)
3. Ejecuta el instalador
4. **IMPORTANTE:** Marca la casilla "Add Python to PATH"
5. Haz clic en "Install Now"

Verifica la instalación:
```powershell
python --version
```

## Pasos de Instalación

### Paso 1: Clonar o Descargar

**Opción A: Con Git**
```bash
git clone https://github.com/kerwil/cowork-session-cleaner.git
cd cowork-session-cleaner
```

**Opción B: Descargar ZIP**
- Visita https://github.com/kerwil/cowork-session-cleaner
- Haz clic en "Code" > "Download ZIP"
- Extrae en una carpeta
- Abre terminal/PowerShell en esa carpeta

### Paso 2: Ejecutar el Instalador

```bash
python3 install.py
```

Esto:
- Detectará tu SO (Windows/Mac/Linux)
- Creará los archivos necesarios
- Agregará la herramienta al PATH
- Te permitirá usar `cowork` desde cualquier lado

### Paso 3: Reinicia la Terminal

Cierra y reabre tu terminal/PowerShell para aplicar los cambios.

### Paso 4: Verifica la Instalación

```bash
cowork
```

Deberías ver el menú del Gestor de Sesiones Cowork.

---

## Solución de Problemas

### "Python was not found" / "Python no encontrado"

**Windows:**
- Asegúrate de haber instalado Python con "Add Python to PATH" marcado
- Reinicia PowerShell después de instalar Python
- Intenta `python --version` en lugar de `python3`

**macOS/Linux:**
- Instala Python con Homebrew: `brew install python3`
- O descarga desde [python.org](https://www.python.org/downloads/)

### "cowork: command not found" / "comando no encontrado"

1. Cierra tu terminal completamente
2. Abre una nueva ventana de terminal
3. Intenta de nuevo

Si no funciona:
- **Windows:** Ejecuta `install.py` nuevamente con privilegios de administrador
- **macOS/Linux:** Ejecuta `source ~/.zshrc` o `source ~/.bash_profile`

### "Permission denied" (macOS/Linux)

Asegúrate de que el script sea ejecutable:
```bash
chmod +x ~/.local/bin/cowork
```

### Carpeta de sesiones Cowork no encontrada

La herramienta no pudo encontrar tus sesiones. Verifica:
1. App de Claude está instalada
2. Has usado el modo Cowork al menos una vez
3. Tu nombre de usuario se detecta correctamente

---

## Instalación Manual (Avanzado)

Si el instalador automático no funciona, puedes configurarlo manualmente:

### macOS/Linux

1. Crea un script en tu PATH:
```bash
mkdir -p ~/.local/bin
nano ~/.local/bin/cowork
```

2. Pega este contenido:
```bash
#!/bin/bash
python3 "/ruta/a/cowork-session-cleaner/cowork_cleaner.py" "$@"
```

Reemplaza `/ruta/a/` con la ruta real.

3. Guarda y hazlo ejecutable:
```bash
chmod +x ~/.local/bin/cowork
```

4. Agrega al PATH (en ~/.zshrc o ~/.bash_profile):
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows

1. Crea un archivo batch:
```powershell
notepad %APPDATA%\cowork.bat
```

2. Pega:
```batch
@echo off
python "C:\ruta\a\cowork-session-cleaner\cowork_cleaner.py" %*
```

3. Agrega el directorio al PATH manualmente vía Settings.
