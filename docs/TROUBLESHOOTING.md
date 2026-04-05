# Troubleshooting Guide

**English** | [Español](#español-1)

## Common Issues

### Python Not Found

**Error Message:**
```
'python' is not recognized as an internal or external command
```

**Solutions:**

1. **Verify Python is installed:**
   ```bash
   python --version
   ```

2. **If not installed:**
   - Download from [python.org](https://www.python.org/downloads/)
   - **IMPORTANT:** Check "Add Python to PATH" during installation
   - Restart your terminal/PowerShell

3. **Try alternative commands:**
   ```bash
   python3 --version
   py --version
   ```

4. **Add Python to PATH manually (Windows):**
   - Find your Python installation folder (usually `C:\Users\YourName\AppData\Local\Programs\Python\`)
   - Settings > System > About > Advanced system settings
   - Environment Variables > PATH > Edit
   - Add your Python folder path

---

### Installation Failed / PATH Not Configured

**Solution:**

1. Delete the tool from your system:
   - Windows: `C:\Users\YourName\AppData\Local\Programs\cowork`
   - macOS/Linux: `~/.local/bin/cowork`

2. Run installer again:
   ```bash
   python3 install.py
   ```

3. On Windows, run as Administrator:
   ```powershell
   python3 install.py
   ```

---

### "cowork: command not found"

**Problem:** Tool installed but can't be found from terminal.

**Solutions:**

1. **Close and reopen terminal:**
   - Completely close your terminal/PowerShell
   - Open a new one
   - Try again

2. **Reload shell configuration (macOS/Linux):**
   ```bash
   source ~/.zshrc
   # or
   source ~/.bash_profile
   ```

3. **Check if PATH is configured:**
   ```bash
   echo $PATH
   ```
   Should include `~/.local/bin` or your installation directory.

4. **Manually add to PATH:**
   - See INSTALLATION.md > Manual Installation

---

### Cowork Sessions Folder Not Found

**Error Message:**
```
❌ Cowork sessions folder not found
```

**Causes:**
1. Claude app not installed
2. Never used Cowork mode
3. Claude stores data in different location

**Solutions:**

1. **Verify Claude is installed:**
   - Download from [claude.ai/desktop](https://claude.ai/desktop)
   - Install and open

2. **Use Cowork mode at least once:**
   - Open Claude
   - Click "Cowork" tab
   - Create a test session
   - Close app

3. **Run the tool again:**
   ```bash
   cowork
   ```

4. **Check session folder manually:**

   **Windows:**
   ```
   C:\Users\YourUsername\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions
   ```

   **macOS:**
   ```
   ~/Library/Application Support/Claude/local-agent-mode-sessions
   ```

   If folder exists but tool doesn't find it, the username detection might be wrong. Contact support with your username (first part of command prompt).

---

### Permission Denied (macOS/Linux)

**Error:**
```
Permission denied
```

**Solution:**

Make the script executable:
```bash
chmod +x ~/.local/bin/cowork
```

---

### Script Runs But No Sessions Appear

**Possible Causes:**
1. No Cowork sessions created yet
2. All sessions were already deleted
3. Sessions folder is empty

**Verification:**

**Windows - Check folder:**
```powershell
dir "C:\Users\YourUsername\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions"
```

**macOS - Check folder:**
```bash
ls -la ~/Library/Application\ Support/Claude/local-agent-mode-sessions
```

If the folder is empty or doesn't exist, create a test session in Claude Cowork first.

---

### Deleted Sessions Still Appear

**Problem:** Deleted sessions show up again after restart.

**Causes:**
1. Deletion didn't complete properly
2. Different session metadata file

**Solution:**

Run the tool again and try deleting with explicit confirmation:
```bash
cowork
# Select [D]
# Enter session numbers (e.g., 1)
# Type "yes" when prompted for confirmation
```

If problem persists, manually delete folder:

**Windows:**
```powershell
Remove-Item -Path "C:\Users\YourUsername\AppData\Local\...\local_SESSION_ID" -Recurse -Force
```

---

### Language Not in Spanish/English

**Problem:** Menu appears in wrong language.

**Note:** Language detection is automatic based on system locale. Currently supports English and Spanish.

**Workaround:**
- Set your system language to English or Spanish
- Or edit the script manually to force a language

---

### "No module named 'xyz'"

**This shouldn't happen** - the tool uses only Python standard library (no external dependencies).

**If you see this error:**

1. Check Python version:
   ```bash
   python3 --version
   ```

2. Verify you're using the correct Python:
   ```bash
   which python3
   ```

3. Try reinstalling:
   ```bash
   python3 install.py
   ```

---

### Claude App Needs Restart

After deleting or archiving/unarchiving sessions, Claude needs to restart to show changes.

**Solution:**

Close Claude completely:
- **Windows:** Close from system tray (if running in background)
- **macOS:** CMD+Q to fully quit

Then reopen Claude.

---

# Español

## Problemas Comunes

### Python No Encontrado

**Mensaje de Error:**
```
'python' no se reconoce como un comando interno o externo
```

**Soluciones:**

1. **Verifica que Python está instalado:**
   ```bash
   python --version
   ```

2. **Si no está instalado:**
   - Descarga desde [python.org](https://www.python.org/downloads/)
   - **IMPORTANTE:** Marca "Add Python to PATH" durante la instalación
   - Reinicia tu terminal/PowerShell

3. **Intenta comandos alternativos:**
   ```bash
   python3 --version
   py --version
   ```

4. **Agrega Python al PATH manualmente (Windows):**
   - Encuentra tu carpeta de instalación de Python (usualmente `C:\Users\TuNombre\AppData\Local\Programs\Python\`)
   - Settings > System > About > Advanced system settings
   - Environment Variables > PATH > Edit
   - Agrega la ruta de tu carpeta Python

---

### Instalación Fallida / PATH No Configurado

**Solución:**

1. Elimina la herramienta de tu sistema:
   - Windows: `C:\Users\TuNombre\AppData\Local\Programs\cowork`
   - macOS/Linux: `~/.local/bin/cowork`

2. Ejecuta el instalador nuevamente:
   ```bash
   python3 install.py
   ```

3. En Windows, ejecuta como Administrador:
   ```powershell
   python3 install.py
   ```

---

### "cowork: command not found" / "comando no encontrado"

**Problema:** Herramienta instalada pero no se encuentra desde la terminal.

**Soluciones:**

1. **Cierra y reabre la terminal:**
   - Cierra completamente tu terminal/PowerShell
   - Abre una nueva
   - Intenta de nuevo

2. **Recarga la configuración del shell (macOS/Linux):**
   ```bash
   source ~/.zshrc
   # o
   source ~/.bash_profile
   ```

3. **Verifica si el PATH está configurado:**
   ```bash
   echo $PATH
   ```
   Debería incluir `~/.local/bin` o tu directorio de instalación.

4. **Agrega manualmente al PATH:**
   - Ver INSTALLATION.md > Manual Installation

---

### Carpeta de Sesiones Cowork No Encontrada

**Mensaje de Error:**
```
❌ Carpeta de sesiones Cowork no encontrada
```

**Causas:**
1. App de Claude no instalada
2. Nunca usó el modo Cowork
3. Claude almacena datos en otra ubicación

**Soluciones:**

1. **Verifica que Claude está instalado:**
   - Descarga desde [claude.ai/desktop](https://claude.ai/desktop)
   - Instala y abre

2. **Usa el modo Cowork al menos una vez:**
   - Abre Claude
   - Haz clic en la pestaña "Cowork"
   - Crea una sesión de prueba
   - Cierra la app

3. **Ejecuta la herramienta nuevamente:**
   ```bash
   cowork
   ```

4. **Verifica la carpeta manualmente:**

   **Windows:**
   ```
   C:\Users\TuNombre\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions
   ```

   **macOS:**
   ```
   ~/Library/Application Support/Claude/local-agent-mode-sessions
   ```

   Si la carpeta existe pero la herramienta no la encuentra, la detección de usuario podría estar mal. Contacta con soporte con tu nombre de usuario (primera parte del prompt).

---

### Permiso Denegado (macOS/Linux)

**Error:**
```
Permission denied
```

**Solución:**

Haz el script ejecutable:
```bash
chmod +x ~/.local/bin/cowork
```

---

### El Script Se Ejecuta Pero No Aparecen Sesiones

**Posibles Causas:**
1. Ninguna sesión Cowork creada aún
2. Todas las sesiones fueron eliminadas
3. Carpeta de sesiones está vacía

**Verificación:**

**Windows - Verifica carpeta:**
```powershell
dir "C:\Users\TuNombre\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions"
```

**macOS - Verifica carpeta:**
```bash
ls -la ~/Library/Application\ Support/Claude/local-agent-mode-sessions
```

Si la carpeta está vacía o no existe, crea una sesión de prueba en Claude Cowork primero.

---

### Sesiones Eliminadas Aún Aparecen

**Problema:** Las sesiones eliminadas vuelven a aparecer después de reiniciar.

**Causas:**
1. La eliminación no se completó correctamente
2. Archivo de metadatos diferente

**Solución:**

Ejecuta la herramienta de nuevo e intenta eliminar con confirmación explícita:
```bash
cowork
# Selecciona [D]
# Ingresa números de sesiones (ej: 1)
# Escribe "sí" cuando se te pida confirmación
```

Si el problema persiste, elimina manualmente la carpeta:

**Windows:**
```powershell
Remove-Item -Path "C:\Users\TuNombre\AppData\Local\...\local_SESSION_ID" -Recurse -Force
```

---

### Idioma No en Español/Inglés

**Problema:** El menú aparece en idioma incorrecto.

**Nota:** La detección de idioma es automática basada en la locale del sistema. Actualmente soporta inglés y español.

**Solución:**
- Configura tu idioma del sistema a inglés o español
- O edita manualmente el script para forzar un idioma

---

### "No module named 'xyz'"

**Esto no debería ocurrir** - la herramienta usa solo la librería estándar de Python (sin dependencias externas).

**Si ves este error:**

1. Verifica la versión de Python:
   ```bash
   python3 --version
   ```

2. Verifica que estés usando el Python correcto:
   ```bash
   which python3
   ```

3. Intenta reinstalar:
   ```bash
   python3 install.py
   ```

---

### Claude Necesita Reiniciar

Después de eliminar o archivar/desarchivar sesiones, Claude necesita reiniciarse para mostrar los cambios.

**Solución:**

Cierra Claude completamente:
- **Windows:** Cierra desde la bandeja del sistema (si está en segundo plano)
- **macOS:** CMD+Q para cerrar completamente

Luego reabre Claude.
