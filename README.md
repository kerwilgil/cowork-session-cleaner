# Cowork Session Cleaner 🧹

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Windows-lightgrey)

**English** | [Español](#español)

---

## Overview

A simple, cross-platform Python tool to **list, archive, unarchive, and delete** your Claude Cowork sessions. Automatically detects your operating system and user, with zero external dependencies.

### The Problem

Claude's Cowork mode stores sessions locally, but there's no built-in UI to:
- 📋 Bulk-delete old sessions
- 🗂️ View archived chats
- 💾 Free up disk space
- 🔄 Restore archived conversations

Over time, sessions pile up and eat disk space. This tool gives you full visibility and control.

### What It Does

✅ **Lists** all Cowork sessions with metadata (title, size, date, status)  
✅ **Deletes** sessions to free up disk space  
✅ **Archives** sessions to hide them from the sidebar  
✅ **Unarchives** sessions to restore previously hidden chats  
✅ **Auto-detects** your OS (Windows/Mac) and username  
✅ **Works offline** - no external dependencies  
✅ **Bilingual** - English & Spanish  
✅ **Safe** - dry-run mode to preview changes  

---

## Quick Start

### Prerequisites

- **macOS 10.14+** or **Windows 10+**
- **Python 3.8+** ([Install here](https://www.python.org/downloads/))
- Claude desktop app installed

### Installation

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/kerwil/cowork-session-cleaner.git
   cd cowork-session-cleaner
   ```

2. **Run the installer (one-time setup):**
   ```bash
   python3 install.py
   ```
   
   This will:
   - Detect your OS automatically
   - Add the tool to your system PATH
   - Verify the installation
   - Allow you to use `cowork` from any terminal

3. **Done!** You can now use the tool from anywhere:
   ```bash
   cowork
   ```

---

## Usage

### Basic Command

```bash
cowork
```

This opens an interactive menu:

```
🔍 Escaneando sesiones de Cowork...

==========================================================================================
  Gestor de Sesiones Cowork
  12 sesión(es)  |  9 activa(s), 3 archivada(s)  |  245.3 MB total
==========================================================================================

    #  Estado     Última Mod.        Tamaño     Título
  ---  --------   ----------------   ----------  ----------------------------------------
    1  activa     2026-03-19 14:22     52.3 MB  Website redesign project
    2  activa     2026-03-18 09:10     38.1 MB  Help me write a cover letter
    3  ARCHIVADA  2026-03-15 16:45     12.7 MB  Budget spreadsheet cleanup
    4  activa     2026-03-12 11:30      8.4 MB  Debug my Python script
    5  ARCHIVADA  2026-03-01 08:55      3.2 MB  Meeting notes summary
  ...

¿Qué deseas hacer?
  [D] Delete sessions
  [A] Show only ARCHIVED
  [V] View ALL sessions
  [S] Quit

Action: _
```

### Options

| Command | Action |
|---------|--------|
| **D** | Delete selected sessions |
| **A** | Show only archived sessions |
| **V** | View all sessions |
| **S** | Exit |

### Examples

**Delete specific sessions:**
```
Select: 1,3,5
```

**Delete a range:**
```
Select: 1-5
```

**Delete all shown sessions:**
```
Select: all
```

---

## For Advanced Users

### Run specific version

If you prefer a specific OS version:

```bash
# macOS only
python3 scripts/mac.py

# Windows only
python3 scripts/windows.py
```

### Dry-run mode (preview changes)

```bash
python3 scripts/windows.py --dry-run
python3 scripts/mac.py --dry-run
```

### Sort sessions

```bash
cowork --sort size          # Largest sessions first
cowork --sort date          # Newest first
cowork --sort name          # Alphabetical
```

---

## Troubleshooting

See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common issues:
- Python not found
- Session path not detected
- Permission errors
- Installation issues

---

## How It Works

### macOS
Sessions are stored in:
```
~/Library/Application Support/Claude/local-agent-mode-sessions/
```

### Windows
Sessions are stored in:
```
C:\Users\[YourUsername]\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions\
```

The tool reads session metadata, displays it, and allows you to manage sessions by modifying JSON files (archive status) or deleting folders (permanent deletion).

---

## Safety & Privacy

✅ **Local-only** - Never sends data anywhere  
✅ **No tracking** - No analytics or telemetry  
✅ **Open source** - Inspect the code yourself  
✅ **MIT License** - Free to use and modify  
✅ **Offline** - Works completely disconnected  

---

## Contributing

Suggestions and PRs are welcome! Ideas:

- [ ] Linux support
- [ ] Export session data before deletion
- [ ] Search by keyword
- [ ] Auto-archive sessions older than X days
- [ ] TUI interface with `rich` library

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

---

## License

MIT License - See [LICENSE](LICENSE) file

---

## Credits

Inspired by the original [cowork-session-cleaner](https://github.com/cloudenochcsis/cowork-session-cleaner) by cloudenochcsis.

---

# Español

## Vista General

Una herramienta simple y multiplataforma en Python para **listar, archivar, desarchivar y eliminar** tus sesiones de Claude Cowork. Detecta automáticamente tu sistema operativo y usuario, sin dependencias externas.

### El Problema

El modo Cowork de Claude almacena sesiones localmente, pero no hay una interfaz para:
- 📋 Eliminar sesiones en lote
- 🗂️ Ver chats archivados
- 💾 Liberar espacio en disco
- 🔄 Restaurar conversaciones archivadas

Con el tiempo, las sesiones se acumulan. Esta herramienta te da control total.

### Qué Hace

✅ **Lista** todas tus sesiones con metadatos  
✅ **Elimina** sesiones para liberar espacio  
✅ **Archiva** sesiones para ocultarlas  
✅ **Desarchiva** sesiones para restaurarlas  
✅ **Detecta automáticamente** tu SO y usuario  
✅ **Funciona sin conexión** - sin dependencias  
✅ **Bilingüe** - Inglés y Español  
✅ **Seguro** - modo preview antes de cambios  

---

## Inicio Rápido

### Requisitos

- **macOS 10.14+** o **Windows 10+**
- **Python 3.8+** ([Descargar aquí](https://www.python.org/downloads/))
- App de Claude instalada

### Instalación

1. **Clona o descarga el repositorio:**
   ```bash
   git clone https://github.com/kerwil/cowork-session-cleaner.git
   cd cowork-session-cleaner
   ```

2. **Ejecuta el instalador (una sola vez):**
   ```bash
   python3 install.py
   ```
   
   Esto:
   - Detecta tu SO automáticamente
   - Agrega la herramienta al PATH
   - Verifica la instalación
   - Te permite usar `cowork` desde cualquier terminal

3. **¡Listo!** Puedes usar la herramienta desde cualquier lado:
   ```bash
   cowork
   ```

---

## Uso

### Comando Básico

```bash
cowork
```

Se abre un menú interactivo (ver ejemplo arriba en inglés).

### Opciones

| Comando | Acción |
|---------|--------|
| **D** | Eliminar sesiones seleccionadas |
| **A** | Mostrar solo sesiones archivadas |
| **V** | Ver todas las sesiones |
| **S** | Salir |

### Ejemplos

**Eliminar sesiones específicas:**
```
Select: 1,3,5
```

**Eliminar un rango:**
```
Select: 1-5
```

**Eliminar todas:**
```
Select: all
```

---

## Para Usuarios Avanzados

### Versión específica del SO

```bash
# Solo macOS
python3 scripts/mac.py

# Solo Windows
python3 scripts/windows.py
```

### Modo preview

```bash
python3 scripts/windows.py --dry-run
python3 scripts/mac.py --dry-run
```

### Ordenar sesiones

```bash
cowork --sort size          # Más grandes primero
cowork --sort date          # Más nuevas primero
cowork --sort name          # Alfabético
```

---

## Solución de Problemas

Ver [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) para problemas comunes:
- Python no encontrado
- Ruta de sesiones no detectada
- Errores de permisos
- Problemas de instalación

---

## Seguridad y Privacidad

✅ **Solo local** - Nunca envía datos a internet  
✅ **Sin tracking** - Sin analytics ni telemetría  
✅ **Código abierto** - Inspecciona el código  
✅ **MIT License** - Libre de usar y modificar  
✅ **Sin conexión** - Funciona completamente desconectado  

---

## Contribuciones

¡Sugerencias y PRs bienvenidos! Ideas:

- [ ] Soporte para Linux
- [ ] Exportar sesiones antes de eliminar
- [ ] Buscar por palabra clave
- [ ] Auto-archivar sesiones antiguas
- [ ] Interfaz TUI con `rich`

Ver [CONTRIBUTING.md](docs/CONTRIBUTING.md) para directrices.

---

## Licencia

MIT License - Ver archivo [LICENSE](LICENSE)

---

## Créditos

Inspirado en el repositorio original [cowork-session-cleaner](https://github.com/cloudenochcsis/cowork-session-cleaner) por cloudenochcsis.
