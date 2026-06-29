# AI Office Suite - Desktop Application

A powerful desktop application combining Word, PowerPoint, and Excel features with advanced AI capabilities.

## Features

### Document Editor (Word-like)
- Rich text editing with formatting options
- Font, size, color, alignment controls
- Headers, bullets, numbering
- Image and table insertion

### Presentation Builder (PowerPoint-like)
- Multiple slide management
- Slide templates and themes
- Text, image, and shape insertion
- Transitions and animations

### Spreadsheet (Excel-like)
- Grid-based data entry
- Formula support
- Cell formatting
- Data sorting and filtering

### AI Features
- **AI Writing Assistant**: Auto-complete, grammar checking, tone adjustment
- **Content Generation**: Generate text, summaries, and ideas
- **Data Analysis**: Analyze spreadsheet data with AI insights
- **Smart Formatting**: Automatic styling suggestions
- **Chart Generation**: Create visualizations from data
- **Translation**: Multi-language support

## Tech Stack

- **GUI Framework**: PyQt6
- **Rich Text Editing**: QTextEdit, QPlainTextEdit
- **Spreadsheet**: QTableWidget
- **Graphics**: QGraphicsView for presentations
- **AI Integration**: OpenAI API (configurable)
- **Data**: Pandas, NumPy
- **Storage**: JSON, SQLite

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Samster102/ai-office-suite.git
cd ai-office-suite
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure AI API:
```bash
cp config.example.json config.json
# Edit config.json with your OpenAI API key
```

5. Run the application:
```bash
python main.py
```

## Project Structure

```
ai-office-suite/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── config.json            # Configuration file
├── ai_office_suite/
│   ├── __init__.py
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── document_editor.py
│   │   ├── presentation_builder.py
│   │   ├── spreadsheet_editor.py
│   │   └── styles.qss
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── ai_engine.py
│   │   ├── text_assistant.py
│   │   └── data_analyzer.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── document_manager.py
│   │   ├── presentation_manager.py
│   │   └── spreadsheet_manager.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_handler.py
│   │   └── config_manager.py
│   └── models/
│       ├── __init__.py
│       ├── document.py
│       ├── presentation.py
│       └── spreadsheet.py
└── resources/
    ├── icons/
    └── templates/
```

## Configuration

Edit `config.json`:

```json
{
  "ai": {
    "provider": "openai",
    "api_key": "your-api-key-here",
    "model": "gpt-4"
  },
  "app": {
    "theme": "dark",
    "auto_save": true,
    "auto_save_interval": 60
  }
}
```

## Usage

### Document Editor
1. Click "New Document" or File → New
2. Start typing with rich formatting options
3. Use AI toolbar for writing assistance

### Presentation Builder
1. Click "New Presentation"
2. Add slides with layouts
3. Insert text, images, shapes
4. Apply transitions and animations

### Spreadsheet
1. Click "New Spreadsheet"
2. Enter data and formulas
3. Use AI analysis for insights
4. Generate charts automatically

## AI Features Usage

### Writing Assistant
```python
from ai_office_suite.ai import AIEngine

ai = AIEngine()
print(ai.improve_writing("Your text here"))
print(ai.summarize_text("Long text here"))
```

### Data Analysis
```python
from ai_office_suite.ai import DataAnalyzer

analyzer = DataAnalyzer()
insights = analyzer.get_insights(data)
```

## Keyboard Shortcuts

- `Ctrl+N` - New document
- `Ctrl+O` - Open file
- `Ctrl+S` - Save
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+A` - Select All
- `Ctrl+B` - Bold
- `Ctrl+I` - Italic
- `Ctrl+U` - Underline
- `Alt+A` - AI Assistant Menu

## Future Enhancements

- [ ] Collaboration features
- [ ] Cloud sync
- [ ] Advanced charting
- [ ] Custom templates
- [ ] Macro support
- [ ] PDF export
- [ ] Real-time collaboration
- [ ] More AI models integration

## License

MIT License

## Support

For issues and feature requests, please create an issue in the repository.

## Contributing

Contributions are welcome! Please follow the code style and submit pull requests.
