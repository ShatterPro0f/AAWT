# AAWT Usage Guide

## Quick Start

### Launch the Application

```bash
python aawt.py
```

### Create Your First Project

1. Click **Projects** in the sidebar
2. Click **New Project** button
3. Fill in the details
4. Click **OK**

### Start Writing

1. Double-click your project to load it
2. The Editor opens automatically
3. Type your content
4. Changes are auto-saved every 60 seconds

## Main Interface

### Sidebar Navigation

- **Dashboard**: Overview of your current project
- **Projects**: Manage all your writing projects
- **Writing Editor**: Main text editing area
- **Analytics**: Detailed statistics and insights
- **Settings**: Configure the application
- **Help**: Built-in documentation

### Menu Bar

#### File Menu
- **New Project** (Ctrl+N): Create a new project
- **Open Project** (Ctrl+O): Load an existing project
- **Save** (Ctrl+S): Save current changes
- **Export** (Ctrl+E): Export to various formats
- **Exit** (Ctrl+Q): Close the application

#### Edit Menu
- **Undo** (Ctrl+Z): Undo last change
- **Redo** (Ctrl+Y): Redo undone change
- **Cut/Copy/Paste**: Standard clipboard operations
- **Select All** (Ctrl+A): Select all text

#### View Menu
- Quick navigation to all main views

#### Tools Menu
- **Analyze Text** (Ctrl+Alt+A): Run text analysis
- **AI Assistance** (Ctrl+Alt+I): Get AI help

#### Help Menu
- **Help Documentation** (F1): View help
- **About AAWT**: Application information

## Features Guide

### Project Management

#### Creating a Project

1. **Projects** > **New Project**
2. Enter details:
   - **Name**: Unique project identifier
   - **Genre**: Fiction, Fantasy, Sci-Fi, etc.
   - **Target Words**: Your word count goal
3. Click **OK**

The system creates:
- Database entry
- Project folder structure
- Initial metadata

#### Loading a Project

**Method 1:** Double-click in Projects list
**Method 2:** Select and click "Load Project"
**Method 3:** File > Open Project

When loaded:
- Content appears in Editor
- Dashboard updates with progress
- Writing session starts

#### Deleting a Project

1. Select project in list
2. Click **Delete Project**
3. Confirm deletion
4. Project is removed from database and disk

### Writing Editor

#### Text Editing

The editor provides:
- Rich text input with undo/redo
- Auto-save (configurable interval)
- Live word count
- Text analysis panel

#### Auto-Save

Default: Every 60 seconds

To configure:
1. **Settings** > **General**
2. Adjust "Auto-save interval"
3. Range: 30-3600 seconds

#### Text Analysis

Click **Analyze Text** to see:
- Word count
- Character count
- Sentence/paragraph counts
- Readability score (0-100)
- Grade level equivalent
- Repeated words
- Long sentences
- Reading time estimate

### AI Assistance

#### Using AI Features

1. Load a project
2. **Tools** > **AI Assistance**
3. Select provider:
   - **OpenAI**: GPT-3.5, GPT-4
   - **Anthropic**: Claude models
   - **Google**: Gemini
   - **Ollama**: Local models (free!)
4. Enter your prompt
5. Click **Generate**

#### Example Prompts

- "Continue this story"
- "Suggest improvements to this paragraph"
- "Generate dialogue between two characters"
- "Describe this scene in more detail"
- "What should happen next?"
- "Check for plot holes"

#### AI Best Practices

- Be specific in prompts
- Provide context from your story
- Review and edit AI suggestions
- Use AI as a tool, not a replacement
- Monitor API costs in Analytics

### Text Analysis

#### Readability Metrics

**Flesch Reading Ease (0-100)**
- 90-100: Very Easy (5th grade)
- 80-89: Easy (6th grade)
- 70-79: Fairly Easy (7th-8th grade)
- 60-69: Standard (9th-10th grade)
- 50-59: Fairly Difficult (11th-12th grade)
- 30-49: Difficult (College)
- 0-29: Very Difficult (College Graduate)

#### Understanding Analysis Results

- **Word Count**: Total words
- **Unique Words**: Vocabulary size
- **Vocabulary Diversity**: Percentage of unique words
- **Avg Words/Sentence**: Sentence length indicator
- **Repeated Words**: Words used too frequently
- **Long Sentences**: Sentences >25 words

#### Improving Readability

1. Break long sentences (>20-25 words)
2. Vary sentence length
3. Use simpler words when possible
4. Remove repeated words
5. Check the analysis regularly

### Export Features

#### Supported Formats

1. **TXT**: Plain text
2. **MD**: Markdown
3. **DOCX**: Microsoft Word
4. **PDF**: Portable Document
5. **EPUB**: E-book
6. **JSON**: Data format

#### How to Export

1. Load project in Editor
2. **File** > **Export** or click **Export** button
3. Select format
4. Choose options:
   - Include metadata
   - Include statistics
5. Click **OK**

Files are saved to `exports/` directory by default.

#### Export Options

