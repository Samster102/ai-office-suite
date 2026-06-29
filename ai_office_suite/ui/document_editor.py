from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton,
    QComboBox, QLabel, QFontComboBox, QSpinBox, QToolBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QTextCursor, QTextCharFormat, QColor

from ai_office_suite.ai.ai_engine import AIEngine
from ai_office_suite.utils.config_manager import ConfigManager


class DocumentEditor(QWidget):
    """Document editor widget with rich text editing."""
    
    def __init__(self, ai_engine: AIEngine, config: ConfigManager):
        """Initialize document editor.
        
        Args:
            ai_engine: AI engine instance
            config: Configuration manager
        """
        super().__init__()
        self.ai_engine = ai_engine
        self.config = config
        self.setup_ui()
    
    def setup_ui(self):
        """Setup document editor UI."""
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar_layout = QHBoxLayout()
        
        # Font selector
        font_label = QLabel("Font:")
        self.font_combo = QFontComboBox()
        toolbar_layout.addWidget(font_label)
        toolbar_layout.addWidget(self.font_combo)
        
        # Font size
        size_label = QLabel("Size:")
        self.size_spin = QSpinBox()
        self.size_spin.setMinimum(8)
        self.size_spin.setMaximum(72)
        self.size_spin.setValue(12)
        toolbar_layout.addWidget(size_label)
        toolbar_layout.addWidget(self.size_spin)
        
        # Bold button
        self.bold_btn = QPushButton("B")
        self.bold_btn.setCheckable(True)
        self.bold_btn.clicked.connect(self.toggle_bold)
        toolbar_layout.addWidget(self.bold_btn)
        
        # Italic button
        self.italic_btn = QPushButton("I")
        self.italic_btn.setCheckable(True)
        self.italic_btn.clicked.connect(self.toggle_italic)
        toolbar_layout.addWidget(self.italic_btn)
        
        # AI buttons
        ai_improve_btn = QPushButton("✨ Improve")
        ai_improve_btn.clicked.connect(self.ai_improve)
        toolbar_layout.addWidget(ai_improve_btn)
        
        ai_summarize_btn = QPushButton("📝 Summarize")
        ai_summarize_btn.clicked.connect(self.ai_summarize)
        toolbar_layout.addWidget(ai_summarize_btn)
        
        toolbar_layout.addStretch()
        layout.addLayout(toolbar_layout)
        
        # Text editor
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Start typing your document here...")
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)
    
    def toggle_bold(self):
        """Toggle bold formatting."""
        fmt = self.text_edit.currentCharFormat()
        fmt.setFontWeight(700 if not self.bold_btn.isChecked() else 400)
        self.text_edit.setCurrentCharFormat(fmt)
    
    def toggle_italic(self):
        """Toggle italic formatting."""
        fmt = self.text_edit.currentCharFormat()
        fmt.setFontItalic(not self.italic_btn.isChecked())
        self.text_edit.setCurrentCharFormat(fmt)
    
    def ai_improve(self):
        """Improve text using AI."""
        text = self.text_edit.toPlainText()
        if text:
            improved = self.ai_engine.improve_writing(text)
            self.text_edit.setPlainText(improved)
    
    def ai_summarize(self):
        """Summarize text using AI."""
        text = self.text_edit.toPlainText()
        if text:
            summary = self.ai_engine.summarize_text(text)
            self.text_edit.setPlainText(summary)
    
    def get_content(self) -> str:
        """Get document content."""
        return self.text_edit.toPlainText()
    
    def set_content(self, content: str) -> None:
        """Set document content."""
        self.text_edit.setPlainText(content)
