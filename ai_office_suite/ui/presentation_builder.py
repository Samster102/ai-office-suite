from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget,
    QListWidgetItem, QTextEdit, QLabel, QSpinBox
)
from PyQt6.QtCore import Qt

from ai_office_suite.ai.ai_engine import AIEngine
from ai_office_suite.utils.config_manager import ConfigManager
from ai_office_suite.models.presentation import Presentation, Slide


class PresentationBuilder(QWidget):
    """Presentation builder widget."""
    
    def __init__(self, ai_engine: AIEngine, config: ConfigManager):
        """Initialize presentation builder.
        
        Args:
            ai_engine: AI engine instance
            config: Configuration manager
        """
        super().__init__()
        self.ai_engine = ai_engine
        self.config = config
        self.presentation = Presentation("New Presentation")
        self.setup_ui()
    
    def setup_ui(self):
        """Setup presentation builder UI."""
        layout = QHBoxLayout()
        
        # Left panel - Slide list
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Slides:"))
        
        self.slides_list = QListWidget()
        self.slides_list.itemClicked.connect(self.on_slide_selected)
        left_layout.addWidget(self.slides_list)
        
        # Slide buttons
        btn_layout = QHBoxLayout()
        add_slide_btn = QPushButton("+ Add Slide")
        add_slide_btn.clicked.connect(self.add_slide)
        btn_layout.addWidget(add_slide_btn)
        
        remove_slide_btn = QPushButton("- Remove")
        remove_slide_btn.clicked.connect(self.remove_slide)
        btn_layout.addWidget(remove_slide_btn)
        
        left_layout.addLayout(btn_layout)
        
        # Right panel - Slide editor
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Slide Title:"))
        
        self.title_edit = QTextEdit()
        self.title_edit.setMaximumHeight(60)
        right_layout.addWidget(self.title_edit)
        
        right_layout.addWidget(QLabel("Slide Content:"))
        self.content_edit = QTextEdit()
        right_layout.addWidget(self.content_edit)
        
        # AI buttons
        ai_layout = QHBoxLayout()
        ai_gen_btn = QPushButton("✨ Generate Content")
        ai_gen_btn.clicked.connect(self.ai_generate_content)
        ai_layout.addWidget(ai_gen_btn)
        
        save_slide_btn = QPushButton("💾 Save Slide")
        save_slide_btn.clicked.connect(self.save_current_slide)
        ai_layout.addWidget(save_slide_btn)
        
        right_layout.addLayout(ai_layout)
        
        # Combine layouts
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        left_widget.setMaximumWidth(200)
        
        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        
        layout.addWidget(left_widget)
        layout.addWidget(right_widget)
        self.setLayout(layout)
        
        # Add initial slide
        self.add_slide()
    
    def add_slide(self):
        """Add new slide."""
        slide = Slide(f"Slide {self.presentation.get_slide_count() + 1}", "")
        idx = self.presentation.add_slide(slide)
        item = QListWidgetItem(f"Slide {idx + 1}")
        self.slides_list.addItem(item)
        self.slides_list.setCurrentItem(item)
    
    def remove_slide(self):
        """Remove current slide."""
        current_row = self.slides_list.currentRow()
        if current_row >= 0:
            self.presentation.remove_slide(current_row)
            self.slides_list.takeItem(current_row)
    
    def on_slide_selected(self, item):
        """Handle slide selection."""
        current_row = self.slides_list.row(item)
        if current_row >= 0 and current_row < len(self.presentation.slides):
            slide = self.presentation.slides[current_row]
            self.title_edit.setPlainText(slide.title)
            self.content_edit.setPlainText(slide.content)
    
    def save_current_slide(self):
        """Save current slide content."""
        current_row = self.slides_list.currentRow()
        if current_row >= 0 and current_row < len(self.presentation.slides):
            slide = self.presentation.slides[current_row]
            slide.title = self.title_edit.toPlainText()
            slide.content = self.content_edit.toPlainText()
    
    def ai_generate_content(self):
        """Generate slide content using AI."""
        title = self.title_edit.toPlainText()
        if title:
            content = self.ai_engine.generate_ideas(title, count=3)
            self.content_edit.setPlainText(content)
