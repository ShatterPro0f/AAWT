# AAWT Installation Guide

## System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 500MB for application and dependencies
- **Display**: 1280x800 minimum resolution

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/ShatterPro0f/AAWT.git
cd AAWT
```

### 2. Create Virtual Environment (Recommended)

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `PyQt5` - GUI framework
- `python-docx` - Microsoft Word export
- `reportlab` - PDF export
- `ebooklib` - EPUB export
- `requests` - API communication
- `psutil` - Performance monitoring

### 4. Run the Application

```bash
python aawt.py
```

Or make it executable (Linux/macOS):
```bash
chmod +x aawt.py
./aawt.py
```

## First-Time Setup

### 1. Configure API Keys (Optional but Recommended)

On first launch, go to **Settings > API Keys** and add your API keys:

#### OpenAI (GPT models)
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Paste it in the OpenAI field
4. Click "Test Connection" to verify

#### Anthropic (Claude models)
1. Visit https://console.anthropic.com/
2. Generate an API key
3. Paste it in the Anthropic field
4. Click "Test Connection" to verify

#### Google (Gemini models)
1. Visit https://makersuite.google.com/app/apikey
2. Create an API key
3. Paste it in the Google field
4. Click "Test Connection" to verify

#### Ollama (Local LLMs - Free!)
1. Install Ollama from https://ollama.ai/
2. Run `ollama pull llama2` (or another model)
3. Start Ollama server: `ollama serve`
4. The default URL is `http://localhost:11434`
5. Click "Test Connection" to verify

**Note:** Ollama runs locally on your machine and is completely free!

### 2. Create Your First Project

1. Go to **Projects** > **New Project**
2. Enter project details:
   - **Project Name**: e.g., "My Fantasy Novel"
   - **Genre**: Select from dropdown
   - **Target Words**: Set your goal (e.g., 50,000)
3. Click **OK**
4. Your project is created!

### 3. Start Writing

1. Double-click your project in the Projects list
2. The Editor view opens automatically
3. Start typing your content
4. Auto-save runs every 60 seconds (configurable)

## Configuration

### Settings Location

All settings are stored in `config/user_settings.json`

You can edit this file directly or use the Settings UI.

### Database Location

The SQLite database is stored at `config/aawt.db`

### Project Storage

Projects are stored in the `projects/` directory:
```
projects/
└── My Project Name/
    ├── content.txt        # Your writing
    ├── metadata.json      # Project info
    ├── backups/           # Auto-backups
    └── exports/           # Exported files
```

## Troubleshooting

### Issue: PyQt5 Installation Fails

**Solution:**
```bash
# Try installing from system package manager first
# Ubuntu/Debian
sudo apt-get install python3-pyqt5

# Fedora
sudo dnf install python3-qt5

# macOS (with Homebrew)
brew install pyqt5
```

### Issue: "No module named 'src'"

**Solution:** Make sure you're running from the AAWT directory:
```bash
cd /path/to/AAWT
python aawt.py
```

### Issue: Database Errors

**Solution:** Delete the database and let it recreate:
```bash
rm config/aawt.db
python aawt.py
```

### Issue: Ollama Connection Failed

**Solution:** 
1. Make sure Ollama is installed
2. Start the Ollama server: `ollama serve`
3. Check the URL in Settings > API Keys > Ollama
4. Default is `http://localhost:11434`

### Issue: Export to PDF/DOCX/EPUB Fails

**Solution:** Ensure all optional dependencies are installed:
```bash
pip install python-docx reportlab ebooklib
```

### Issue: High CPU Usage

**Solution:** 
1. Go to Settings > Performance
2. Increase "Analytics Update Interval" to 5+ seconds
3. Disable real-time analysis if not needed

## Advanced Configuration

### Custom Database Path

Edit `config/user_settings.json`:
```json
{
  "advanced": {
    "database_path": "/path/to/custom/database.db"
  }
}
```

### Custom Project Directory

Edit `src/system/file_operations.py` initialization, or:
```python
from src.system.file_operations import FileOperations
files = FileOperations('/custom/projects/path')
```

### Connection Pool Size

For better performance with large projects:
```json
{
  "performance": {
    "connection_pool_size": 10
  }
}
```

## Updating

To update to the latest version:

```bash
cd AAWT
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstallation

1. Delete the AAWT directory
2. Optionally backup your projects first:
   ```bash
   cp -r AAWT/projects ~/my-writing-backup
   ```

## Support

For issues and questions:
1. Check the built-in Help documentation (Help menu)
2. Review the README.md file
3. Check troubleshooting section above
4. Create an issue on GitHub

## License

See LICENSE file for details.
