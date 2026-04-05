# Contributing

**English** | [Español](#español)

## How to Contribute

We welcome contributions! Here are some ways you can help:

### Report Bugs

Found a bug? Open an issue on GitHub with:
- Your OS (Windows/macOS/Linux)
- Python version (`python --version`)
- Error message (complete output)
- Steps to reproduce

### Suggest Features

Have an idea? Open an issue with:
- Feature description
- Use case (why you need it)
- Proposed behavior

### Code Contributions

1. **Fork the repository**
2. **Create a branch:**
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Make your changes** (follow the style guide below)
4. **Test your changes:**
   ```bash
   python3 cowork_cleaner.py
   ```
5. **Commit with clear messages:**
   ```bash
   git commit -m "Add feature: description"
   ```
6. **Push to your fork:**
   ```bash
   git push origin feature/my-feature
   ```
7. **Open a Pull Request** with description of changes

## Code Style

- **Python 3.8+ compatible**
- Use standard library only (no external dependencies)
- PEP 8 style guide
- Clear variable names
- Comments for complex logic
- No trailing whitespace

## Project Structure

```
cowork-session-cleaner/
├── cowork_cleaner.py        # Main multi-platform script
├── install.py               # Installation script
├── scripts/
│   ├── windows.py           # Windows-specific version
│   └── mac.py               # macOS-specific version
├── docs/
│   ├── INSTALLATION.md
│   ├── TROUBLESHOOTING.md
│   └── CONTRIBUTING.md
└── .github/
    └── workflows/
        └── tests.yml        # GitHub Actions config
```

## Development Workflow

### Testing

1. Test on Windows and macOS if possible
2. Test with Python 3.8, 3.10, 3.12
3. Test edge cases (no sessions, large folders, permission errors)

### Adding Features

1. **Update the appropriate script(s):**
   - Feature in all versions → update `cowork_cleaner.py` + `scripts/`
   - OS-specific → update only that version

2. **Update documentation:**
   - New options → update README.md
   - New command → add to docs/USAGE.md (when created)
   - Known issues → add to docs/TROUBLESHOOTING.md

3. **Update GitHub Actions** if new dependencies needed (we avoid them!)

### Common Improvements

These are areas we're looking for help with:

- [ ] **Linux support** - Adapt paths for Linux systems
- [ ] **Export sessions** - Dump conversation data before deletion
- [ ] **Search by keyword** - Filter sessions by title
- [ ] **Auto-archive old** - Archive sessions older than X days
- [ ] **TUI interface** - Use `rich` library for prettier UI
- [ ] **Batch operations** - Script to delete multiple sessions programmatically
- [ ] **Configuration file** - .coworkrc for user preferences

## Questions?

- Open an issue labeled "question"
- Include OS, Python version, and detailed description
- We'll help!

---

# Español

## Cómo Contribuir

¡Bienvenidas las contribuciones! Aquí hay formas en que puedes ayudar:

### Reportar Bugs

¿Encontraste un bug? Abre un issue en GitHub con:
- Tu SO (Windows/macOS/Linux)
- Versión de Python (`python --version`)
- Mensaje de error (salida completa)
- Pasos para reproducir

### Sugerir Características

¿Tienes una idea? Abre un issue con:
- Descripción de la característica
- Caso de uso (por qué la necesitas)
- Comportamiento esperado

### Contribuciones de Código

1. **Fork el repositorio**
2. **Crea una rama:**
   ```bash
   git checkout -b feature/mi-caracteristica
   ```
3. **Haz tus cambios** (sigue la guía de estilo abajo)
4. **Prueba tus cambios:**
   ```bash
   python3 cowork_cleaner.py
   ```
5. **Commit con mensajes claros:**
   ```bash
   git commit -m "Agregar característica: descripción"
   ```
6. **Push a tu fork:**
   ```bash
   git push origin feature/mi-caracteristica
   ```
7. **Abre un Pull Request** con descripción de cambios

## Estilo de Código

- **Python 3.8+ compatible**
- Solo librería estándar (sin dependencias externas)
- Guía de estilo PEP 8
- Nombres de variable claros
- Comentarios para lógica compleja
- Sin espacios en blanco al final

## Estructura del Proyecto

```
cowork-session-cleaner/
├── cowork_cleaner.py        # Script principal multiplataforma
├── install.py               # Script de instalación
├── scripts/
│   ├── windows.py           # Versión específica para Windows
│   └── mac.py               # Versión específica para macOS
├── docs/
│   ├── INSTALLATION.md
│   ├── TROUBLESHOOTING.md
│   └── CONTRIBUTING.md
└── .github/
    └── workflows/
        └── tests.yml        # Configuración GitHub Actions
```

## Flujo de Desarrollo

### Pruebas

1. Prueba en Windows y macOS si es posible
2. Prueba con Python 3.8, 3.10, 3.12
3. Prueba casos extremos (sin sesiones, carpetas grandes, errores de permiso)

### Agregar Características

1. **Actualiza el(los) script(s) apropiado(s):**
   - Característica en todas las versiones → actualiza `cowork_cleaner.py` + `scripts/`
   - Específica del SO → actualiza solo esa versión

2. **Actualiza la documentación:**
   - Nuevas opciones → actualiza README.md
   - Nuevo comando → agrega a docs/USAGE.md (cuando se cree)
   - Problemas conocidos → agrega a docs/TROUBLESHOOTING.md

3. **Actualiza GitHub Actions** si nuevas dependencias son necesarias (¡las evitamos!)

### Mejoras Comunes

Estas son áreas donde buscamos ayuda:

- [ ] **Soporte para Linux** - Adapta rutas para sistemas Linux
- [ ] **Exportar sesiones** - Descarga datos de conversación antes de eliminar
- [ ] **Búsqueda por palabra clave** - Filtra sesiones por título
- [ ] **Auto-archivar antiguas** - Archiva sesiones más antiguas que X días
- [ ] **Interfaz TUI** - Usa librería `rich` para UI más bonita
- [ ] **Operaciones en lote** - Script para eliminar múltiples sesiones programáticamente
- [ ] **Archivo de configuración** - .coworkrc para preferencias del usuario

## ¿Preguntas?

- Abre un issue etiquetado como "question"
- Incluye SO, versión de Python y descripción detallada
- ¡Te ayudaremos!