**Metadata includes:**
- Project name
- Creation date
- Last modified
- Genre
- Target audience

**Statistics include:**
- Current word count
- Target word count
- Progress percentage

### Analytics

#### Text Analysis Tab

View comprehensive text metrics:
- All basic counts
- Readability scores
- Repeated words list
- Long sentences
- Grade level

Click **Refresh Analysis** to update.

#### API Usage Tab

Track your AI usage:
- Total API calls
- Total cost ($)
- Tokens used
- Breakdown by provider

Monitor to manage costs.

#### Session Stats Tab

See your writing patterns:
- Total sessions
- Total words written
- Average words per session
- Writing streak

### Settings

#### General Settings

- **Auto-save interval**: How often to save
- **Font family**: Editor font
- **Font size**: Editor text size

#### API Keys

Add keys for AI providers:
1. Get key from provider website
2. Paste in appropriate field
3. Click **Test Connection**
4. Key is saved automatically

**Security:** Keys are stored locally, never shared.

#### Writing Settings

- **Default tone**: Formal, Professional, etc.
- **Default POV**: First, Second, Third
- **Default genre**: Fiction, Fantasy, etc.
- **Daily word goal**: Target words per day
- **Enable checks**: Spell/grammar checking

#### Theme Settings

- **Theme**: Light or Dark mode
- **Primary color**: Accent color (#RRGGBB)

Changes apply immediately.

## Advanced Features

### Keyboard Shortcuts

#### File Operations
- `Ctrl+N`: New project
- `Ctrl+O`: Open project
- `Ctrl+S`: Save
- `Ctrl+E`: Export
- `Ctrl+Q`: Quit

#### Editing
- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo
- `Ctrl+X`: Cut
- `Ctrl+C`: Copy
- `Ctrl+V`: Paste
- `Ctrl+A`: Select All

#### Tools
- `Ctrl+Alt+A`: Analyze text
- `Ctrl+Alt+I`: AI assistance
- `F1`: Help

### Session Tracking

The application automatically tracks:
- Start time
- End time
- Words written
- Session duration

View in **Analytics** > **Session Stats**.

### Backup System

Automatic backups:
- Created when you make significant changes
- Stored in `projects/{name}/backups/`
- ZIP compressed
- Includes content and metadata

### Performance Monitoring

Status bar shows:
- CPU usage percentage
- Memory usage (MB)
- Cache entries count

Updates every 2 seconds.

### Database Maintenance

The application automatically:
- Clears expired cache (7 days)
- Optimizes database weekly
- Maintains connection pool

## Tips and Best Practices

### Writing Workflow

1. **Planning**: Create project, set target
2. **Writing**: Use editor, ignore mistakes
3. **Analysis**: Check readability after ~1000 words
4. **Revision**: Address repeated words, long sentences
5. **AI Assist**: Use for brainstorming, not first draft
6. **Export**: Save milestones as you progress

### Managing Large Projects

- Split into multiple projects (by chapter/section)
- Export regularly as backup
- Monitor database size in Analytics
- Use project naming conventions

### Optimizing Performance

- Increase auto-save interval for large documents
- Disable real-time analysis while writing
- Run analysis manually when needed
- Clear cache periodically (Settings)

### Using Ollama (Local LLM)

**Advantages:**
- Completely free
- No internet required
- Privacy (data stays local)
- No rate limits

**Setup:**
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2

# Start server
ollama serve
```

Then use in AAWT with provider "ollama".

## Troubleshooting

### Common Issues

#### Editor Not Responding
- Save your work (Ctrl+S)
- Restart the application
- Check logs in `logs/aawt.log`

#### Analysis Taking Too Long
- For very large documents (>50,000 words)
- Analysis may take 5-10 seconds
- This is normal

#### Export Fails
- Ensure dependencies installed
- Check export directory exists
- Review error message
- Check logs for details

### Getting Help

1. **Built-in Help**: Press F1
2. **README.md**: Comprehensive documentation
3. **INSTALL.md**: Installation guide
4. **Logs**: Check `logs/aawt.log`

## FAQ

**Q: How do I move projects between computers?**
A: Copy the project folder from `projects/` directory.

**Q: Can I edit the same project on multiple devices?**
A: Not simultaneously. Copy projects, edit, then merge manually.

**Q: What's the maximum project size?**
A: No hard limit, but performance may degrade beyond 100,000 words.

**Q: Are my API keys secure?**
A: Yes, they're stored locally and never transmitted except to the API provider.

**Q: Can I use AAWT offline?**
A: Yes! All features work offline except AI assistance.

**Q: How much do API calls cost?**
A: Varies by provider. Check Analytics > API Usage for your costs.

**Q: Is Ollama really free?**
A: Yes! It runs locally on your machine at no cost.

**Q: Can I customize the interface?**
A: Yes, via Settings > Theme. More customization coming soon.

**Q: Where are my projects stored?**
A: In the `projects/` directory within AAWT installation.

**Q: Can I import existing documents?**
A: Currently, copy/paste into editor. Import feature coming soon.
