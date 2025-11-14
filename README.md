# AAWT
AI Assisted Writing Tool

**An integrated writing platform for authors who want real-time analysis, versioning, and AI-assisted improvements.**

## Comprehensive Feature Documentation

**Version:** 2.0
**Last Updated:** November 2024
**Purpose:** Complete documentation of all AAWT features, designed to help writers manage drafts, track changes, and stay organized in their world-building and writing projects

---

# Table of Contents
1. [Application Overview](#application-overview)
2. [Getting Started](#getting-started)
3. [Core Architecture](#core-architecture)
4. [User Interface Components](#user-interface-components)
5. [Text Analysis & Writing Tools](#text-analysis--writing-tools)
6. [Project Storage & Organization](#project-storage--organization)
7. [Writing Session Mechanics](#writing-session-mechanics)
8. [Undo/Redo System & Versioning](#undoredo-system--versioning)
9. [API Integration & Caching](#api-integration--caching)
10. [Settings & Configuration](#settings--configuration)
11. [Export Functionality](#export-functionality)
12. [Security & Privacy](#security--privacy)
13. [Performance & Scalability](#performance--scalability)
14. [Accessibility Features](#accessibility-features)
15. [Multi-Language Support](#multi-language-support)
16. [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference)
17. [Theme System](#theme-system)
18. [Notification System](#notification-system)
19. [Help & Documentation System](#help--documentation-system)
20. [Best Practices for Writers](#best-practices-for-writers)
21. [Future Enhancements & Roadmap](#future-enhancements--roadmap)
22. [Workflow & User Flows](#workflow--user-flows)
23. [Troubleshooting & Support](#troubleshooting--support)
24. [Technical Reference](#technical-reference)

---

# Application Overview

## Purpose

AAWT is a comprehensive desktop application designed to assist writers—particularly those working on fantasy, fiction, and world-building projects—through an integrated writing system with real-time analysis, quality checking, and multi-format export capabilities. 

**Key User Pain Points Addressed:**
- **Managing Drafts:** Keep track of multiple versions and iterations of your work with automatic versioning
- **Tracking Changes:** Monitor every modification with detailed change history and undo/redo capabilities
- **Staying Organized:** Manage complex projects with character lists, plot outlines, and session tracking
- **Improving Quality:** Get real-time feedback on readability, grammar, and style consistency
- **Collaborating with AI:** Leverage AI assistance for brainstorming, continuation, and refinement
- **World-Building:** Maintain consistency across character names, places, and terminology in complex fictional worlds

Whether you're crafting an epic fantasy series, developing intricate characters, or building detailed fictional universes, AAWT helps you stay organized and maintain quality throughout your writing journey.

## Technology Stack
- **Language:** Python 3.x
- **GUI Framework:** PyQt5 (Graphical User Interface)
- **Database:** SQLite 3 with connection pooling
- **External APIs:** OpenAI, Anthropic, Google, Words API, ApyHub Readability API (API = Application Programming Interface)
- **File Formats:** DOCX, PDF, EPUB, TXT, Markdown, JSON

## Core Features
- **Multi-Project Management:** Create, load, and delete projects with full state persistence
- **Real-Time Text Analysis:** Continuous metrics calculation including word count, readability, and complexity
- **Advanced Grammar & Readability:** Integrated grammar checking, repeated word detection, and readability scoring
- **Version Control & Change Tracking:** Comprehensive undo/redo system with detailed change history for managing drafts
- **Settings Persistence:** Dot-notation configuration system with nested section access and JSON storage
- **Comprehensive Export:** Multi-format export supporting TXT, Markdown, DOCX, PDF, EPUB, and JSON
- **Performance Monitoring:** Real-time CPU, memory, and disk usage tracking with threshold alerts
- **API Integration:** Support for OpenAI, Anthropic, Claude, and Google APIs with intelligent caching and rate limiting
- **Cost Estimation:** Automatic calculation of API usage costs and budget tracking
- **Responsive Status Bar:** Real-time display of connection status, resource usage, and application state
- **Theme System:** Light and dark mode support with customizable color schemes
- **Automated Workflows:** 11-step writing process with progress tracking and recovery
- **Writing Analytics:** Session tracking, word count goals, productivity insights, and historical analysis
- **Database System:** SQLite backend with connection pooling, query caching, and automatic optimization
- **Error Handling:** Comprehensive error logging, user-friendly error dialogs, and graceful degradation
- **Accessibility:** Full keyboard navigation and screen reader support for inclusive writing experience

---

# Getting Started

## First-Time Setup

Welcome to AAWT! Here's what you'll see and do when you first launch the application:

### Initial Launch

1. **Welcome Screen:** On first launch, AAWT displays a welcome screen introducing the main features
2. **Quick Setup Wizard:**
   - Select your preferred theme (Light, Dark, or System default)
   - Configure basic writing preferences (font, autosave interval)
   - Optionally enter API keys for AI assistance (can be done later)

### Creating Your First Project

1. **Click "New Project"** or press `Ctrl+N`
2. **Enter Project Details:**
   - **Project Name:** Give your project a unique name
   - **Genre:** Select the genre (Fantasy, Science Fiction, Mystery, etc.)
   - **Target Word Count:** Set your goal (optional)
   - **Target Audience:** Choose your intended readership
   - **Writing Style:** Select tone and point of view preferences
3. **Start Writing:** Begin typing in the main editor—your work is auto-saved every 30-60 seconds

### Understanding the Interface

**Main Areas:**
- **Sidebar (Left):** Navigation buttons to access different views (Dashboard, Projects, Analytics, Settings, etc.)
- **Content Area (Right):** Main workspace displaying the current view or editor
- **Status Bar (Bottom):** Real-time metrics including word count, connection status, and performance indicators

**Key Views to Explore:**
- **Dashboard:** Overview of your current project, progress toward goals, and recent activity
- **Writing Editor:** Main text editing area with real-time word count and readability feedback
- **Analytics:** Detailed statistics about your writing sessions and quality metrics
- **Settings:** Customize the application to match your preferences

### Quick Tips for New Users

- Press `F1` at any time to access context-sensitive help
- All features are accessible via keyboard shortcuts (see [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference))
- Your work is automatically saved—look for the green checkmark in the status bar
- Use the Text Analysis tools to get immediate feedback on readability and style
- Explore the Export menu when you're ready to share your work

---

# Core Architecture

## Entry Point
**File:** `aawt.py`
- Main application entry point
- Initializes PyQt5 application
- Loads configuration and database
- Manages window lifecycle
- Integrates all subsystems

## Directory Structure
```
AAWT/
├── src/
│   ├── ui/
│   │   ├── main_gui.py           # Main GUI (Graphical User Interface) implementation (8,700+ lines)
│   │   ├── main_window.py        # Main window container
│   │   ├── core_ui.py            # Core UI components
│   │   ├── enhanced_analytics.py # Analytics dashboard
│   │   ├── enhanced_settings.py  # Settings panel
│   │   ├── export_ui.py          # Export interface
│   │   ├── project_selector_dialog.py  # Project selection
│   │   └── automated_novel_gui.py      # Novel automation
│   ├── system/
│   │   ├── api_manager.py        # API integration (1,200+ lines)
│   │   ├── text_analyzers.py     # Grammar & readability
│   │   ├── export_manager.py     # Export functionality
│   │   ├── settings_manager.py   # Settings persistence
│   │   ├── file_operations.py    # File I/O
│   │   └── memory_manager.py     # Cache management
│   ├── database/
│   │   ├── database_manager.py   # Database operations
│   │   └── connection_pool.py    # Connection pooling
│   ├── text/
│   │   └── text_processing.py    # Text analysis
│   └── config/
│       └── global_config.py      # Global configuration
├── config/                       # Configuration files
│   ├── app_config.json
│   ├── user_settings.json
│   └── default_config.json
├── exports/                      # Export output directory
├── projects/                     # Project storage
├── tests/                        # Test files
└── docs/                         # Documentation
```

## Component Interaction Model
```
Main Application (aawt.py)
│
├─→ Database Manager (Connection Pooling, Migrations)
│
├─→ Settings Manager (Persistent Configuration)
│
├─→ API Manager (OpenAI, Anthropic, Google APIs)
│   ├─→ SQLite Cache (LZ4 Compression)
│   ├─→ Rate Limiter (Request Throttling)
│   └─→ Text Analyzers (Grammar, Readability)
│
├─→ Export Manager (6 Format Export)
│
├─→ GUI System (PyQt5)
│   ├─→ Main Window
│   ├─→ Navigation System
│   ├─→ Analytics Dashboard
│   ├─→ Settings Panel
│   └─→ Export Interface
│
└─→ Performance Monitor (CPU, Memory, Disk)
```

---

# User Interface Components

## Main Window Architecture

### Window Dimensions & Layout
- **Default Size:** 1280x800 pixels (configurable)
- **Layout Type:** Modern responsive design with split areas
- **Theme Support:** Light/Dark mode with custom color schemes
- **Resizable:** Fully resizable with minimum constraints

### Layout Structure
The main GUI uses a proportional split layout:
- **Sidebar:** 1/4 width (left), navigation buttons and project info
- **Main Content:** 3/4 width (right), stacked widget with multiple views
- **Status Bar:** Bottom, shows real-time metrics

### Sidebar Navigation

#### Navigation Button Categories (15 total)
1. **Dashboard** - Overview and metrics
2. **Projects** - Project management interface
3. **Workflow** - Workflow management and control
4. **Project Management** - Advanced project operations
5. **Settings** - Application configuration
6. **Help** - Documentation and support
7. **Performance** - Performance monitoring
8. **System Health** - System resource monitoring
9. **File Operations** - File I/O operations
10. **Writing Tools** - Text analysis and writing aids
11. **Analytics** - Advanced statistics and reports
12. **Export** - Export functionality interface
13. **Cache/Rate** - Cache management and rate limiting
14. **Optimization** - System optimization tools
15. **Advanced** - Advanced features and options

#### Button Styling
- Active button: Highlighted with primary color (#2196F3)
- Inactive button: Gray (#666)
- Hover state: Darker shade with transition animation
- Text: 12pt Arial, white on colored background
- Padding: 10px vertical, 15px horizontal

### Main Content Area (Stacked Widget)

#### Dashboard View
**Purpose:** Provides project overview and key metrics

**Components:**
- **Progress Bar:** 0-100% visual progress indicator
- **Word Count Display:** Current and target word counts
- **Chapter Counter:** Total chapters/sections
- **Mood Meter:** Story emotional tone indicator
- **Pacing Indicator:** Story pacing visualization
- **Recent Activity List:** Last 10 actions performed
- **Metrics Charts:** Visual representation of progress over time

**Metrics Displayed:**
- Total word count vs. goal
- Average daily progress
- Reading time estimation
- Completion percentage
- Project trend graph

#### Projects View
**Purpose:** Manage multiple writing projects

**Features:**
- **Project List:** Scrollable list of all projects
- **Quick Create:** Create new project button
- **Project Info Display:** Show selected project details
- **Load/Switch Project:** Load existing project
- **Delete Project:** Remove project (with confirmation)
- **Recent Projects:** Quick access to recently used projects

**Project Properties Shown:**
- Project name
- Creation date
- Last modified date
- Word count
- Target words
- Current status (active/paused/completed)

#### Workflow View
**Purpose:** Control and monitor automated workflow

**Components:**
- **Workflow Controls:** Start, Pause, Stop, Resume buttons
- **Steps Display:** Show current and completed steps
- **Progress Tracking:** Visual step progress
- **Status Indicator:** Current workflow state
- **Log Viewer:** Real-time workflow logs

**Workflow Features:**
- 11-step automated writing process
- Step completion verification
- Progress persistence
- Error recovery
- Workflow history

#### Analytics View (Enhanced)
**Purpose:** Comprehensive statistics and analysis

**Tabs:**
1. **Dashboard Tab**
   - Project statistics summary
   - Key metrics overview
   - Quick action buttons
   - Recent activities

2. **Text Analysis Tab**
   - Word/character/sentence counts
   - Readability metrics
   - Complexity scoring
   - Repeated words detection

3. **Performance Tab**
   - API usage statistics
   - Cache hit rates
   - Database performance
   - Memory usage trends

4. **Session Stats Tab**
   - Writing session duration
   - Words written per session
   - Average typing speed
   - Break frequency

5. **Reports Tab**
   - Generate detailed reports
   - Export analytics
   - Custom metric queries
   - Historical data

#### Settings View (Enhanced)
**Purpose:** Comprehensive application configuration

**Tabs:**
1. **General Tab**
   - Application name
   - Default project directory
   - Autosave interval (30-3600 seconds)
   - Font selection and size

2. **Themes Tab**
   - Light/Dark/System mode
   - Primary color (#RRGGBB)
   - Secondary color
   - Text color
   - Background color
   - Theme preview

3. **Writing Tab**
   - Default tone (Formal, Professional, Conversational, Creative, Academic)
   - Default POV (First, Second, Third Limited, Omniscient)
   - Enable spell check
   - Enable grammar check
   - Highlight repeated words

4. **API Tab**
   - OpenAI API key input
   - Anthropic API key input
   - Google API key input
   - HuggingFace API key input
   - Test connection buttons
   - API status indicators

5. **Export Tab**
   - Default export directory
   - Default export format
   - Include metadata option
   - Include statistics option
   - Compress output option
   - Format checkboxes (TXT, MD, DOCX, PDF, EPUB, JSON)

6. **Performance Tab**
   - Cache size (MB)
   - Analytics update interval (1-60 seconds)
   - Database optimization frequency
   - Connection pool size
   - Query timeout (milliseconds)

7. **Advanced Tab**
   - Debug mode toggle
   - Logging level (DEBUG, INFO, WARNING, ERROR)
   - Enable query cache
   - Enable connection pooling
   - Database path
   - Reset to defaults button

#### Help View
**Purpose:** User documentation and support

**Sections:**
- **Getting Started:** Initial setup guide
- **Features:** Overview of all features
- **Workflow Steps:** 11-step process documentation
- **Text Tools:** How to use text analysis tools
- **Export Guide:** Export format guide
- **API Setup:** API key configuration help
- **Troubleshooting:** Common issues and solutions

### Status Bar

**Components (Left to Right):**
1. **Status Message Label:** Current application status
2. **Progress Bar:** Operation progress (hidden when not in use)
3. **Connection Status:** Online/Offline indicator with green/red dot
4. **Performance Metrics:** CPU and Memory usage display

**Status Messages:**
- "Ready" - Application idle
- "Loading project..." - Project loading
- "Exporting..." - Export in progress
- "Analyzing text..." - Analysis running
- "Error: [message]" - Error state
- "[Project Name] loaded" - Project status

**Performance Metrics Format:**
`CPU: 0% | Memory: 0MB`
- Updates display every 1-2 seconds
- Shows real-time system resource usage
- Changes color based on load: Green (<50%), Yellow (50-80%), Red (>80%)

### Menu Bar

**File Menu:**
- New Project
- Open Project
- Save Project
- Export Project (submenu: TXT, DOCX, PDF, EPUB, JSON)
- Recent Projects (dynamic submenu)
- Settings
- Exit Application

**View Menu:**
- Toggle Dark Mode
- Zoom In (Ctrl++)
- Zoom Out (Ctrl+-)
- Reset Zoom (Ctrl+0)
- Fullscreen (F11)
- Show/Hide Sidebar

**Tools Menu:**
- Text Analysis
- Grammar Check
- Readability Analyzer
- Export Manager
- Project Templates
- Backup Manager

**Help Menu:**
- View Documentation
- API Setup Guide
- Keyboard Shortcuts
- About AAWT
- Check for Updates
- Report Issue

---

# Text Analysis & Writing Tools

## Text Processing Engine

### TextAnalyzer Class
**Location:** `src/text/text_processing.py`

**Core Methods:**
```python
analyze_text(text: str) -> Dict[str, Any]
  - word_count: int
  - character_count: int
  - sentence_count: int
  - paragraph_count: int
  - average_words_per_sentence: float
  - average_characters_per_word: float
  - unique_words: int
  - readability_score: float (0-100)
  - complexity_level: str (Simple, Moderate, Complex)
  - repeated_words: List[Tuple[str, int]]
  - long_sentences: List[str]
  - readability_grade_level: str (1-16+)
```

**Performance Metrics:**
- Processes 10,000 word documents in <100ms
- Memory usage: ~2-5MB per analysis
- Cached results for repeated texts
- Thread-safe operations

## Grammar Analysis Tool

### Vocabulary Analysis System

The grammar analyzer provides comprehensive vocabulary assessment through multiple channels. It extracts all meaningful words from user text and analyzes each word for several characteristics. The system maintains a sophisticated vocabulary database that grows as users interact with the application.

**Word Analysis Capabilities:**
- Extraction of meaningful words (excluding common stop words like "the", "and", "is")
- Identification of complex vocabulary (words with 3+ syllables or rare usage)
- Synonyms retrieval from external vocabulary APIs or internal dictionaries
- Part-of-speech tagging to understand word function
- Definition lookup for complex terms
- Vocabulary difficulty scoring for reader comprehension assessment

**Complex Word Identification:**
The system identifies words that might be difficult for the target audience by analyzing:
- Syllable count (words with more syllables are generally harder)
- Frequency in standard English corpora (rare words are more difficult)
- Technical terminology classification
- Academic or specialized vocabulary indicators
- Length (character count) as an indicator of complexity

**Repeated Word Detection:**
The analyzer tracks all word frequencies throughout the text and flags problematic repetition. When a word appears too frequently within a reasonable section (such as every 100-200 words or 3+ times in a paragraph), it's flagged for user attention. The system suggests synonyms or alternative phrasings to increase linguistic variety. The detection includes both exact matches and variations of the same word stem.

### Grammar Structure Analysis

**Sentence-Level Checking:**
The grammar analyzer processes each sentence independently to identify structural issues. For every sentence, it evaluates:
- Length (word count) to detect run-on or fragmentary sentences
- Punctuation correctness and consistency
- Subject-verb agreement patterns
- Proper clause structure and construction
- Pronoun-antecedent relationships

**Common Grammar Issues Detected:**
- Sentence fragments (incomplete sentences without main verbs)
- Run-on sentences exceeding recommended length (typically >30 words)
- Subject-verb disagreement patterns
- Tense inconsistencies within sentences
- Improper comma usage and splice errors
- Incorrect pronoun references or ambiguous antecedents
- Misplaced or dangling modifiers
- Parallel structure violations in lists or series

**Style Issues Flagged:**
- Passive voice overuse when active voice would be clearer
- Clichéd or overused phrases common in the genre
- Weak verbs that could be replaced with stronger alternatives
- Redundant words or phrases that repeat meaning
- Vague language that lacks specificity
- Inconsistent tone shifts within related passages

### API Integration for Enhanced Analysis

The grammar analyzer connects to the Words API through RapidAPI to access comprehensive vocabulary information. The API provides:
- Definition retrieval with multiple meanings and contexts
- Part-of-speech information for word classification
- Synonym suggestions ranked by similarity and usage frequency
- Antonym identification for alternative expressions
- Example sentences showing proper usage
- Related words and word family connections

**API Fallback Strategy:**
When the Words API is unavailable or rate limits are reached, the system automatically falls back to local algorithms. The fallback uses built-in dictionaries and heuristic rules to provide basic analysis. This ensures the application remains functional even without API connectivity. The system caches all API responses locally to minimize API calls and improve performance.

**Caching System:**
The system caches API responses with a 24-hour expiration. When the same analysis is requested, the system retrieves the cached result rather than making a new API call. This significantly reduces both API costs and user wait time. The system stores the cache in a local database and automatically cleans expired entries.

## Readability Analysis Tool

### Readability Scoring System

The readability analyzer measures how easy or difficult text is to read and understand. It produces several complementary metrics that describe different aspects of readability.

**Flesch Reading Ease Score (0-100 scale):**
- Scores above 90 indicate very easy, elementary-level reading (appropriate for grades 1-6)
- Scores between 80-89 indicate easy reading with clear communication (grades 7-9)
- Scores between 70-79 indicate fairly easy reading that most readers follow easily (grades 10-12)
- Scores between 60-69 indicate standard reading difficulty for general audiences (college level)
- Scores between 50-59 indicate fairly difficult reading requiring attention and concentration
- Scores between 30-49 indicate difficult reading aimed at educated readers only
- Scores below 30 indicate very difficult, highly technical or complex reading

**Grade Level Equivalents:**
The system converts readability metrics into U.S. grade level equivalents. A readability score of 70 equates to a 10th-grade reading level, meaning the text requires the comprehension skills of a typical 10th grader. Grade levels range from 1 (easiest) through 16+ (most difficult). This provides an intuitive way to understand the text difficulty relative to educational levels.

**Reading Time Estimation:**
Based on average reading speed (approximately 200-250 words per minute for adults), the system estimates how long it will take to read the full text. Reading time varies based on text complexity—difficult texts are read more slowly than easy texts. The system adjusts its estimate based on the readability score.

### Syllable and Complexity Analysis

**Syllable Counting Algorithm:**
The system estimates syllable count for each word using heuristic rules and pattern matching. While not 100% accurate (no perfect algorithm exists without pronunciation data), the estimates are reliable enough for readability scoring. The algorithm:
- Counts vowel groups (consecutive vowels count as one syllable)
- Applies corrections for common patterns (silent e's, special endings)
- Handles exceptions common in English
- Recognizes prefixes and suffixes that affect syllable count

**Complexity Metrics:**
- Average syllables per word (higher averages indicate more complex vocabulary)
- Percentage of complex words (3+ syllables) in the text
- Sentence length variation (variety is good; repetitive patterns are monotonous)
- Paragraph length and structure (very long paragraphs are harder to follow)
- Vocabulary diversity (unique word count vs. total word count)

### Internal Fallback Calculation

When external APIs are unavailable, the analyzer uses the Flesch-Kincaid readability formula based on:
- Total word count from the entire text
- Total syllable count calculated by the local algorithm
- Total sentence count determined by punctuation analysis

The calculation produces the same score ranges and grade levels as the API, ensuring consistency regardless of data source. This fallback mechanism guarantees the application provides readability feedback even without internet connectivity.

### External API Integration

The readability analyzer optionally connects to the ApyHub API for advanced analysis. This service provides:
- More accurate readability calculations based on linguistic analysis
- Advanced metrics including complexity scoring beyond basic readability
- Reading difficulty classification
- Audience suitability recommendations
- Detailed breakdown by sentence and paragraph

**API Response Handling:**
When the API returns results, the system validates the response and uses the provided scores. If the API fails or returns invalid data, the system immediately falls back to local calculation. The system logs all API interactions for debugging and optimization purposes.

**Language Support:**
The analyzer can handle multiple languages including English, Spanish, French, German, and others. Language detection is automatic based on the text, though users can override this. Readability formulas are adapted for each language to account for linguistic differences.

## Integrated Text Tools Widgets

### Text Analysis Widget Architecture

**Purpose and Integration:**
The text analysis widget is a standalone component within the main writing interface that provides real-time text metrics. It's designed to give writers immediate feedback about their writing statistics without requiring manual action.

**Input Mechanism:**
Users can either paste text into the widget's text area or use a button to analyze the currently edited content from the main editor. The widget automatically processes the input and displays results without leaving the application.

**Metrics Calculated and Displayed:**
- **Word Count:** Total number of words in the text
- **Character Count:** Total characters including spaces, and separately excluding spaces
- **Sentence Count:** Total number of sentences (determined by terminal punctuation)
- **Paragraph Count:** Number of paragraphs (determined by line breaks)
- **Average Words Per Sentence:** Mean number of words per sentence (indicator of sentence complexity)
- **Average Characters Per Word:** Mean character count per word (vocabulary complexity indicator)
- **Unique Words Count:** Number of distinct words (vocabulary diversity)
- **Readability Score:** 0-100 scale indicating text difficulty
- **Complexity Level:** Classification as Simple, Moderate, or Complex
- **Repeated Words List:** Words appearing too frequently with their counts
- **Long Sentences List:** Sentences exceeding the recommended length with line numbers
- **Grammar Issues:** Summary of detected grammar problems

**Performance Characteristics:**
- Processes large documents (10,000+ words) in under 100 milliseconds
- Uses approximately 2-5MB of memory per analysis
- Results are cached to avoid redundant calculations
- Updates are debounced (minimum 500ms between updates) to prevent overwhelming the display
- Thread-safe operations allow analysis without blocking UI

**User Interaction Flow:**
Users can click the "Analyze" button to run analysis. A progress indicator shows during processing. Results appear in a scrollable results area with color-coding (green for good, yellow for warnings, red for issues). Users can click on individual results to jump to problematic sections in the editor.

### Grammar Check Widget

**Functionality Overview:**
The grammar check widget performs comprehensive grammar analysis and presents findings in an organized format. It uses the integrated grammar analyzer to identify issues across multiple categories.

**Issue Categories Displayed:**
- **Repeated Words Section:** Shows each word that appears too frequently with its exact count in the text
- **Long Sentences Section:** Lists sentences exceeding the recommended length threshold (typically 20 words) along with word count and location
- **Sentence Structure Issues:** Grammar patterns that violate standard English conventions
- **Style Issues:** Recommendations for improving writing style and clarity
- **Readability Score:** Overall readability assessment with grade level equivalent

**Output Format and Presentation:**
Results are organized hierarchically with section headers, indented lists, and severity indicators. Each issue type can be expanded or collapsed. Severity is indicated with visual icons (✓ for good, ⚠️ for warnings). Users can click "Details" buttons to see additional information about each issue.

**Suggestions and Alternatives:**
For repeated words, the widget displays synonym suggestions retrieved from the vocabulary analysis. Users see the original word, frequency count, and suggested alternatives. Clicking a suggestion shows where that word is used in the text.

**API Integration:**
The widget automatically uses the Words API if available and an API key is configured. It queries the API for advanced word suggestions and definitions. Without API access, the widget uses fallback suggestions from local dictionaries. The widget indicates whether it's using API-backed or local suggestions.

**Interactive Features:**
- Users can mark issues as "reviewed" without changing them
- Custom ignore lists can be created for words the user doesn't want flagged
- Suggestions can be applied to replace all instances or one at a time
- History of previous checks is maintained for comparison
- Export function to save grammar check results

### Style Analysis Widget

**Configuration Interface:**
Before analyzing style, users select several parameters that define their target writing style:

**Tone Selection (5 Primary Options):**
- **Formal Tone:** Academic, professional, legal, or technical writing with sophisticated vocabulary, complex sentences, and objective perspective
- **Professional Tone:** Business, corporate, or official communication with clear structure, polite language, and results-focused phrasing
- **Conversational Tone:** Friendly, accessible writing that uses contractions, casual vocabulary, and direct address to readers
- **Creative Tone:** Imaginative, expressive writing with literary devices, varied sentence structures, and emotional resonance
- **Academic Tone:** Educational writing with proper citations, technical terminology, evidence-based arguments, and structured presentation

**Genre Selection (8 Primary Options):**
- **Fiction:** General narrative with story structure, character development, and plot progression
- **Fantasy:** World-building elements, magic systems, mythical creatures, and adventure themes
- **Science Fiction:** Futuristic technology, space exploration, alternative realities, and scientific concepts
- **Mystery:** Suspenseful narrative with clues, red herrings, investigations, and reveals
- **Romance:** Relationship-focused narrative with emotional development, tension, and personal connection
- **Horror:** Dark, scary elements with suspense, psychological tension, and disturbing imagery
- **Non-Fiction:** Factual, informative writing with research, citations, and objective perspective
- **Adventure:** Action-packed narrative with danger, quests, discovery, and exciting scenarios

**Point of View Selection (4 Primary Options):**
- **First Person:** "I/we" narrative from protagonist's perspective with internal thoughts and limited external knowledge
- **Second Person:** "You" narrative directly addressing the reader (uncommon but used in interactive fiction)
- **Third Person Limited:** "He/she/they" narrative from single character's perspective with limited omniscience
- **Third Person Omniscient:** "He/she/they" narrative with all-knowing narrator revealing multiple perspectives

**Analysis Process:**
After users configure their preferences, the widget analyzes the text against these parameters. It examines vocabulary choices, sentence structures, narrative voice, and thematic elements to determine if they align with the selected style.

**Specific Checks Performed:**
- **Tone Consistency:** Verifies vocabulary matches the selected tone (formal vs. casual, objective vs. emotional)
- **Vocabulary Alignment:** Checks that word choices are appropriate for the genre and tone
- **Sentence Structure:** Analyzes sentence complexity and variety relative to the tone
- **Perspective Consistency:** Verifies the narrative maintains the selected POV without unexpected shifts
- **Genre Appropriateness:** Checks for genre-specific elements and conventions
- **Theme Consistency:** Verifies thematic elements support the selected genre

**Recommendations Generated:**
The widget provides specific suggestions including:
- Alternative phrasings that better match the selected tone
- Vocabulary suggestions that align with the genre and tone
- Structural recommendations for sentences or paragraphs
- Example sentences showing the recommended style
- Explanations of why changes would improve the writing

### Consistency Check Widget

**Consistency Verification System:**
The consistency check widget identifies variations and inconsistencies throughout the text that should be standardized. It scans the entire document for patterns and deviations.

**Specific Consistency Checks:**

**Character Name Consistency:**
Detects all character mentions and identifies spelling variations. If a character is referred to as both "Elara" and "Elera," the system flags this. It shows all variants and their frequencies, allowing users to standardize to a single spelling.

**Place Name Spelling:**
Tracks all location names and identifies spelling inconsistencies. Detects when a place is spelled as both "Westmarch" and "West March" and flags for correction.

**Terminology Standardization:**
Identifies technical terms, magical concepts, or special vocabulary and ensures they're used consistently. Detects if a magical system is called both "The Arcane" and "Arcane Magic."

**Capitalization Consistency:**
Verifies that titles, proper nouns, and special terms maintain consistent capitalization. Flags if "the King" appears in some places and "the king" in others (unless stylistically intentional).

**Verb Tense Consistency:**
Analyzes the narrative's primary tense (past, present, or conditional) and detects sudden switches. Identifies if the story is primarily in past tense but a single paragraph switches to present tense.

**Punctuation Pattern Analysis:**
Examines punctuation usage to ensure consistency. For example, if dialog uses single quotation marks in some sections and double quotation marks in others, this is flagged. Also checks dash usage (em dash vs. hyphen vs. en dash).

**Output and Recommendations:**
For each consistency type, the widget shows:
- All variants or inconsistencies found
- Frequency count for each variant
- Line numbers or context showing where each variant appears
- Suggested standardization (typically the most frequently used variant)
- One-click correction to standardize all instances or select specific changes

### Readability Analysis Widget

**Audience Selection and Configuration:**
Before analysis, users select their target audience, which affects readability assessment:
- **General (Grades 8-12):** For general readers and most commercial fiction
- **Academic (College Level):** For college students and educated readers
- **Professional (Adult Technical):** For business and technical readers
- **Children (Grades 4-6):** For children's literature
- **Young Adults (Grades 6-8):** For young adult fiction and teen readers

**Comprehensive Analysis Process:**
Once configured, the widget analyzes the text and generates a detailed readability assessment including:

**Core Metrics Displayed:**
- Flesch Reading Ease score on a 0-100 scale
- Grade level equivalent (e.g., "10th Grade")
- Estimated reading time in minutes
- Percentage of complex words (3+ syllables)
- Average sentence length in words
- Average word length in characters
- Total syllable count in the text

**Audience Suitability Assessment:**
The widget compares the calculated readability metrics against the selected audience's typical reading level. It provides:
- Clear indication of suitability ("✓ Suitable for this audience" or "✗ Too difficult" or "✗ Too easy")
- Comparison to target audience reading level
- Visual gauge showing difficulty relative to audience
- Color-coded indicators (green for suitable, yellow for marginal, red for unsuitable)

**Detailed Feedback and Recommendations:**
- Specific sections that are too difficult or too easy
- Vocabulary recommendations (simplify complex words, add variety, etc.)
- Sentence structure suggestions (break up long sentences, combine short ones, etc.)
- Paragraph organization tips
- Example phrasings showing recommended improvements
- Estimated impact of suggested changes on readability

**Interactive Elements:**
- Users can apply readability improvements incrementally
- Before/after readability comparison showing improvement
- Detailed breakdown showing which factors most affect readability
- Historical tracking of readability score changes across editing sessions



---

# Database System

## Overview

The database system is the backbone of AAWT, providing persistent storage for all application data, project information, writing sessions, API usage, and analytics. It uses SQLite with connection pooling for concurrent access, fast queries, and reliable data integrity.

## Key Features

**Performance Optimization:**
- **Connection Pooling:** Maintains 5 reusable connections (configurable) to minimize connection overhead
- **Query Caching:** Caches frequently-run queries with 70%+ cache hit rates
- **Smart Indexing:** Uses appropriate indexes for fast lookups and joins
- **Write-Ahead Logging:** Improves concurrent access performance

**Data Storage:**
- **Projects:** Stores all project metadata, settings, and content references
- **Writing Sessions:** Tracks every writing session for analytics
- **API Usage:** Logs all API calls for cost tracking and monitoring
- **Content Cache:** Stores analysis results to avoid redundant processing
- **Change History:** Records all modifications for undo/redo functionality

**Data Integrity:**
- **Transaction Management:** All multi-step operations are atomic
- **Foreign Key Constraints:** Enforces referential integrity across tables
- **Data Validation:** All input is validated before storage
- **Automatic Backups:** Regular automated backups prevent data loss

## Database Operations

**Common Operations:**
- **Loading Projects:** Retrieves project metadata, session history, and cached metrics in optimized queries
- **Tracking API Usage:** Logs every API call with timing, cost, and success status
- **Caching Analysis:** Stores text analysis results for instant retrieval
- **Historical Queries:** Aggregates data for statistics, trends, and reporting

**Maintenance:**
- Automatic cache cleanup (removes entries older than 7 days)
- Session data retention (keeps last 90 days)
- Weekly database optimization (ANALYZE and VACUUM)
- Integrity checks and repairs

For detailed schema information, see the [Technical Reference](#technical-reference) section.

---

# API Integration & Caching

## API Manager System Overview

The API manager is the central hub for all external artificial intelligence API interactions. It provides a unified interface to multiple AI services while managing rate limits, caching, costs, and error handling transparently. This abstraction allows the application to switch between providers or use multiple providers simultaneously without changing UI or business logic.

## Multi-API Support Architecture

### Supported API Providers

**OpenAI (ChatGPT family):**
The application supports multiple OpenAI models with varying capabilities and costs. GPT-3.5-turbo is fast and economical, suitable for general writing assistance. GPT-4 is more powerful and better at complex tasks, though slower and more expensive. GPT-4-turbo offers a middle ground with advanced capabilities at moderate costs.

**Anthropic (Claude family):**
Three Claude models are available in different sizes. Claude-3 Opus is the most powerful for complex reasoning. Claude-3 Sonnet provides good balance between capability and speed. Claude-3 Haiku is the fastest and cheapest option. All models can be used interchangeably through the API manager.

**Google (Generative AI):**
Google's text and Gemini models provide an alternative AI source. These models have different capability profiles and pricing structures, allowing users to choose based on their needs.

**HuggingFace (Open Source Models):**
The system can access open-source models hosted on HuggingFace or self-hosted. This provides a privacy-focused option where model access doesn't go through third-party servers.

### Request Handling Pipeline

When a user requests AI assistance (text continuation, suggestions, analysis), the system follows a standardized pipeline:

**Step 1: Request Validation**
The request is validated for completeness. Required parameters like the prompt are checked. The selected API is verified to be configured with an API key. The project context is validated for consistency.

**Step 2: Rate Limit Check**
The system checks if the rate limit for this API allows a new request. If limits are exceeded, the request is either queued or rejected with a message to the user. Limits are per API and per time window (usually per hour).

**Step 3: Cache Lookup**
A cache key is generated from the request (typically a hash of the prompt and parameters). The system checks if this exact request has been made before and if the cached result is still valid. If a cache hit occurs, the cached response is returned immediately without API call.

**Step 4: Context Enhancement**
If not cached, the system gathers context about the current project to include in the API request. This includes the project's genre, style, target audience, character list, and recent content. This context helps the AI provide more relevant responses.

**Step 5: API Request Execution**
The enhanced request is formatted according to the selected API's requirements and sent via HTTP. The system includes authentication headers with the API key. Request timeout is enforced to prevent hanging indefinitely.

**Step 6: Response Parsing**
The API response is parsed and validated. The system extracts the generated text and any metadata. Error responses are detected and reported to the user.

**Step 7: Cache Storage**
The system stores successful responses in the cache with a timestamp and expiration time. The system calculates cost based on token usage and logs the API call to the database.

**Step 8: User Presentation**
The response is presented to the user in the UI, typically in a suggestion dialog. The user can accept, reject, edit, or request regeneration.

## Rate Limiting System

### Per-API Rate Limits

Each API provider has limits on how many requests can be made in a time window:
- **OpenAI:** Typically 3000 requests per minute (varies by subscription tier)
- **Anthropic:** Typically 1000 requests per minute
- **Google:** Typically 60 requests per minute (more restrictive)
- **HuggingFace:** Typically 1000 requests per hour

**Rate Limit Enforcement:**
The system tracks the number of requests made to each API within the current time window. When approaching a limit, users are warned. When a limit is exceeded, requests are rejected with a message explaining when they can try again.

**Request Queuing:**
Rather than immediately rejecting requests that would exceed limits, the system can queue them. When the time window resets, queued requests are processed. This provides a better user experience by automatically handling requests instead of requiring the user to retry.

**Rate Limit Detection and Adaptation:**
When an API returns a rate limit error response, the system detects this and automatically reduces its request rate. For the next several requests, it waits longer between submissions. This prevents cascading failures where the system keeps hitting the same rate limit repeatedly.

## SQLite Caching System

### Cache Storage Mechanism

Responses from API calls are stored in SQLite for fast retrieval. Each cache entry includes the request parameters (as a hash key), the response data, a timestamp, and an expiration time. When the same request is made again, the system checks the cache first.

**Cache Keys:**
Cache keys are generated by hashing the request prompt and important parameters. Identical requests generate identical keys. Different prompts or parameters generate different keys. This ensures cache hits only occur when the exact request is made again.

**Data Storage:**
Response data is stored as JSON text (or optionally compressed with LZ4). Smaller responses are stored uncompressed for faster access. Larger responses are automatically compressed to save storage space.

**Expiration Management:**
Each cache entry has an expiration time (default 7 days from creation). When retrieving from cache, the system checks if the entry has expired. Expired entries are ignored and fresh queries execute. Old cache entries are periodically deleted during maintenance operations.

**Cache Statistics:**
The system maintains statistics about cache performance:
- Total entries in cache
- Total cache size (MB)
- Cache hit rate (percentage of requests served from cache)
- Average compression ratio for compressed entries
- Most frequently cached queries

### LZ4 Compression Support

When the LZ4 compression library is available, large cached responses are automatically compressed. This reduces storage requirements by 70-90% for typical JSON responses.

**Compression Benefits:**
- Reduced database file size saves disk space
- Smaller file size allows more cache entries to fit in memory
- Faster SQLite operations with smaller data
- More efficient disk I/O when reading/writing cache

**Transparent Compression:**
Compression is transparent to the application. The cache layer automatically compresses when storing and decompresses when retrieving. If LZ4 is unavailable, caching still works with uncompressed data.

**Performance Trade-off:**
Compression adds slight overhead during storage and retrieval. For small responses (<1KB), uncompressed storage is faster. For large responses (>10KB), compression overhead is recovered through faster I/O. The system uses heuristics to choose whether to compress each entry.

### Memory Caching Layer

In addition to SQLite, frequently-accessed cache entries are kept in memory for even faster access. This two-tier cache system (memory + disk) provides excellent performance without consuming too much RAM.

**In-Memory Cache:**
The most recently used cache entries are kept in RAM. When a cache entry is accessed, it's promoted to the memory cache. The memory cache has a size limit (e.g., 100MB). When the limit is exceeded, least-recently-used entries are evicted.

**Eviction Policy:**
When new entries arrive and the memory cache is full, the least-recently-used entry is removed first. This prioritizes keeping frequently-accessed data in memory.

## Cost Estimation and Tracking

### Pricing Database

The system maintains a comprehensive pricing database for all supported models. Pricing is stored as cost per 1000 tokens for input and output separately. For example, GPT-4 costs $0.03 per 1000 input tokens and $0.06 per 1000 output tokens.

**Dynamic Pricing Updates:**
API prices change periodically as providers adjust pricing. The system's pricing database should be updated to reflect current prices. This can be done through manual configuration or automatic updates via a pricing service.

**Provider-Specific Pricing:**
Different providers have different pricing structures. Some charge differently based on model size, others charge based on input vs. output tokens. The system accounts for these variations in its cost calculation.

### Cost Calculation

When an API call completes, the system calculates its cost:
- Input tokens used times input cost per token
- Output tokens used times output cost per token
- Sum of input and output costs

This cost is stored in the database alongside the API call record.

### Cost Analysis and Reporting

Users can view comprehensive cost analysis:
- **Total spending:** Overall API spending for a time period
- **Cost by API:** How much spent with each provider
- **Cost by model:** How much each model cost
- **Cost trends:** Spending over time (daily, weekly, monthly)
- **Cost estimates:** Projected spending if current usage continues

This helps users understand their API costs and potentially adjust usage patterns to save money.

### Budget Alerts

The system can optionally alert users when spending exceeds configurable thresholds:
- Daily limit (e.g., "alert when daily spending exceeds $10")
- Weekly limit (e.g., "alert when weekly spending exceeds $50")
- Monthly limit (e.g., "alert when monthly spending exceeds $200")

When a limit is about to be exceeded, the system warns the user. Optionally, it can prevent further API calls until the user confirms they want to continue.

## Project Context Enhancement

### Context Gathering

When making API requests, the system gathers relevant context about the current project to include in the request. This helps AI provide more appropriate and consistent responses.

**Project Metadata Context:**
- Project name and genre
- Target audience demographics
- Writing style and tone preferences
- Themes and central conflicts
- Main character names and brief descriptions
- Setting details and world-building elements

**Current Content Context:**
- The last 500-1000 characters of current text (recent writing)
- Character list and relationships
- Plot outline or summary
- Completed chapters or sections

**Request-Specific Context:**
- What user is currently asking for (continuation, dialogue, description, etc.)
- User's current writing section or chapter
- Any special instructions from the user

### Context Integration into Prompts

The gathered context is synthesized into a system prompt or context block that precedes the user's actual request. This context frame helps the AI understand the story world and maintain consistency.

**Context Block Structure:**
The context is organized hierarchically with clear sections for each information type. This makes it easy for the AI to locate relevant information. The system prioritizes the most important context (character names, genre, recent content) and includes it first.

**Token Budget:**
API providers charge by token usage, and the system has a token budget for context. If context becomes too large (e.g., entire project outline), it's truncated to fit the budget. The most relevant context is preserved while less important details are cut.

### Adaptive Context Selection

The system is smart about what context to include:
- When continuing dialogue, it includes recent dialogue to maintain voice
- When describing scenes, it includes setting descriptions
- When creating characters, it includes character guidelines
- When writing action, it includes pacing notes

Different request types benefit from different context, and the system adapts accordingly.

## Async Request Processing

### Background Request Execution

To keep the UI responsive, API requests are processed asynchronously in background threads. While a request is being processed, the UI remains interactive and doesn't freeze.

**Threading Architecture:**
A dedicated thread pool processes API requests. When a request is submitted, it's added to a queue. Worker threads process requests from the queue one at a time. As requests complete, results are communicated back to the UI.

**Request Queuing:**
Multiple requests can be queued if users request multiple AI completions. Requests are processed in order (FIFO - first in, first out). However, priority requests (like high-cost items) can be prioritized.

**Progress Indication:**
While a request is processing, the UI shows a progress indicator. Users can see that something is happening and how long it's taking. For long requests, periodic status updates keep the user informed.

### Asynchronous Signal/Callback System

When an API request completes, the result needs to be communicated back to the UI. This is done through signals or callbacks.

**Completion Signals:**
When a request finishes successfully, a completion signal is emitted containing the response. The UI responds by displaying the response to the user.

**Failure Signals:**
If a request fails, a failure signal is emitted with the error message. The UI displays the error to the user and suggests retry or alternative actions.

**Progress Signals:**
During long operations, periodic progress signals can be emitted to update the UI. For example, when fetching context from the database, a signal is sent showing progress through the fetch.

**Status Signals:**
Status signals provide general information about what the system is doing (e.g., "Contacting OpenAI", "Processing response", "Calculating cost").

### Error Handling in Async Context

When errors occur in background threads, they must be properly caught and communicated. The system catches exceptions in worker threads and emits error signals rather than crashing the application.

**Network Errors:**
Connection failures are caught and retried automatically up to 3 times with exponential backoff. After 3 failures, an error is shown to the user with options to retry or cancel.

**API Errors:**
API errors (4xx and 5xx responses) are parsed and shown to the user. Specific error messages help users understand what went wrong. For example, "Your API key is invalid" vs. "Service temporarily unavailable".

**Timeout Errors:**
If a request takes longer than the timeout (typically 30 seconds), it's cancelled and an error is shown. This prevents hanging forever on unresponsive services.

## Request Deduplication and Optimization

### Request Hashing

To detect duplicate requests, each request is hashed. Identical requests generate identical hashes. The system checks if a request with this hash has been made recently. If so, it reuses the cached response instead of making a new call.

**Hash Input:**
The hash includes the prompt text, model selection, temperature setting, and other parameters that affect the response. Any difference results in a different hash.

**Hash Quality:**
Using a good hash function (like SHA-256) ensures that different requests almost never collide. The probability of a false match is negligible.

### Deduplication Window

Duplicate detection works within a time window (e.g., 7 days). If the same request was made more than 7 days ago, it's treated as a new request and a fresh response is generated. This prevents serving very stale responses.

### Batch Request Optimization

When multiple similar requests are queued, the system can sometimes combine them into a single API call for efficiency. For example, if three different text sections all need grammar checking, they might be combined into one larger request.

**Batch Benefits:**
- Fewer API calls reduce latency
- Batch discounts from some providers reduce costs
- Reduced rate limit pressure from fewer requests

**Batching Limitations:**
Not all requests can be batched. Some require real-time processing or have dependencies on previous results. Batching is only done when safe and beneficial.

# Settings & Configuration

## Settings Manager System

The settings system provides centralized management of all application configuration with persistent JSON-based storage. It uses a dot-notation system to access nested settings, making complex configuration trees intuitive to work with.

### Dot-Notation Access Pattern

Rather than navigating deeply nested dictionaries, the settings system allows accessing values using dot-separated paths. For example, `settings.get("ui.theme")` retrieves the theme value from the nested ui section. This pattern is much cleaner than `settings["ui"]["theme"]` and automatically creates missing sections on write.

**Nested Section Support:**
The system supports arbitrary nesting depth. Settings can be organized into logical sections (ui, api, export, etc.), and each section can contain subsections. For example, `settings.get("api.openai.key")` accesses the OpenAI key within the api section.

**Automatic Section Creation:**
When writing to a path that doesn't exist, missing sections are automatically created. Writing `settings.set("new.nested.value", 42)` creates the "new" and "nested" sections if they don't exist, then stores the value.

**Default Values:**
Get operations can specify default values. If a setting doesn't exist, the default is returned. For example, `settings.get("theme", "light")` returns "light" if the theme setting hasn't been configured yet.

### JSON Persistence

Settings are persisted to a JSON file (`config/user_settings.json`) on disk. This file is human-readable and can be manually edited if needed, though the UI is the recommended way to change settings.

**Automatic File Management:**
The JSON file is automatically created if it doesn't exist. The directory is created if needed. File permissions are set appropriately for the current user. Backups are created before writing to prevent data loss.

**Atomic Writes:**
Settings are written atomically - either the entire write succeeds or the file is unchanged. This prevents partially-written corrupted files if the system crashes during a write.

**Change Detection:**
When settings are modified through the UI, the changes are detected and saved automatically. If the settings file is modified externally (e.g., manually edited), the application detects this and reloads settings.

### In-Memory Caching

In addition to persistent JSON storage, settings are maintained in memory for fast access. When the application starts, all settings are loaded into memory. UI accesses happen in-memory, not from disk.

**Cache Invalidation:**
When settings are modified through the UI, the memory cache is updated immediately, and the change is written to disk in the background. This ensures UI responsiveness while maintaining persistence.

**Efficiency:**
Since settings are accessed frequently, keeping them in memory provides excellent performance. Disk writes are batched to reduce I/O operations.

## Default Settings Structure

The application maintains a comprehensive set of default settings organized into logical sections. Users can override any default through the settings UI or by editing the JSON file directly.

### User Interface Settings

**Theme Configuration:**
- **theme:** Specifies the visual appearance ("light", "dark", or "system" to follow OS settings)
- **primary_color:** Main accent color in hexadecimal format (e.g., "#2196F3" for blue)
- **secondary_color:** Secondary accent color for highlights and selections
- **text_color:** Default text color
- **background_color:** Default background color for main window
- **font_family:** Preferred font (e.g., "Arial", "Courier New")
- **font_size:** Default font size in points (8-24pt range)

**Window Geometry:**
- **width:** Default window width in pixels (e.g., 1280)
- **height:** Default window height in pixels (e.g., 800)
- **x:** Horizontal position when window opens
- **y:** Vertical position when window opens
- **maximized:** Whether window should start maximized

**UI Preferences:**
- **sidebar_width:** Width of left sidebar in pixels
- **show_status_bar:** Whether to display status bar
- **show_toolbar:** Whether to display toolbar
- **compact_mode:** Reduced visual density for smaller screens
- **animations_enabled:** Whether to show UI animations

### Writing Preferences

**Writing Style Defaults:**
- **default_tone:** Default writing tone (Formal, Professional, Conversational, Creative, Academic)
- **default_pov:** Default point of view (First, Second, Third Limited, Omniscient)
- **default_genre:** Default genre selection (Fiction, Fantasy, Mystery, etc.)
- **default_target_audience:** Default reader demographic (General, Children, Young Adults, Academic, Professional)

**Writing Assistance:**
- **enable_spell_check:** Enable real-time spell checking
- **enable_grammar_check:** Enable grammar analysis
- **highlight_repeated_words:** Highlight words used frequently
- **show_readability_score:** Display readability metrics in real-time
- **auto_save_interval:** How often to auto-save (seconds, typically 30-300)
- **highlight_long_sentences:** Flag sentences exceeding recommended length

**Writing Goals:**
- **daily_word_goal:** Target words to write per day (e.g., 1000)
- **session_word_goal:** Target words per session (e.g., 500)
- **weeklygoal:** Target words per week (e.g., 7000)
- **writing_reminder_interval:** When to remind user to write (hours)

### API Configuration

**API Key Storage:**
- **openai_key:** OpenAI API key (stored encrypted)
- **anthropic_key:** Anthropic API key (stored encrypted)
- **google_key:** Google API key (stored encrypted)
- **huggingface_key:** HuggingFace API key (stored encrypted)
- **words_api_key:** Words API key for vocabulary analysis
- **apyhub_key:** ApyHub key for readability API

**API Preferences:**
- **default_model:** Which AI model to use by default (e.g., "gpt-3.5-turbo")
- **default_provider:** Which API provider to use by default
- **request_timeout:** How long to wait for API response (seconds, typically 30)
- **max_retries:** How many times to retry failed requests (typically 3)
- **enable_api_caching:** Whether to cache API responses
- **cache_expiration_days:** How many days to keep cached responses (typically 7)

**API Rate Limiting:**
- **rate_limit_requests:** Maximum requests per time window
- **rate_limit_window:** Time window in seconds (typically 3600 for 1 hour)
- **enable_rate_limiting:** Whether to enforce rate limits
- **queue_excess_requests:** Queue requests that exceed limits instead of rejecting

### Export Configuration

**Export Preferences:**
- **default_format:** Which format to use by default (txt, md, docx, pdf, epub, json)
- **default_export_dir:** Directory to save exports to
- **include_metadata:** Include project metadata in exports
- **include_statistics:** Include text statistics in exports
- **compress_output:** Compress exported files
- **auto_backup_exports:** Keep backup of exports

**Format-Specific Options:**
- **docx_include_images:** Include images in DOCX export
- **pdf_quality:** PDF quality preset (high, medium, low)
- **epub_version:** EPUB version to use (2.0 or 3.0)
- **markdown_include_toc:** Include table of contents in Markdown

### Performance Settings

**Performance Tuning:**
- **cache_size_mb:** Maximum cache size in megabytes (100-5000)
- **analytics_update_interval:** How often to update analytics (seconds, 1-60)
- **database_optimization_frequency:** How often to optimize database (seconds, 300-86400)
- **connection_pool_size:** Number of database connections in pool (1-20)
- **query_timeout_ms:** How long to wait for database query (milliseconds, 1000-600000)

**Resource Usage:**
- **enable_performance_monitoring:** Track CPU and memory usage
- **performance_alert_threshold:** Alert when resource usage exceeds this percentage
- **max_background_threads:** Maximum threads for background tasks
- **enable_cpu_throttling:** Reduce resource usage on battery power

**Optimization Flags:**
- **enable_query_cache:** Cache database query results
- **enable_connection_pooling:** Use connection pool
- **enable_memory_optimization:** Aggressive memory cleanup
- **enable_compression:** Use compression for cache

### Analytics Settings

**Analytics Tracking:**
- **track_sessions:** Record writing session data
- **track_api_usage:** Track all API calls and costs
- **track_performance:** Collect performance metrics
- **track_analytics:** Generate statistical reports
- **retention_days:** How many days to keep historical data (typically 30-90)

**Goals and Targets:**
- **daily_goal:** Target words per day
- **weekly_goal:** Target words per week
- **monthly_goal:** Target words per month
- **project_target:** Default project word count goal

**Analytics Display:**
- **show_analytics_dashboard:** Display analytics widget
- **show_progress_bar:** Show project progress visualization
- **show_metrics:** Display text metrics in editor
- **show_suggestions:** Display improvement suggestions

### Advanced Settings

**Debug Mode:**
- **debug_mode:** Enable debug logging and additional information
- **logging_level:** Logging verbosity (DEBUG, INFO, WARNING, ERROR)
- **log_file_path:** Where to save log files
- **max_log_size_mb:** Maximum log file size before rotation
- **keep_log_backups:** How many old log files to keep

**Database Settings:**
- **database_path:** Location of SQLite database file
- **enable_foreign_keys:** Enforce foreign key constraints
- **enable_wal_mode:** Use Write-Ahead Logging for better concurrency
- **auto_vacuum_mode:** Automatic database optimization mode
- **journal_mode:** How to handle transaction journal

**Application Behavior:**
- **auto_update_enabled:** Check for application updates
- **send_crash_reports:** Send error reports to developers
- **enable_telemetry:** Send usage data
- **startup_project:** Which project to open on startup
- **recent_projects_count:** How many recent projects to remember

**Reset Options:**
- **reset_to_defaults_on_startup:** Start with defaults each time
- **clear_cache_on_startup:** Clear cache each time
- **delete_logs_on_startup:** Delete log files each time

## Settings UI Components

### Settings Dialog Structure

The settings interface is organized into tabs, with each tab covering a major settings category. This prevents overwhelming users with hundreds of options at once.

**Tab Organization:**
1. **General Tab** - Basic application settings
2. **Appearance Tab** - Theme, colors, fonts
3. **Writing Tab** - Writing defaults and assistants
4. **API Tab** - AI provider configuration
5. **Export Tab** - Export format preferences
6. **Performance Tab** - Advanced performance tuning
7. **Analytics Tab** - Data tracking and reporting
8. **Advanced Tab** - Developer options and reset

### General Tab

Contains basic application settings like project directory, auto-save interval, and startup behavior.

**Controls:**
- Text input for application name
- Directory browser for default project directory
- Spinner control for auto-save interval (allowing manual entry or up/down buttons)
- Dropdown for startup project selection
- Checkbox for auto-update

### Appearance Tab

Allows customization of visual appearance through theme and color selection.

**Controls:**
- Dropdown for theme selection (light/dark/system)
- Color picker for primary color with hex input field
- Color picker for secondary color
- Color picker for text color
- Color picker for background color
- Font selection dropdown with system fonts
- Font size spinner (8-24pt)
- Live preview showing theme changes
- Button to reset to default colors

**Real-Time Preview:**
As users change colors or fonts, a preview area updates immediately to show how the changes look. This provides instant feedback without needing to apply and close the dialog.

### Writing Tab

Configures defaults for writing assistance and analysis.

**Controls:**
- Dropdown for default tone with explanation text
- Dropdown for default POV with examples
- Dropdown for default genre
- Dropdown for target audience
- Checkbox for spell check
- Checkbox for grammar check
- Checkbox for repeated word highlighting
- Checkbox for readability score display
- Spinner for auto-save interval
- Spinner for daily/weekly/monthly writing goals

### API Tab

Configures access to AI APIs and related services.

**Controls:**
- Text input fields for API keys (with masking for security)
- "Test Connection" buttons for each API to verify configuration
- Status indicators (green for working, red for invalid, yellow for untested)
- Dropdown for default model selection (updated based on provider)
- Spinner for request timeout
- Checkbox for API caching
- Info text showing remaining API quota (if available)

**Security:**
API keys are stored securely and never displayed in plaintext. When editing, the field shows masked asterisks. Only when explicitly clicking "Show" does the actual key appear briefly.

### Export Tab

Configures export format preferences and options.

**Controls:**
- Dropdown for default export format
- Directory browser for export directory
- Checkboxes for format-specific options
- Checkboxes for metadata and statistics inclusion
- Checkbox for compression
- Format selection checkboxes (which formats to support)

### Performance Tab

Advanced performance tuning for power users.

**Controls:**
- Slider for cache size (100-5000 MB)
- Slider for analytics update interval
- Spinner for connection pool size
- Spinner for query timeout
- Checkbox for query caching
- Checkbox for connection pooling
- Checkbox for memory optimization
- Checkbox for compression
- Button to "Optimize Now" (manual optimization)

**Information Display:**
Shows current resource usage (CPU %, Memory MB, Disk GB) with historical charts. Users can see the impact of performance settings on resource usage.

### Analytics Tab

Configures what data to track and display.

**Controls:**
- Checkboxes for tracking options (sessions, API usage, performance)
- Spinner for data retention (days)
- Writing goal configuration (daily, weekly, monthly)
- Checkboxes for display options (dashboard, progress bar, metrics)
- Button to view analytics
- Button to export analytics

### Advanced Tab

Developer and power user options.

**Controls:**
- Checkbox for debug mode with explanation
- Dropdown for logging level (DEBUG/INFO/WARNING/ERROR)
- Text display showing log file location
- Button to open log file in editor
- Checkbox for enabling crash reports
- Checkbox for telemetry
- Buttons for reset to defaults, clear cache, delete logs
- Warning messages for destructive operations

## Settings Validation and Error Handling

### Input Validation

Settings are validated before being saved. Invalid values are rejected with clear error messages.

**Validation Rules:**
- Font size must be between 8 and 24 points
- Cache size must be between 100 and 5000 MB
- Timeout values must be positive numbers
- API keys must be non-empty strings (if enabled)
- Directory paths must exist or be creatable
- Color codes must be valid hex format

**Validation Errors:**
When validation fails, the invalid field is highlighted in red, and an error message appears. The user can see exactly what's wrong and how to fix it. Settings are not saved until all fields are valid.

### Conflict Resolution

When conflicting settings are detected, the system resolves them intelligently:
- If cache size exceeds available memory, it's reduced
- If timeout is shorter than average query time, it's increased
- If pool size exceeds system resources, it's capped

Users are notified of these adjustments so they understand what changed.

## Settings Persistence and Recovery

### Automatic Backup

Before writing new settings, a backup of the current settings file is created. If something goes wrong, the previous settings can be restored.

**Backup Location:**
Backups are stored with timestamps in a backup directory. Users can manually restore from any backup if needed.

### Recovery on Corruption

If the settings file is corrupted or unreadable, the application detects this and offers options:
- Use the most recent backup
- Reset to defaults
- Manually specify a settings file to use

This ensures the application can always start, even if settings are corrupted.

### Settings Version Compatibility

When application versions change, the settings format might change. The system handles this by:
- Detecting the version of the loaded settings
- Automatically migrating to the new format
- Preserving user customizations where possible
- Resetting new settings to defaults



# Export Functionality

## Export System Architecture

### ExportManager Class
**Location:** `src/system/export_manager.py`

**Purpose:** Comprehensive export to multiple document formats

**Supported Formats:**
1. **TXT** - Plain text with metadata headers
2. **Markdown (.md)** - Markdown format with YAML frontmatter
3. **DOCX** - Microsoft Word document with formatting
4. **PDF** - Professional PDF with styled headers
5. **EPUB** - eBook format for e-readers
6. **JSON** - Structured data format

### Export Methods

**Method: export_to_txt()**
```python
def export_to_txt(
    content: str,
    filename: str,
    metadata: Optional[Dict] = None
) -> bool
```

**Output Format:**
```
================================================
TITLE
================================================
Author: Author Name
Export Date: YYYY-MM-DD HH:MM:SS
Description: Project description

================================================
CONTENT
================================================

[Full content text here...]
```

**Method: export_to_markdown()**
```python
def export_to_markdown(
    content: str,
    filename: str,
    metadata: Optional[Dict] = None
) -> bool
```

**Output Format:**
```markdown
---
title: "Project Title"
author: "Author Name"
date: 2024-11-14
description: "Project description"
word_count: 5000
---

# Content

[Full content here...]
```

**Method: export_to_docx()**
```python
def export_to_docx(
    content: str,
    filename: str,
    metadata: Optional[Dict] = None
) -> bool
```

**Features:**
- Professional formatting
- Centered title and author
- Metadata headers
- Paragraph formatting
- Font styling (Arial, 12pt)
- Proper spacing

**Output Components:**
- Title (Heading 1, centered)
- Author (italic, centered)
- Export date (italic, centered)
- Description (paragraph)
- Body text (formatted paragraphs)

**Method: export_to_pdf()**
```python
def export_to_pdf(
    content: str,
    filename: str,
    metadata: Optional[Dict] = None
) -> bool
```

**Features:**
- Styled headers with metadata
- Professional typography
- Page breaks
- Proper spacing and margins
- ReportLab or PyPDF2 backend

**Layout:**
- Header section: Title, author, date
- Body section: Formatted paragraphs
- Page size: Letter (8.5"x11")
- Margins: 1 inch all sides

**Method: export_to_epub()**
```python
def export_to_epub(
    content: str,
    filename: str,
    metadata: Optional[Dict] = None
) -> bool
```

**Features:**
- eBook-compatible format
- Chapter structure
- Metadata embedding
- XHTML content
- EPUB3 compatible

**Structure:**
- Book metadata (title, author, language)
- Table of contents
- Main content chapter
- Navigation document

**Method: export_to_json()**
```python
def export_to_json(
    data: Dict,
    filename: str
) -> bool
```

**Output Format:**
```json
{
  "metadata": {
    "title": "Project Title",
    "author": "Author Name",
    "created_date": "2024-11-14",
    "export_date": "2024-11-14T12:34:56",
    "word_count": 5000,
    "description": "Project description"
  },
  "content": {
    "text": "Full content here...",
    "sections": []
  }
}
```

**Method: export_multiple_formats()**
```python
def export_multiple_formats(
    content: str,
    filename: str,
    formats: List[str],
    metadata: Optional[Dict] = None
) -> Dict[str, bool]
```

**Returns:**
```python
{
    'txt': True,
    'docx': True,
    'pdf': True,
    'epub': False,  # If library not available
    'json': True
}
```

### Export Configuration

**Export Directory:**
- Default: `exports/` (relative to application directory)
- Configurable via settings
- Auto-created if missing
- Organized by format

**File Naming:**
- Format: `{filename}.{extension}`
- Examples: `my_novel.docx`, `story.pdf`
- Timestamp appended if file exists

### Export UI Components

**ExportFormatSelector Widget:**
**Location:** `src/ui/export_ui.py`

**Format Selection:**
- Checkboxes for each format
- Visual format icons
- Description of each format
- Default selection (DOCX)

**Format-Specific Options:**

**DOCX Options:**
- Include images (checkbox)
- Insert page breaks between chapters (checkbox)
- Preserve formatting (checkbox)

**PDF Options:**
- Quality preset (High/Medium/Low)
- Include bookmarks (checkbox)
- Paper size selection

**EPUB Options:**
- Include table of contents (checkbox)
- Split chapters (checkbox)
- EPUB version (2.0/3.0)

**Output Settings:**
- Directory browser
- Filename prefix input
- Preview filename

**ExportManagerWidget:**

**Tabs:**
1. **Export Tab**
   - Format selection
   - Options configuration
   - Export button
   - Progress indicator

2. **History Tab**
   - List of recent exports
   - File size information
   - Export date
   - Format indicator

3. **Validation Tab**
   - Export file validation
   - Integrity checking
   - Format verification
   - Size information

### Export Validation

**ExportValidator Class:**
**Location:** `src/export_formats/validator.py`

**Validation Checks:**

**DOCX Validation (DOCXValidator):**
- ZIP file integrity
- Valid DOCX structure
- XML document validation
- Metadata presence
- Content accessibility

**PDF Validation (PDFValidator):**
- PDF file format validation
- Version checking
- Compression verification
- Page count validation
- Metadata extraction

**EPUB Validation (EPUBValidator):**
- ZIP file integrity
- Container.xml validation
- OPF file validation
- XHTML content validation
- TOC validation

**Validation Methods:**
```python
validate_file(file_path: str, format_type: str = None) -> ExportValidationResult
validate_docx(file_path: str) -> ExportValidationResult
validate_pdf(file_path: str) -> ExportValidationResult
validate_epub(file_path: str) -> ExportValidationResult
validate_multiple_files(file_paths: List[str]) -> Dict[str, ExportValidationResult]
```

**ExportValidationResult:**
```python
class ExportValidationResult:
    is_valid: bool
    format_type: str
    file_path: str
    error_message: Optional[str]
    file_size: int
    creation_date: str
    warnings: List[str]
```

---

# Performance Monitoring

## Performance Monitor System

### PerformanceMonitor Class
**Location:** `src/core/performance_monitor.py`

**Purpose:** Real-time system resource monitoring and statistics

**Monitoring Metrics:**

1. **CPU Usage**
   - Current percentage (0-100%)
   - Per-core breakdown
   - Process-specific usage
   - Historical trend

2. **Memory Usage**
   - Current usage (MB)
   - Percentage of total
   - Available memory
   - Virtual memory usage

3. **Disk Usage**
   - Current usage (GB)
   - Percentage of total
   - Free space
   - Read/write activity

4. **Application Performance**
   - Frame rate (FPS)
   - Response time
   - Database query time
   - API response time

**Update Intervals:**
- Default: 1-2 seconds
- Configurable: 1-60 seconds
- Background thread monitoring

**Display Locations:**
- Status bar: CPU % and Memory MB
- Dashboard: Real-time charts
- Analytics: Performance trends
- Settings: Performance configuration

### Performance Dashboard

**Dashboard Components:**

1. **System Resources Widget**
   - CPU usage (gauge display)
   - Memory usage (gauge display)
   - Disk usage (gauge display)
   - Color-coded thresholds

2. **Performance Charts**
   - CPU trend over time
   - Memory trend over time
   - Disk activity
   - API response times

3. **Database Performance**
   - Query execution times
   - Connection pool status
   - Cache hit/miss rates
   - Slow query detection

4. **API Statistics**
   - Total API calls
   - Successful requests
   - Failed requests
   - Average response time
   - Cost breakdown by API

### Performance Thresholds

**Warning Levels:**
```python
{
    "cpu_threshold": 80,      # % CPU usage warning
    "memory_threshold": 80,   # % memory usage warning
    "disk_threshold": 90      # % disk usage warning
}
```

**Color Coding:**
- Green: <50% usage
- Yellow: 50-80% usage
- Red: >80% usage

### Performance Optimization

**Automatic Optimizations:**
1. **Database Optimization**
   - VACUUM command
   - Index analysis
   - Query optimization
   - Connection pool tuning

2. **Cache Optimization**
   - Expired entry cleanup
   - Cache size management
   - Compression verification
   - Hit rate analysis

3. **Memory Optimization**
   - Garbage collection
   - Unused object cleanup
   - Cache trimming
   - Memory profiling

**Optimization Methods:**
```python
optimize_database() -> bool
  # Runs: VACUUM, ANALYZE, etc.

cleanup_cache() -> int
  # Returns: entries deleted

cleanup_temp_files() -> int
  # Returns: files deleted

optimize_connections() -> bool
  # Rebalances connection pool
```

---

# Advanced Features

## Project Management System

### Project Lifecycle

**Project Creation:**
```python
create_new_project(
    name: str,
    genre: str,
    target_words: int = 50000,
    metadata: Optional[Dict] = None
) -> bool
```

**Project Initialization:**
- Creates project directory: `projects/{name}/`
- Initializes project metadata
- Creates empty content file
- Sets up project configuration
- Creates initial database entry
- Sets status to "active"

**Project Loading:**
```python
load_project(name: str) -> Project
```

**Retrieves:**
- Project configuration
- Current word count
- Writing sessions
- Project metadata
- Recent modifications

**Project Switching:**
- Saves current project state
- Clears UI state
- Loads new project data
- Updates display
- Refreshes all metrics

**Project Deletion:**
```python
delete_project(name: str, confirm: bool = True) -> bool
```

**Process:**
- Confirmation dialog
- Backup creation (optional)
- File deletion
- Database cleanup
- Cache invalidation

### Project Templates

**Available Templates:**
1. **Novel** (50,000+ words)
   - Complete novel structure
   - Chapter templates
   - Character development sheets
   - Plot outline template

2. **Screenplay** (90-120 pages)
   - Scene structure
   - Character profiles
   - Dialog format
   - Action descriptions

3. **Blog Series** (Varies)
   - Post structure
   - Category organization
   - Publishing schedule
   - SEO optimization

4. **Short Story** (1,000-10,000 words)
   - Compressed story arc
   - Quick character creation
   - Conflict resolution
   - Ending preparation

5. **Fantasy Epic** (100,000+ words)
   - World building guide
   - Magic system template
   - Multi-plot structure
   - Character relationship map

6. **Mystery/Thriller** (80,000+ words)
   - Clue worksheet
   - Red herring planning
   - Timeline tracker
   - Reveal schedule

7. **Romance Novel** (70,000+ words)
   - Relationship progression
   - Tension building
   - Conflict escalation
   - Resolution planning

## Backup System

**Backup Features:**
- Automatic project backups
- Manual backup creation
- Backup scheduling
- Backup restoration
- Incremental backups
- Compression support

**Backup Methods:**
```python
create_backup(project_name: str, description: str = "") -> str
  # Returns: backup_id

restore_backup(project_name: str, backup_id: str) -> bool

list_backups(project_name: str) -> List[Backup]
  # Each backup has: id, date, size, description

delete_backup(project_name: str, backup_id: str) -> bool
```

## Plugin System

**Plugin Architecture:**
- Plugin directory: `plugins/`
- Plugin manifest: `plugin.json`
- Plugin entry point: `main.py`

**Plugin Types:**
1. **Text Processors** - Text analysis plugins
2. **Export Formats** - Custom export formats
3. **Workflow Extensions** - Workflow step additions
4. **UI Widgets** - Custom UI components
5. **API Integrations** - New API support

**Plugin Interface:**
```python
class Plugin:
    name: str
    version: str
    description: str

    def initialize()
    def execute()
    def cleanup()
    def get_config()
    def set_config(config)
```

## Automated Workflow

**11-Step Writing Process:**
1. Project Initialization
2. Character Development
3. World Building
4. Plot Outlining
5. Scene Planning
6. First Draft Writing
7. Editing Pass 1
8. Editing Pass 2
9. Beta Reader Feedback
10. Final Revisions
11. Export & Publishing

**Each Step:**
- Accepts user input
- Generates AI content
- Provides quality checks
- Requires user approval
- Tracks progress
- Saves state

---

# Integration Points

## File Operations

**File I/O Location:** `src/system/file_operations.py`

**Operations:**
```python
get_project_list() -> List[str]
  # Returns all project names

validate_project_name(name: str) -> bool
  # Validates project name format

initialize_project_files(project_name: str) -> bool
  # Creates project directory structure

read_project_file(project_name: str, filename: str) -> str
  # Reads project file content

write_project_file(project_name: str, filename: str, content: str) -> bool
  # Writes to project file

delete_project_directory(project_name: str) -> bool
  # Removes entire project directory

list_project_files(project_name: str) -> List[str]
  # Lists all files in project

backup_project(project_name: str) -> str
  # Returns backup path
```

## Memory Caching

**Cache Manager:** `src/system/memory_manager.py`

**Features:**
- In-memory caching
- LRU eviction policy
- TTL (time-to-live) support
- Thread-safe operations
- Statistics tracking

## Configuration Loading

**Configuration Sources:**
1. Default configuration (hardcoded)
2. User configuration (config/user_settings.json)
3. Environment variables
4. Command-line arguments

**Load Order:**
- Start with defaults
- Override with user settings
- Override with environment
- Override with CLI args

---

# Error Handling & Logging

## Error Handling System

**ErrorHandler Class:** `src/core/error_handling_system.py`

**Error Types:**
- APIError - External API failures
- DatabaseError - Database operation failures
- FileError - File I/O failures
- ValidationError - Input validation failures
- ConfigError - Configuration issues

**Error Handler Methods:**
```python
handle_error(error: Exception, context: str = "") -> None
  # Logs error and shows user notification

create_styled_message_box(title: str, message: str, error_type: str) -> None
  # Shows styled error dialog

get_error_context() -> Dict[str, Any]
  # Returns current error context

clear_errors() -> None
  # Resets error state
```

## Logging System

**Logger Setup:**
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/fanws.log'),
        logging.StreamHandler()
    ]
)
```

**Log Levels:**
- DEBUG: Detailed diagnostic information
- INFO: General informational messages
- WARNING: Warning messages
- ERROR: Error messages
- CRITICAL: Critical failures

**Log Files:**
- Location: `logs/`
- Naming: `fanws.log` (rotated daily)
- Retention: 30 days default

---

# Data Structures

## Key Data Models

### Project Model
```python
@dataclass
class Project:
    id: int
    name: str
    created_date: datetime
    last_modified: datetime
    status: str  # active, paused, completed
    settings: Dict[str, Any]
    word_count: int
    target_words: int
    metadata: Dict[str, Any]
```

### APIUsageRecord Model
```python
@dataclass
class APIUsageRecord:
    id: int
    project_id: Optional[int]
    api_type: str  # openai, anthropic, google, huggingface
    endpoint: str
    timestamp: datetime
    tokens_used: int
    cost: float
    response_time: float
    success: bool
    error_message: Optional[str]
    request_hash: str
```

### WritingSession Model
```python
@dataclass
class WritingSession:
    id: int
    project_id: int
    start_time: datetime
    end_time: Optional[datetime]
    words_written: int
    session_type: str  # writing, editing, review
```

---

# Workflow & User Flows

## Core Writing Process Workflow

### Phase 1: Project Initialization & Setup

**Step 1: Application Launch**
```
1. Initialize PyQt5 Application
2. Load Configuration (config/user_settings.json)
3. Initialize Database Manager
   └─ Create database if missing
   └─ Run migrations
   └─ Initialize connection pool
4. Check API Keys (Stored in settings)
5. Load Performance Monitor
6. Display Main Window with Dashboard
7. Set status bar to "Ready"
```

**Step 2: Project Selection/Creation**
```
User opens project selector:
├─ View existing projects
│  ├─ Sort by: name, date modified, word count
│  ├─ Filter by: status (active/paused/completed)
│  └─ Quick load (double-click or button)
├─ Create new project
│  ├─ Enter project name
│  ├─ Select template (Novel, Screenplay, etc.)
│  ├─ Set target word count
│  ├─ Define genre and style
│  ├─ Create project directory
│  ├─ Initialize database entry
│  └─ Create project metadata file
└─ Recent projects quick access
```

**Project Creation Database Operations:**
```python
# Database entry created:
INSERT INTO projects (
    name, created_date, last_modified, status,
    word_count, target_words, settings
) VALUES (?, ?, ?, 'active', 0, ?, ?)

# Project directory structure:
projects/
└── {project_name}/
    ├── content.txt
    ├── metadata.json
    ├── outline.md
    ├── characters.json
    └── settings.json
```

**Step 3: Project Loading**
```
1. Retrieve project from database
2. Load project metadata (name, goals, target audience)
3. Load current content from file system
4. Restore session state
   └─ Cursor position
   └─ Scroll position
   └─ Open sections
5. Calculate and display metrics
6. Load recent writing sessions
7. Initialize analytics dashboard
8. Update UI with project-specific settings
9. Set status to "[Project Name] loaded"
```

### Phase 2: Writing Session Initiation

**Writing Session Start:**
```
User clicks "Start Writing" or begins typing:

1. Create WritingSession record
   ├─ project_id: Current project
   ├─ start_time: Current timestamp
   ├─ session_type: "writing"
   └─ words_written: 0

2. Enable writing mode
   ├─ Focus text editor
   ├─ Activate word count tracking
   ├─ Enable auto-save timer
   └─ Start elapsed time counter

3. Initialize session tracking
   ├─ Track character count
   ├─ Monitor typing speed
   ├─ Record keystroke patterns
   └─ Calculate productivity metrics

4. Update status bar: "Writing session in progress"

5. Schedule auto-save (every 30-60 seconds)
   └─ Save content to file
   └─ Update word count in database
   └─ Update last_modified timestamp
```

**Auto-Save Mechanism:**
```python
def auto_save_content():
    """Execute every 30-60 seconds during active writing"""
    1. Get current content from editor
    2. Calculate word/character count delta
    3. Update project.word_count in database
    4. Write content to project/content.txt
    5. Log writing session progress
    6. Update timestamp
    7. Emit signal for UI update
    8. Store in cache for performance
```

### Phase 3: Real-Time Feedback & Analysis Loop

**Real-Time Metrics Update (Every 1-2 seconds):**
```
While user is writing:

1. Monitor text changes in editor
2. Trigger text analysis debounce (500ms minimum between updates)
3. Execute analysis suite:
   ├─ Character count
   ├─ Word count
   ├─ Sentence count
   ├─ Paragraph count
   ├─ Average sentence length
   └─ Readability score (cached)

4. Update dashboard metrics
   ├─ Progress bar (current vs target)
   ├─ Words today counter
   ├─ Session word count
   └─ Time elapsed

5. Detection of potential issues:
   ├─ Repeated words (flagged if >3 occurrences/1000 words)
   ├─ Long sentences (>25 words)
   ├─ Complex vocabulary (flagged via API)
   └─ Readability drop (>10 point decrease)

6. Update status bar:
   ├─ Current word count
   ├─ Reading time estimate
   ├─ CPU/Memory usage
   └─ Connection status
```

**Readability Feedback System:**
```
As user writes, calculate readability metrics:

1. Flesch Reading Ease Score (0-100)
   ├─ 90-100: Very Easy (Elementary)
   ├─ 80-89: Easy (Clear communication)
   ├─ 70-79: Fairly Easy (Standard)
   ├─ 60-69: Standard (General audiences)
   ├─ 50-59: Fairly Difficult (Requires attention)
   ├─ 30-49: Difficult (Educated readers)
   └─ 0-29: Very Difficult (Technical)

2. Grade Level Assessment
   └─ Display as: "Grade 8-9 reading level"

3. Complex Word Detection
   ├─ Words >3 syllables
   ├─ Technical/rare vocabulary
   └─ Provide synonym suggestions from Words API

4. Sentence Structure Analysis
   ├─ Average words per sentence
   ├─ Sentence variety (short/medium/long)
   └─ Readability of sentences
```

### Phase 4: Interactive Feedback & Suggestions

**User Requests Analysis (On-Demand):**

**When user clicks "Text Analysis":**
```
1. Extract current text from editor
2. Run comprehensive text analysis:
   ├─ Statistical metrics
   │  ├─ Total words
   │  ├─ Total characters
   │  ├─ Unique words
   │  ├─ Total sentences
   │  ├─ Total paragraphs
   │  ├─ Average words/sentence
   │  └─ Average characters/word
   ├─ Complexity scoring
   │  ├─ Readability score (0-100)
   │  ├─ Grade level
   │  ├─ Complexity level (Simple/Moderate/Complex)
   │  └─ Reading time estimate
   └─ Issues detected
      ├─ Repeated words with frequency counts
      ├─ Long sentences (>20 words)
      ├─ Short sentences (<5 words)
      └─ Fragmented paragraphs

3. Display results in dedicated widget
   └─ Color-coded severity (green/yellow/red)

4. Store analysis in cache
   └─ Cache key: hash of content
   └─ Expiration: 1 hour
```

**When user clicks "Grammar Check":**
```
1. Extract text and tokenize into sentences
2. For each sentence:
   ├─ Check for repeated words
   ├─ Identify long sentences
   ├─ Analyze grammar structure
   ├─ Call Words API if key available
   │  └─ Get synonyms for repeated words
   │  └─ Get definitions for complex words
   └─ Compile suggestions

3. Detect patterns:
   ├─ Repeated word usage
   │  └─ Flag words appearing >3x
   ├─ Capitalization issues
   │  └─ Flag inconsistent capitalization
   ├─ Punctuation issues
   │  └─ Flag punctuation inconsistencies
   └─ Style issues
      └─ Passive voice overuse
      └─ Clichéd phrases

4. Generate report:
   ├─ List issues with line numbers
   ├─ Provide severity ratings
   ├─ Suggest improvements
   └─ Show before/after examples

5. Allow user to:
   ├─ Accept suggestions
   ├─ Ignore suggestions
   ├─ Apply to similar instances
   └─ Add to custom dictionary
```

**When user clicks "Style Analysis":**
```
1. User selects writing parameters:
   ├─ Tone (Formal/Professional/Conversational/Creative/Academic)
   ├─ Genre (Fiction/Fantasy/Mystery/Romance/etc.)
   └─ POV (First/Second/Third Limited/Omniscient)

2. Analyze text against selected style:
   ├─ Tone consistency
   │  └─ Check vocabulary matches tone
   │  └─ Verify sentence structure aligns
   ├─ Genre appropriateness
   │  └─ Check for genre-specific elements
   │  └─ Verify pacing matches genre
   └─ POV consistency
      └─ Monitor character perspective
      └─ Detect POV switches
      └─ Flag perspective violations

3. Generate style recommendations:
   ├─ Suggest vocabulary improvements
   ├─ Recommend pacing adjustments
   ├─ Propose structure changes
   └─ Highlight style inconsistencies

4. Provide comparison examples:
   ├─ "Current style: [example]"
   ├─ "Recommended style: [example]"
   └─ "Reason: [explanation]"
```

**When user clicks "Readability Analysis":**
```
1. User selects target audience:
   ├─ General (8th-12th grade)
   ├─ Academic (College level)
   ├─ Professional (Adult technical)
   ├─ Children (4th-6th grade)
   └─ Young Adults (6th-8th grade)

2. Calculate readability metrics:
   ├─ Flesch Reading Ease Score
   ├─ Grade level equivalent
   ├─ Reading time estimation
   ├─ Complex word percentage
   ├─ Average sentence length
   └─ Syllable count

3. Generate feedback:
   ├─ "✓ Suitable for [audience]" OR "✗ Too [easy/difficult]"
   ├─ Identify problematic sections
   ├─ Suggest improvements:
   │  └─ Simplify vocabulary
   │  └─ Shorten sentences
   │  └─ Add transitions
   │  └─ Break up paragraphs
   └─ Provide before/after examples

4. Display visual feedback:
   ├─ Score gauge (0-100)
   ├─ Color-coded difficulty
   └─ Grade level badge
```

**When user clicks "Consistency Check":**
```
1. Scan full text for consistency:
   ├─ Character name spelling (flag variations)
   ├─ Place name spelling (flag variations)
   ├─ Terminology consistency
   │  └─ Track technical terms
   │  └─ Verify consistent usage
   ├─ Capitalization patterns
   │  └─ Proper nouns
   │  └─ Special terms
   ├─ Verb tense consistency
   │  └─ Past vs Present
   │  └─ Conditional consistency
   ├─ Punctuation patterns
   │  └─ Dialog punctuation
   │  └─ Dash/ellipsis usage
   └─ Narrative consistency
      └─ POV adherence
      └─ Timeline accuracy

2. Build consistency report:
   ├─ List all variations found
   ├─ Show frequency of each variant
   ├─ Suggest standardization
   └─ Allow batch corrections

3. Enable bulk fixes:
   ├─ Replace all instances
   ├─ Review before applying
   └─ Track changes for undo
```

### Phase 5: AI-Powered Content Assistance

**When user requests AI continuation:**
```
1. Prepare context:
   ├─ Get last 500 characters of current content
   ├─ Add project metadata
   │  └─ Genre, style, tone
   ├─ Include character list
   ├─ Include story outline (first 1000 chars)
   └─ Add writing prompt from user

2. Select appropriate API:
   ├─ Check available API keys
   ├─ Choose based on:
   │  └─ Cost preferences
   │  └─ Speed requirements
   │  └─ Quality needs
   └─ Fall back to secondary API if needed

3. Build context-aware prompt:
   ```
   [Project Context]
   Project: {name}
   Genre: {genre}
   Style: {style}
   Tone: {tone}
   Target Audience: {audience}

   [Story Elements]
   Main Characters: {characters}
   Setting: {location}
   Key Themes: {themes}

   [Current Context]
   Recent Content: {last_500_chars}

   [User Request]
   {user_prompt}
   ```

4. Make API request:
   ├─ Check rate limiter
   ├─ Look up response cache (if available)
   ├─ If cache miss:
   │  └─ Send request to API
   │  └─ Parse response
   │  └─ Cache result
   ├─ Log API usage to database
   └─ Calculate and store cost

5. Process response:
   ├─ Extract generated text
   ├─ Validate quality
   ├─ Format for insertion
   └─ Present to user for approval

6. User decision:
   ├─ Accept (insert into document)
   ├─ Reject (discard)
   ├─ Edit (modify before accepting)
   └─ Regenerate (try different prompt)

7. If accepted:
   ├─ Insert into editor
   ├─ Update word count
   ├─ Mark in content as AI-generated (optional)
   ├─ Trigger auto-save
   └─ Update analytics
```

### Phase 6: Analytics & Progress Tracking

**Dashboard Updates (Real-Time):**
```
As user writes and edits:

1. Update writing progress:
   ├─ Words written today
   ├─ Words written this session
   ├─ Progress toward daily goal
   ├─ Progress toward project goal
   └─ Days remaining to deadline (if set)

2. Update activity metrics:
   ├─ Total projects created
   ├─ Words written (all-time)
   ├─ Writing sessions completed
   ├─ Active project progress
   └─ Recent activity log

3. Calculate productivity insights:
   ├─ Average words per session
   ├─ Average session duration
   ├─ Most productive day/time
   ├─ Writing streaks
   └─ Estimated completion date

4. Update performance metrics:
   ├─ Database query performance
   ├─ Cache hit rates
   ├─ API response times
   ├─ Memory usage
   └─ CPU usage

5. Store session data:
   ├─ Update WritingSession record
   ├─ Log session to database
   ├─ Archive historical data
   └─ Generate session report
```

**Analytics Report Generation:**
```
User can generate comprehensive reports:

1. Session Report:
   ├─ Session duration
   ├─ Words written
   ├─ Productivity metrics
   ├─ Focus patterns
   └─ Improvement suggestions

2. Project Report:
   ├─ Total word count
   ├─ Progress percentage
   ├─ Estimated completion
   ├─ Writing statistics
   └─ Quality metrics

3. Quality Report:
   ├─ Readability scores
   ├─ Complexity analysis
   ├─ Grammar quality
   ├─ Style consistency
   └─ Improvement areas

4. API Usage Report:
   ├─ Total API calls
   ├─ Cost breakdown by API
   ├─ Most-used features
   ├─ Cache efficiency
   └─ Performance insights
```

### Phase 7: Saving & Export

**Manual Save:**
```
User presses Ctrl+S or clicks Save:

1. Get current content from editor
2. Calculate metrics (word count, etc.)
3. Write to project/content.txt
4. Update database:
   ├─ Update project.word_count
   ├─ Update project.last_modified
   └─ Log to change_history table
5. Update status: "✓ Saved"
6. Clear unsaved indicator
7. Emit saved signal for UI updates
```

**Export Process:**
```
User clicks Export:

1. User selects export format(s):
   ├─ TXT (plain text)
   ├─ Markdown (.md)
   ├─ DOCX (Word)
   ├─ PDF
   ├─ EPUB (e-book)
   └─ JSON (structured data)

2. Configure export options:
   ├─ Include metadata (Y/N)
   ├─ Include statistics (Y/N)
   ├─ Compress output (Y/N)
   └─ Custom filename

3. For each selected format:
   ├─ Generate output in specified format
   ├─ Validate generated file
   ├─ Store in exports/ directory
   ├─ Log export to analytics
   └─ Report success/failure

4. Post-export:
   ├─ Show file locations
   ├─ Offer to open files
   ├─ Update export history
   ├─ Show file sizes
   └─ Display generation time
```

### Phase 8: Session End & Cleanup

**Writing Session End:**
```
When user stops writing or closes app:

1. End WritingSession record:
   ├─ Calculate end_time
   ├─ Calculate total words_written
   ├─ Calculate session duration
   └─ Update database record

2. Perform final save:
   ├─ Save current content
   ├─ Update metrics
   ├─ Write session summary
   └─ Archive to history

3. Generate session feedback:
   ├─ "Great session! 1,250 words written"
   ├─ "You're X% toward your daily goal"
   ├─ Performance tips
   └─ Suggestion for next session

4. Store analytics:
   ├─ Log to SessionAnalytics table
   ├─ Update ProjectMetrics
   ├─ Update UserStatistics
   └─ Store in cache
```

**Application Shutdown:**
```
User closes AAWT:

1. Check for unsaved content:
   ├─ If changes exist:
   │  └─ Ask user: "Save before closing?"
   │  └─ Save if confirmed
   └─ If no changes, skip

2. End active writing session:
   ├─ Calculate final metrics
   ├─ Store session data
   └─ Generate final report

3. Close database:
   ├─ Commit pending transactions
   ├─ Close all connections
   ├─ Run VACUUM (optional)
   └─ Close connection pool

4. Save application state:
   ├─ Save window geometry
   ├─ Save current project
   ├─ Save theme preferences
   ├─ Save all settings
   └─ Save UI state

5. Cleanup:
   ├─ Stop background threads
   ├─ Stop performance monitor
   ├─ Stop auto-save timer
   ├─ Clear temporary files
   └─ Release resources

6. Exit:
   ├─ Show shutdown message
   ├─ Log shutdown event
   └─ Exit application
```

---

## Advanced Feedback Loop System

### Real-Time Suggestion Engine

**Suggestion Processing Pipeline:**
```
User types text:

1. Text Buffer Management (500ms debounce)
   └─ Collect keystrokes
   └─ Wait for typing pause
   └─ Trigger analysis on completion

2. Parallel Analysis Tasks:
   ├─ Grammar Analysis (check_grammar_structure)
   │  └─ Runs in thread pool
   │  └─ Checks for issues
   │  └─ Returns results within 100ms
   ├─ Vocabulary Analysis (check_vocabulary)
   │  └─ Runs in thread pool
   │  └─ Queries Words API if available
   │  └─ Returns synonyms/definitions
   └─ Readability Calculation
      └─ Runs in thread pool
      └─ Calculates Flesch score
      └─ Returns grade level

3. Result Aggregation:
   ├─ Combine all analysis results
   ├─ Prioritize issues by severity
   ├─ Rank suggestions by usefulness
   └─ Cache results for future use

4. UI Presentation:
   ├─ Show inline annotations
   ├─ Highlight problematic words
   ├─ Display tooltips on hover
   ├─ Show metric updates
   └─ Emit suggestions to widgets

5. Performance Optimization:
   ├─ Skip redundant calculations
   ├─ Use cached results where possible
   ├─ Prioritize interactive features
   ├─ Defer background tasks
   └─ Limit thread count to 3
```

### Adaptive Feedback Intensity

**User Feedback Preferences:**
```
Settings allow customization:

1. Grammar Checking Level:
   ├─ Off (no checking)
   ├─ Basic (major issues only)
   ├─ Standard (all common issues)
   └─ Strict (all issues, including style)

2. Readability Checking:
   ├─ Off (no checking)
   ├─ Passive (background only)
   ├─ Active (real-time updates)
   └─ Intrusive (suggestions pop-up)

3. Suggestion Frequency:
   ├─ None (no suggestions)
   ├─ Minimal (major issues only)
   ├─ Moderate (standard issues)
   └─ Maximum (all possible suggestions)

4. UI Density:
   ├─ Minimal (status bar only)
   ├─ Normal (standard widget updates)
   └─ Detailed (comprehensive dashboard)
```

### Issue Prioritization System

**Severity Ranking:**
```
1. Critical Issues (Red, highest priority):
   ├─ Broken sentence structure
   ├─ Major grammar errors
   ├─ Inconsistent POV
   └─ Broken narrative continuity

2. Important Issues (Orange, medium priority):
   ├─ Repeated words
   ├─ Long sentences (>30 words)
   ├─ Passive voice overuse
   └─ Unclear pronoun references

3. Minor Issues (Yellow, low priority):
   ├─ Style suggestions
   ├─ Tone inconsistencies
   ├─ Minor readability improvements
   └─ Optional vocabulary upgrades

4. Informational (Blue, lowest priority):
   ├─ Statistics and metrics
   ├─ Progress updates
   ├─ Performance information
   └─ Suggestions for future sessions
```

### Contextual Suggestion System

**Context-Aware Recommendations:**
```
System learns from:

1. Genre-Specific Patterns:
   ├─ Fantasy: Check for world-building consistency
   ├─ Mystery: Track clue placement and pacing
   ├─ Romance: Monitor emotional arc
   ├─ Thriller: Check tension and pacing
   └─ Other genres: Apply genre templates

2. User Writing Style:
   ├─ Average sentence length
   ├─ Preferred vocabulary level
   ├─ Common mistakes
   ├─ Repeated phrases
   └─ Personal preferences

3. Project Context:
   ├─ Target audience affects readability suggestions
   ├─ Genre affects style recommendations
   ├─ Writing style affects tone checks
   └─ Word count goals affect pacing suggestions

4. Current Section:
   ├─ Opening chapters: Check hook quality
   ├─ Middle chapters: Check pacing
   ├─ Climax: Check tension
   ├─ Resolution: Check satisfaction
   └─ Epilogue: Check closure

5. Time of Day:
   ├─ Morning sessions: Fresh suggestions
   ├─ Evening sessions: Focused on refinement
   └─ Based on session history patterns
```

### Learning & Adaptation

**System Learns From:**
```
1. User Acceptance Rate:
   ├─ Track which suggestions user accepts
   ├─ Reduce frequency of rejected suggestions
   ├─ Increase frequency of accepted suggestions
   └─ Adjust suggestion types based on acceptance

2. Writing Progress:
   ├─ Monitor readability improvements
   ├─ Track grammar quality over time
   ├─ Measure project completion progress
   └─ Adjust recommendations based on trajectory

3. User Feedback:
   ├─ "Helpful" button on suggestions
   ├─ "Not helpful" button feedback
   ├─ User ratings of suggestions
   └─ Adjustment of future suggestions

4. Performance Metrics:
   ├─ Time spent implementing suggestions
   ├─ Reversion rate of changes
   ├─ User satisfaction (via surveys)
   └─ Adaptation of future recommendations
```

---

## Multi-Session Feedback Loop

### Session Continuity

**When User Returns:**
```
1. Load previous session context:
   ├─ Last project opened
   ├─ Last cursor position
   ├─ Recent writing goals
   ├─ Current progress toward goals
   └─ Recent issues encountered

2. Present session summary:
   ├─ "You wrote 1,250 words yesterday"
   ├─ "You're 60% through your project"
   ├─ "Your average sentence is 18 words"
   ├─ "Current readability: 72/100"
   └─ "Suggested focus: Reduce repeated words"

3. Resume where left off:
   ├─ Open last project
   ├─ Restore scroll position
   ├─ Show last edited section
   ├─ Highlight recent changes
   └─ Display related suggestions

4. Cross-session suggestions:
   ├─ "You used 'sword' 15 times last session"
   ├─ "Consider varying word choices"
   ├─ "Your pacing slowed in chapter 3"
   ├─ "Try shorter sentences in dialogue"
   └─ "Your readability improved by 8 points!"
```

### Progress Tracking

**Long-Term Analytics:**
```
System maintains 30-day history:

1. Writing Consistency:
   ├─ Words written per day
   ├─ Sessions per week
   ├─ Average session length
   ├─ Most productive times
   └─ Streak tracking

2. Quality Evolution:
   ├─ Readability trend (up/down)
   ├─ Grammar quality trend
   ├─ Repeated words trend
   ├─ Sentence length trend
   └─ Vocabulary complexity trend

3. Project Progress:
   ├─ Days to completion (estimated)
   ├─ Words per day (average)
   ├─ Acceleration/deceleration
   ├─ Milestone achievements
   └─ Deadline tracking

4. Goal Achievement:
   ├─ Daily goal: {words today} / {target}
   ├─ Weekly goal: {words this week} / {target}
   ├─ Monthly goal: {words this month} / {target}
   ├─ Project goal: {words total} / {target}
   └─ Motivation: "You're X% toward your goal!"
```

### Predictive Suggestions

**Forecasting System:**
```
Based on historical patterns:

1. Predict completion date:
   ├─ Current rate: X words/day
   ├─ Days to completion: Y
   ├─ Estimated date: Z
   ├─ Adjust based on recent acceleration
   └─ Account for writing patterns

2. Predict writing quality:
   ├─ Project will likely have readability: X
   ├─ Expected grammar quality: Y
   ├─ Vocabulary level: Z
   ├─ Time needed for editing: X hours
   └─ Suggestion: "Plan for 2-3 editing passes"

3. Predict problem areas:
   ├─ "Chapters 5-7 often have pacing issues"
   ├─ "You tend to overuse 'suddenly' in climax"
   ├─ "Your dialog tags need work"
   ├─ "Consider planning this section carefully"
   └─ Proactive suggestions before problem occurs

4. Predict user needs:
   ├─ "You usually edit after 5k words"
   ├─ "Time for a break? (You've written 2 hours)"
   ├─ "Would you like grammar check now?"
   ├─ "Ready to export? (Nearly at target)"
   └─ Suggestions based on typical patterns
```

---

---

# Project Storage & Organization

## Project File Structure

Each project is organized on disk with a consistent directory structure. When a project is created, a directory is established in the `projects/` folder with the project name.

**Project Directory Layout:**
```
projects/
└── {project_name}/
    ├── content.txt              # Main writing content
    ├── metadata.json            # Project metadata (genre, author, etc.)
    ├── outline.md               # Story outline or chapter breakdown
    ├── characters.json          # Character definitions and relationships
    ├── settings.json            # Project-specific settings
    ├── sessions/                # Historical writing sessions
    │   ├── session_001.json
    │   ├── session_002.json
    │   └── ...
    ├── backups/                 # Project backups
    │   ├── backup_20241101.zip
    │   ├── backup_20241108.zip
    │   └── ...
    └── exports/                 # Exported files
        ├── my_novel.docx
        ├── my_novel.pdf
        └── my_novel.epub
```

**Metadata File Structure:**
The metadata.json contains comprehensive project information including creation date, author name, genre, target word count, writing style preferences, target audience, themes, character list, and any custom metadata the user adds.

**Content Storage:**
The main content is stored as plain text in content.txt. This allows easy version control integration and compatibility with external tools. Line breaks represent paragraph breaks, and special markers can denote chapter breaks or sections.

**Session Tracking:**
Each writing session is recorded as a separate JSON file with start time, end time, words written, and session type (writing/editing/review).

**Backup Strategy:**
Backups are stored as compressed ZIP archives with timestamps. Users can restore from any backup, and automatic backups can be configured to run at regular intervals or before major operations.

## File Locking and Concurrent Access

When a project is open in the application, a lock file is created to prevent multiple instances from editing simultaneously. This prevents data corruption from concurrent writes.

**Lock Mechanism:**
A `.lock` file is created in the project directory containing the process ID and timestamp. If the application crashes, the lock file persists but is detected as stale and removed. This prevents permanent lock situations.

**Read-Only Mode:**
If a project is already open in another instance, the second instance offers to open it in read-only mode, allowing the user to view but not edit the content.

---

# Writing Session Mechanics

## Session Lifecycle

A writing session begins when the user starts typing and ends when the user stops for a configurable period (e.g., 2 minutes) or explicitly ends the session.

**Session Start:**
The application creates a WritingSession record in the database with start time and project ID. An elapsed time counter begins. Word count tracking initializes to the current project word count.

**Active Session:**
As the user types, word count changes are tracked continuously. The application can calculate typing speed, word count delta since session start, and estimated time to reach daily goals. Real-time metrics update the display.

**Session Pause/Resume:**
Users can pause sessions temporarily (for breaks, research, etc.). Paused time doesn't count toward session duration. When resumed, the timer continues from where it paused.

**Session End:**
Sessions end when the user explicitly closes the session or when idle timeout occurs. The end time is recorded, final word count is calculated, and the session is saved to the database. The user sees a session summary showing words written, duration, average speed, and progress toward goals.

## Session Analytics

Each session generates detailed analytics:
- Duration (total time active, excluding pauses)
- Words written in session
- Words per minute (average typing speed)
- Peak productivity period (when most words were written)
- Breaks taken and duration
- Overall focus quality (continuously typing vs. frequent breaks)
- Writing streaks (consecutive sessions without breaks)

This data is stored and used for historical analysis and trend reporting.

---

# Undo/Redo System & Versioning

## Change Tracking & Version History

The system maintains a comprehensive stack of changes to your document, providing powerful versioning capabilities for managing drafts and tracking modifications. Each keystroke or action is recorded with:
- Timestamp of change
- Type of change (insert, delete, replace)
- Content before the change
- Content after the change
- Character position where change occurred
- Line number affected

**Versioning Benefits:**
- **Draft Management:** Track every iteration of your work with complete change history
- **Safe Experimentation:** Try different approaches knowing you can always revert
- **Change Comparison:** Review what changed between versions
- **Recovery:** Restore previous versions if needed

**Change Buffer:**
Not every character is recorded individually, as that would be inefficient. Instead, the system groups changes intelligently:
- Continuous typing is batched as a single insertion
- Cut/paste operations are atomic
- Formatting changes are grouped
- Multiple deletions are combined

**Memory Management:**
The undo stack has a maximum size (e.g., 1000 changes) to prevent consuming excessive memory. Older changes are discarded when the limit is exceeded. Users can clear history if needed.

## Undo/Redo Operations

**Undo Action:**
Pressing Ctrl+Z or clicking Undo reverses the most recent change. The content is restored to its state before the change. Users can undo multiple times to go back further in history.

**Redo Action:**
After undoing, users can redo (Ctrl+Y) to reapply the change. Redo is only available if the user has undone something and hasn't made new changes.

**Undo History Display:**
An undo history panel shows a list of recent changes with descriptions (e.g., "Typed 150 characters", "Deleted selection", "Replaced text"). Clicking a history entry jumps to that point in history.

---

# Keyboard Shortcuts Reference

## Editing Shortcuts
- **Ctrl+A** - Select all text
- **Ctrl+C** - Copy selected text
- **Ctrl+X** - Cut selected text
- **Ctrl+V** - Paste from clipboard
- **Ctrl+Z** - Undo last change
- **Ctrl+Y** - Redo last undone change
- **Ctrl+F** - Find in current document
- **Ctrl+H** - Find and replace
- **Ctrl+Home** - Go to beginning of document
- **Ctrl+End** - Go to end of document
- **Delete** - Delete selected text or character to the right
- **Backspace** - Delete character to the left
- **Tab** - Indent selected text or insert tab
- **Shift+Tab** - Unindent selected text

## File Shortcuts
- **Ctrl+N** - New project
- **Ctrl+O** - Open project
- **Ctrl+S** - Save current project
- **Ctrl+Shift+S** - Save as (save with new name)
- **Ctrl+E** - Export project
- **Ctrl+Q** - Quit application

## Analysis & Tools Shortcuts
- **Ctrl+Alt+A** - Run text analysis
- **Ctrl+Alt+G** - Check grammar
- **Ctrl+Alt+R** - Check readability
- **Ctrl+Alt+C** - Check consistency
- **Ctrl+Alt+S** - Check style

## View & Navigation Shortcuts
- **F11** - Toggle fullscreen
- **Ctrl+Plus** - Zoom in
- **Ctrl+Minus** - Zoom out
- **Ctrl+0** - Reset zoom to default
- **Alt+1** - Switch to Dashboard view
- **Alt+2** - Switch to Projects view
- **Alt+3** - Switch to Analytics view
- **Alt+4** - Switch to Settings view

## Other Shortcuts
- **F1** - Open help documentation
- **Ctrl+Comma** - Open settings
- **Ctrl+,** - Open preferences

---

# Theme System

## Theme Architecture

The application supports multiple appearance themes that affect colors, fonts, icons, and overall visual style.

**Theme Components:**
- Color palette (primary, secondary, accent, text, background)
- Font specifications (family, size, weight)
- Icon style (monochrome, colorful, system icons)
- Border and corner radius styles
- Padding and spacing scales

**Built-in Themes:**
1. **Light Theme** - Bright background with dark text, suitable for daytime use
2. **Dark Theme** - Dark background with light text, suitable for low-light environments
3. **High Contrast Theme** - Maximized contrast for accessibility
4. **System Theme** - Follows the operating system setting (light on Windows/Linux daytime, dark on nighttime)

## Theme Customization

Users can customize any theme through the settings interface. All color values can be changed with a color picker. Font selections come from system-available fonts. Themes are saved as JSON files and loaded on application startup.

**Custom Themes:**
Users can create and save custom themes with their preferred colors and fonts. Themes are stored in a user themes directory and appear in the theme selector alongside built-in themes.

**Theme Inheritance:**
Custom themes inherit from a base theme and only override specific elements. This allows creating light variants of the dark theme or vice versa without needing to customize every single color.

---

# Notification System

## Notification Types

The application uses notifications to alert users about important events:

**Information Notifications:**
- "Project saved successfully"
- "Analysis complete"
- "Export completed" with file location

**Warning Notifications:**
- "You're approaching your daily word goal"
- "API rate limit approaching"
- "Cache size exceeding limit"
- "Unsaved changes exist"

**Error Notifications:**
- "Failed to save project"
- "API request failed"
- "Invalid API key"
- "Database error occurred"

**Success Notifications:**
- "Project created successfully"
- "Settings saved"
- "Backup completed"
- "Export successful"

## Notification Display

Notifications appear as toast messages (small pop-ups) at the bottom-right of the window. They auto-dismiss after 3-5 seconds or when clicked. Important notifications (errors, warnings) require acknowledgment before dismissing.

**Notification History:**
Recent notifications are logged and can be reviewed in a notification history panel. Users can clear the history or search for specific notifications.

---

# Help & Documentation System

## Integrated Help

The Help view provides comprehensive documentation accessible without leaving the application.

**Help Sections:**
- Getting Started guide for new users
- Feature overview describing all major features
- Detailed workflow documentation for the 11-step process
- Text analysis tools guide showing how to use each tool
- Export format guide explaining each export option
- API setup instructions for configuring external APIs
- Keyboard shortcuts reference
- Troubleshooting guide with common problems and solutions
- FAQ section with frequently asked questions

**Context-Sensitive Help:**
Hovering over any setting or control shows a tooltip with brief help text. Users can press F1 while focused on an element for detailed help about that element.

**External Documentation:**
The Help menu includes links to online documentation, video tutorials, and community forums if available.

---

# Security & Privacy

## Overview

AAWT prioritizes the security of your work and the privacy of your data. This section outlines the security measures in place and best practices for protecting your writing projects.

## API Key Storage & Protection

The system stores API keys securely in the settings file with encryption. When displaying keys in the UI, the system masks them, showing only the last 4 characters. Full keys are only visible if you explicitly click "Show".

**Encryption Method:**
The system encrypts keys using your operating system credentials when possible. This ties encryption to your user account, preventing access by other users on the same computer.

**Environment Variable Support (Recommended for Advanced Users):**
You can alternatively store API keys in environment variables (e.g., `AAWT_OPENAI_KEY`), which the application reads instead of using stored keys. This is the recommended approach for deployments where security is critical.

**Best Practices:**
- Never share your API keys with others
- Regularly rotate API keys if you suspect compromise
- Use environment variables for sensitive deployments
- Review API usage regularly to detect unauthorized access

## Data Privacy & Storage

The application stores all your data locally on your computer. No data is sent to external servers except when you explicitly make API calls to language models or external analysis services.

**What Stays Local:**
- All your writing content
- Project files and metadata
- Writing session history
- Settings and preferences
- Cache data and analysis results

**What May Be Sent Externally (Only When You Request It):**
- Text sent to AI services for analysis or generation
- API requests to grammar/readability services
- Optional telemetry (disabled by default)

## User Data Protection

**Telemetry Disabled by Default:**
Optional telemetry can be enabled to help developers improve the application, but it's disabled by default. You can review exactly what data would be sent before enabling it.

**No Automatic Cloud Sync:**
The application doesn't automatically sync data to cloud storage. You must manually export or back up projects if you want to store them elsewhere. This gives you complete control over your data.

**Offline Mode:**
AAWT works fully offline for all core features. API-based features (AI assistance, external grammar checking) require internet connectivity, but all text analysis and editing functions work without internet access.

## Project File Encryption

**Future Enhancement:**
Project-level encryption is planned for a future release, allowing you to password-protect sensitive projects.

## Security Recommendations

- **Keep Backups:** Regularly back up your projects to external storage
- **Update Regularly:** Keep AAWT updated to receive security patches
- **Secure Your Computer:** Use operating system security features (full disk encryption, strong passwords)
- **Review Permissions:** Ensure the application has appropriate file system permissions
- **Monitor API Usage:** Check your API usage dashboard for unexpected activity

---

# Performance & Scalability

## Performance Optimization

AAWT is designed to handle large writing projects efficiently while maintaining responsive performance.

### Text Processing Performance

**Metrics:**
- Processes 10,000-word documents in under 100ms
- Memory usage: ~2-5MB per analysis
- Cached results for repeated texts to avoid redundant processing
- Thread-safe operations allow analysis without blocking the UI

**Optimization Techniques:**
- Debounced analysis (minimum 500ms between updates) prevents overwhelming the system
- Parallel processing for independent analysis tasks
- Query caching reduces database load by over 70% for read-heavy operations
- Connection pooling minimizes database connection overhead

### Database Performance

**Configuration:**
- Write-Ahead Logging (WAL) mode improves concurrent access
- Synchronous mode set to NORMAL balances safety with speed
- Cache size allocation (2000 pages default) for in-memory buffering
- Automatic incremental vacuum cleans up space gradually

**Query Optimization:**
- Appropriate indexes on frequently-queried columns
- Compound indexes for multi-column queries
- Query result caching with 1-hour expiration
- Connection pool size: 5 connections (configurable)

## Scalability Considerations

### Large Projects

**Handling Large Documents:**
- Supports projects with 100,000+ words without performance degradation
- Incremental text analysis processes only changed sections
- Smart caching strategies reduce memory footprint
- Background tasks prevent UI blocking

**Multiple Projects:**
- Efficient project switching with minimal load time
- Shared resource management across projects
- Isolated project data prevents cross-contamination

### Multiple Users

**Current Status:**
AAWT is designed as a single-user desktop application. Each user runs their own instance with separate data.

**Future Enhancement:**
Multi-user collaboration features are planned for future releases (see [Future Enhancements & Roadmap](#future-enhancements--roadmap)).

### Offline Mode & Fallback Behavior

**Offline Capabilities:**
- Core writing and editing functions work completely offline
- Local text analysis (grammar, readability) available without internet
- Project management and session tracking function offline
- Export to all formats works without internet connectivity

**Fallback Behavior:**
- When external APIs are unavailable, the system automatically switches to local analysis
- Built-in algorithms provide grammar and readability scoring
- Cache serves previously analyzed content during outages
- Clear status indicators show when operating in offline mode

### Large Exports

**Export Performance:**
- Asynchronous export processing keeps UI responsive during generation
- Progress indicators show export status for large documents
- Validation ensures generated files are correct before completion
- Compression options reduce file sizes for large projects

## Performance Monitoring

**Real-Time Metrics:**
- CPU usage tracking with color-coded indicators
- Memory usage monitoring with threshold alerts
- Disk I/O performance tracking
- API response time measurement

**Performance Dashboard:**
Available in the Analytics view, showing:
- Database query performance trends
- Cache hit rates over time
- API usage and response times
- Memory usage patterns
- System resource utilization

---

# Accessibility Features

## Overview

AAWT is designed to be accessible to all writers, including those with disabilities. The application follows accessibility best practices and supports assistive technologies.

## Keyboard Navigation

The entire application is navigable using keyboard only. All buttons, menus, and controls respond to keyboard input without requiring a mouse.

**Tab Order:**
- Tab key moves focus through controls in a logical order
- Shift+Tab moves backward through controls
- Arrow keys navigate within menus and lists
- Enter/Space activates buttons and controls

**Keyboard Focus Indicators:**
All focused elements display a clear focus indicator (typically a border or highlight) so you can easily see which control is selected.

**Comprehensive Shortcuts:**
Over 20 keyboard shortcuts provide quick access to common functions (see [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference) for the complete list).

## Screen Reader Support

The application supports screen readers such as NVDA, JAWS, and VoiceOver through proper accessibility labeling of all UI elements.

**Labels and Descriptions:**
- All buttons have accessible names describing their function
- Input fields have associated labels read by screen readers
- Complex elements include detailed descriptions
- Dynamic content updates are announced appropriately

**Semantic Structure:**
The UI structure is logically organized so screen reader users can navigate through related elements efficiently and understand the application hierarchy.

## Visual Accessibility

### High Contrast Mode

The High Contrast theme provides maximum contrast between text and background for users with low vision.

**Color Standards:**
- Colors meet WCAG AAA contrast standards (7:1 ratio minimum)
- Information is never conveyed by color alone
- Icons, text, and other indicators support color choices

### Text Scaling

- Users can increase or decrease font size throughout the application (Ctrl+Plus/Minus)
- Text reflows to accommodate larger sizes without breaking layouts
- UI elements scale proportionally with text size
- Zoom functionality (100%-200%) maintains readability

## Customization Options

**Theme Flexibility:**
- Light, Dark, and High Contrast themes accommodate different visual needs
- Custom color schemes can be created for specific requirements
- Font family and size are fully customizable

**UI Density:**
- Adjustable spacing between elements
- Configurable information density (minimal, normal, detailed)
- Resizable panels and windows

---

# Multi-Language Support

## Internationalization (i18n)

AAWT supports multiple languages through a comprehensive translation system, making the application accessible to writers worldwide.

**Supported Languages:**
- English (default)
- Spanish
- French
- German
- Chinese (Simplified)
- Japanese

**Additional Language Packs:**
Additional languages can be added through community-contributed translation files.

## UI Localization

**Complete Interface Translation:**
- All menus, buttons, and labels are translated
- Dialog boxes and error messages appear in the selected language
- Help documentation is localized where available
- Keyboard shortcuts are adapted for different keyboard layouts

**Language Selection:**
Users select their preferred language in the Settings panel. The interface updates immediately, and the preference persists between sessions.

**Translation System:**
All user-facing text is stored in language files rather than hardcoded in the application. This allows translators to provide text in their native language without modifying code.

## Text Analysis Language Support

**Multi-Language Analysis:**
The text analysis system can process content in multiple languages:
- Readability formulas are adapted for each language to account for linguistic differences
- Language detection is automatic based on the text content
- Users can manually override language selection if needed

**Supported Analysis Languages:**
- English, Spanish, French, German, and other major European languages
- Additional language support planned for future releases

## Right-to-Left Language Support

The application properly handles right-to-left (RTL) languages like Arabic and Hebrew:
- Automatic layout mirroring for RTL languages
- Proper text direction and alignment
- Bidirectional text support for mixed-direction content

---

# Best Practices for Writers

## Structuring Your Workflow with AAWT

To get the most out of AAWT, follow these recommended practices:

### Project Organization

**Start with Planning:**
1. Create a new project with clear goals (target word count, deadline)
2. Fill in the outline.md file with your chapter structure
3. Define main characters in characters.json before you start writing
4. Set your genre and target audience in project settings

**Maintain Consistency:**
- Use the Consistency Check tool regularly to catch character name variations
- Run Text Analysis after completing each chapter
- Review the readability scores to ensure they match your target audience
- Check for repeated words every 5,000 words written

### Writing Session Best Practices

**Establish a Routine:**
- Set daily word count goals in the Settings
- Start a dedicated writing session (Start Writing button) to track your progress
- Take advantage of auto-save—you don't need to manually save constantly
- Use the session analytics to identify your most productive times

**Minimize Distractions:**
- Use fullscreen mode (F11) for focused writing
- Disable or minimize real-time analysis during first drafts if it's distracting
- Review analysis results during editing sessions instead

### Version Management

**Leverage Change Tracking:**
- Don't be afraid to experiment—the undo history lets you revert changes
- Review your change history (Ctrl+Alt+H) to see how your text evolved
- Create manual backups before major revisions or restructuring
- Use the export feature to create milestone snapshots (e.g., "Chapter_3_Draft_1.docx")

**Draft Iterations:**
- Save each major draft as a separate export
- Use naming conventions like "ProjectName_Draft_1", "ProjectName_Draft_2"
- Keep all drafts until you're certain about changes
- Review the Undo History panel to understand what changed between drafts

### Using AI Assistance Effectively

**When to Use AI:**
- Breaking through writer's block (request continuation suggestions)
- Generating alternative phrasings for awkward sentences
- Brainstorming character dialogue options
- Getting unstuck on plot points

**When to Write Manually:**
- Your unique voice and style
- Emotional or pivotal scenes
- Character-defining moments
- Final polishing and refinement

**Cost Management:**
- Monitor your API usage in the Analytics dashboard
- Set budget alerts to avoid unexpected costs
- Use local analysis tools (grammar, readability) which are free
- Cache reduces redundant API calls automatically

### Quality Control Workflow

**Recommended Review Process:**
1. **First Draft:** Write freely without stopping for analysis
2. **Second Pass:** Run Grammar Check and fix major issues
3. **Third Pass:** Run Readability Analysis and adjust for your audience
4. **Fourth Pass:** Run Consistency Check for character/place names
5. **Final Pass:** Style Analysis to ensure tone consistency

**Regular Maintenance:**
- Clear cache weekly to free up disk space (Settings → Performance)
- Review API usage monthly to understand costs
- Back up projects weekly to external storage
- Archive completed projects to keep the interface clean

### Export Strategy

**During Development:**
- Export to TXT or Markdown for version control systems
- Keep milestone exports as you complete major sections

**For Sharing:**
- Export to DOCX for editors and beta readers
- Export to PDF for agents or publishers
- Export to EPUB for e-reader testing

**For Backup:**
- Export to JSON to preserve all metadata and structure
- Keep backups on external drives or cloud storage (manually)

---

# Future Enhancements & Roadmap

## Planned Features

AAWT is under active development. Here are some features planned for future releases:

### Version Control Integration

**Git Integration:**
- Built-in Git support for professional version control
- Automatic commits on significant changes
- Branch-based draft management
- Diff visualization for comparing versions

### Collaboration Features

**Multi-User Support:**
- Real-time collaborative editing for co-authors
- Comments and annotations system
- Track changes with author attribution
- Share projects securely with editors or beta readers
- Role-based permissions (author, editor, viewer)

**Note:** Until collaboration features are implemented, AAWT remains a single-user application. Users can manually share exported files for feedback.

### Cloud Sync & Mobile

**Cloud Integration:**
- Optional cloud backup and sync (encrypted)
- Access projects across multiple computers
- Mobile companion app for on-the-go note-taking and drafting
- Automatic conflict resolution for multi-device editing

**Privacy:** Cloud sync will be optional and use end-to-end encryption

### Advanced AI Features

**Enhanced AI Capabilities:**
- Fine-tuning AI models on your writing style
- Genre-specific writing assistants
- Plot consistency checker using AI
- Character voice differentiation analysis
- Automatic chapter summarization

### Plugin Architecture

**Extensibility:**
- Plugin system for community-developed extensions
- Custom export format support
- Third-party API integrations
- Custom analysis tools

### Enhanced Analytics

**Writing Insights:**
- Predictive completion date based on writing patterns
- Mood and tone analysis over time
- Character development tracking
- Plot pacing visualization
- Comparison with published works in your genre

### Project Templates

**Quick Start Templates:**
- Genre-specific project templates
- Pre-built character sheets
- Plot structure templates
- World-building frameworks

### Integration with "Everything App"

As part of a larger ecosystem, AAWT may integrate with other productivity tools in the future, enabling seamless workflows across writing, research, and publication tasks.

## Community Contributions

We welcome community contributions! If you'd like to suggest features, report bugs, or contribute code, please visit our GitHub repository.

---

# Troubleshooting & Support

## Common Issues and Solutions

**Application Won't Start:**
- Check Python version (3.7+)
- Verify PyQt5 is installed
- Check for corrupted configuration files
- Try deleting the config directory and restarting

**Text Analysis Tools Not Working:**
- Verify API keys are configured correctly
- Check internet connection
- Ensure API services are not down
- Try the fallback offline analysis

**Slow Performance:**
- Clear cache in settings
- Reduce connection pool size
- Enable memory optimization
- Close other applications
- Check disk space (at least 1GB free recommended)

**Projects Won't Load:**
- Check project file isn't corrupted
- Try restoring from a backup
- Check file permissions
- Ensure project directory isn't read-only

**Export Failing:**
- Verify export directory exists and is writable
- Check available disk space
- Try different export format
- Ensure required libraries are installed (python-docx, reportlab, etc.)

**API Errors:**
- Verify API key is valid
- Check account has sufficient credits
- Ensure API service is not down
- Try a different API provider

**Settings Not Saving:**
- Check config directory is writable
- Verify sufficient disk space
- Try resetting settings to defaults
- Check file isn't locked by another process

## Debug Mode

Debug mode provides detailed logging and additional information for troubleshooting.

**Enabling Debug Mode:**
In the Advanced settings tab, enable "Debug Mode". This activates detailed logging to the application log file.

**Log File Location:**
The system stores logs in `logs/aawt.log`. Each session creates a timestamped entry. Old logs are automatically rotated and archived.

**Debug Output:**
Debug mode enables extra information display in the UI, expanded error messages, and performance profiling.

---

# Data Flow Architecture

## User Input Processing

User input (typing, button clicks, menu selections) is captured by the UI layer. The input is validated and converted to application commands. These commands are dispatched to the appropriate system module (API manager, database, text analyzer, etc.).

**Processing Pipeline:**
Input → Validation → Command Creation → System Processing → Data Storage → UI Update

## Data Storage and Retrieval

When data is modified (project content, settings, session data), it's processed through the database manager. The manager uses connection pooling to efficiently handle database operations. Results are cached to avoid redundant queries. The cache is invalidated when data changes.

**Query Optimization:**
Related data is fetched together to minimize database roundtrips. Indexes ensure common queries execute quickly. Batch operations reduce overhead.

## Real-Time Updates

Metrics and analytics update in real-time as the user types. Text analysis runs continuously but is debounced to avoid overwhelming the system. Updates are sent to the UI which refreshes displays.

**Update Frequency:**
- Metrics: Every 1-2 seconds
- Text analysis: Every 500ms (debounced)
- Performance stats: Every 1-2 seconds
- Analytics dashboard: Every 5 seconds

## Export Processing

When exporting, content is retrieved from the database, formatted according to the selected format, validated, then written to disk. Large exports are done asynchronously to keep the UI responsive.

---

# Summary

AAWT is a comprehensive, production-ready writing application featuring:

- **1,000+ components** across multiple systems
- **8,700+ lines** of GUI code alone
- **Integrated text analysis** with 5 specialized tools
- **Multi-API support** with intelligent caching
- **6 export formats** with validation
- **Persistent storage** with connection pooling
- **Real-time monitoring** and analytics
- **Responsive UI** with dark/light themes
- **Version control** with comprehensive change tracking
- **Extensible architecture** for future enhancements
- **Robust error handling** and logging
- **Full accessibility** support

The application combines a modern PyQt5 interface with powerful backend systems to create a comprehensive writing assistant for authors working on fiction, fantasy, and world-building projects.

---

# Technical Reference

This appendix provides detailed technical information for developers and advanced users.

## Database System

### Database Architecture Overview

The database system provides persistent storage for all application data, project information, writing sessions, API usage, and analytics. It uses SQLite with connection pooling for concurrent access, fast queries, and reliable data integrity.

### Database Manager System

#### Core Responsibilities

The database manager handles all interactions with the underlying SQLite database:
- Connection lifecycle management (creation, validation, reuse, cleanup)
- Connection pool size optimization based on application load
- Automatic reconnection on connection failures
- Query timeout enforcement to prevent hanging queries
- Health check monitoring to detect stale connections
- Transaction management with automatic rollback on errors
- Performance statistics collection and reporting

#### Connection Pooling Strategy

The system maintains a pool of pre-established connections rather than creating a new database connection for each query. This dramatically improves performance since connection creation is expensive.

**Pool Configuration:**
- Default pool size: 5 connections
- Maximum connection limit prevents resource exhaustion
- Connection timeout: 30 seconds (default)
- Idle connection cleanup removes unused connections after a period of inactivity
- Health monitoring thread periodically tests connections in the pool
- Automatic growth when all connections are in use (up to maximum)

#### Query Cache System

The query cache stores results of frequently-run queries so they don't need to be re-executed. Queries with identical parameters return cached results instead of hitting the database.

**Cache Configuration:**
- Cache key generated from query text and parameters
- Cached entries expire after 1 hour (configurable by query type)
- Cache invalidation on data modifications
- Cache hit rates often exceed 70% for read-heavy operations

### Database Schema

#### Projects Table

Stores information about each writing project.

**Fields:**
- `id` (Integer, Primary Key): Unique identifier
- `name` (Text, Unique): Project name
- `created_date` (Text): ISO 8601 timestamp of creation
- `last_modified` (Text): ISO 8601 timestamp of most recent change
- `status` (Text): Current state ("active", "paused", "completed")
- `settings` (Text, JSON): Project-specific settings
- `word_count` (Integer): Current total word count
- `target_words` (Integer): Target word count goal
- `metadata` (Text, JSON): Additional project information

**Indexes:**
- Primary key on `id`
- Unique constraint on `name`
- Recommended index on `created_date` and `status`

#### API Usage Table

Tracks every API call for analytics, cost calculation, and performance monitoring.

**Fields:**
- `id` (Integer, Primary Key): Unique identifier
- `project_id` (Integer, Foreign Key): Associated project
- `api_type` (Text): API called ("openai", "anthropic", "google", "huggingface")
- `endpoint` (Text): Specific API endpoint
- `response_time` (Float): Call duration in seconds
- `success` (Boolean): Whether call succeeded
- `status_code` (Integer): HTTP status code
- `error_message` (Text): Error description if failed
- `tokens_used` (Integer): Tokens consumed
- `cost` (Float): Calculated cost in dollars
- `timestamp` (Text): ISO 8601 timestamp
- `request_hash` (Text): Hash for deduplication

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id`
- Compound index on (`api_type`, `timestamp`)
- Index on `timestamp`
- Index on `success`

#### Content Cache Table

Stores cached analysis results and API responses.

**Fields:**
- `id` (Integer, Primary Key): Unique identifier
- `project_id` (Integer, Foreign Key): Associated project
- `content_type` (Text): Type ("analysis", "api_response", "readability")
- `content_key` (Text): Identifying key
- `content_value` (Text/BLOB): Cached data (typically JSON)
- `content_hash` (Text): Hash for integrity checking
- `created_date` (Text): ISO 8601 timestamp of caching
- `expires_date` (Text): ISO 8601 timestamp of expiration
- `access_count` (Integer): Usage count
- `last_accessed` (Text): ISO 8601 timestamp of last use

**Unique Constraint:**
- Compound unique on (`project_id`, `content_type`, `content_key`)

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id`
- Index on `expires_date`
- Index on (`content_type`, `content_key`)

#### Writing Sessions Table

Records each writing session for analytics.

**Fields:**
- `id` (Integer, Primary Key): Unique identifier
- `project_id` (Integer, Foreign Key): Associated project
- `start_time` (Text): ISO 8601 timestamp of session start
- `end_time` (Text): ISO 8601 timestamp of session end
- `words_written` (Integer): Words written during session
- `session_type` (Text): Type ("writing", "editing", "review")

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id`
- Index on (`project_id`, `start_time`)

#### Change History Table

Tracks all modifications for undo functionality.

**Fields:**
- `id` (Integer, Primary Key): Unique identifier
- `project_id` (Integer, Foreign Key): Associated project
- `change_type` (Text): "insert", "delete", or "replace"
- `content_before` (Text): Content before change
- `content_after` (Text): Content after change
- `timestamp` (Text): When change was made
- `character_position` (Integer): Position in document
- `line_number` (Integer): Affected line number

### Database Configuration

**PRAGMA Settings:**
- Foreign key enforcement enabled
- Write-Ahead Logging (WAL) mode for concurrent access
- Synchronous mode: NORMAL (balances safety with speed)
- Cache size: 2000 pages (in-memory buffering)
- Temporary storage: memory
- Automatic incremental vacuum

## Data Flow Architecture

### User Input Processing

User input flows through a structured pipeline:

**Pipeline:**
Input → Validation → Command Creation → System Processing → Data Storage → UI Update

### Data Storage and Retrieval

The system processes data modifications through the database manager, uses connection pooling for efficiency, caches results to avoid redundant queries, and invalidates cache when data changes.

**Query Optimization:**
- Related data fetched together to minimize roundtrips
- Indexes ensure common queries execute quickly
- Batch operations reduce overhead

### Real-Time Updates

**Update Frequency:**
- Metrics: Every 1-2 seconds
- Text analysis: Every 500ms (debounced)
- Performance stats: Every 1-2 seconds
- Analytics dashboard: Every 5 seconds

### Export Processing

The system retrieves content from the database, formats it according to the selected format, validates the output, then writes to disk. Large exports are processed asynchronously to keep the UI responsive.

---

**End of Documentation**
