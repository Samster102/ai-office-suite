import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QMenuBar, QMenu, QToolBar, QStatusBar, QMessageBox, QFileDialog
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon

from ai_office_suite.utils.config_manager import ConfigManager
from ai_office_suite.ai.ai_engine import AIEngine
from .document_editor import DocumentEditor
from .presentation_builder import PresentationBuilder
from .spreadsheet_editor import SpreadsheetEditor


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.config = ConfigManager()
        self.ai_engine = AIEngine(self.config)
        self.setup_ui()
        self.setup_menus()
        self.setup_toolbar()
    
    def setup_ui(self):
        """Setup user interface."""
        # Window settings
        self.setWindowTitle("AI Office Suite - Document & Presentation Editor")
        app_config = self.config.get_app_config()
        self.setGeometry(100, 100, app_config.get('window_width', 1400), 
                        app_config.get('window_height', 900))
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Tab widget
        self.tabs = QTabWidget()
        self.document_editor = DocumentEditor(self.ai_engine, self.config)
        self.presentation_builder = PresentationBuilder(self.ai_engine, self.config)
        self.spreadsheet_editor = SpreadsheetEditor(self.ai_engine, self.config)
        
        self.tabs.addTab(self.document_editor, "📄 Document")
        self.tabs.addTab(self.presentation_builder, "📊 Presentation")
        self.tabs.addTab(self.spreadsheet_editor, "📈 Spreadsheet")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        central_widget.setLayout(layout)
        
        # Status bar
        self.statusBar().showMessage("Ready")
    
    def setup_menus(self):
        """Setup application menus."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        new_action = QAction("New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        file_menu.addSeparator()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        edit_menu.addAction(redo_action)
        
        # AI menu
        ai_menu = menubar.addMenu("AI")
        assist_action = QAction("AI Assistant", self)
        assist_action.setShortcut("Alt+A")
        assist_action.triggered.connect(self.show_ai_assistant)
        ai_menu.addAction(assist_action)
        
        improve_action = QAction("Improve Writing", self)
        improve_action.triggered.connect(self.improve_writing)
        ai_menu.addAction(improve_action)
        
        summarize_action = QAction("Summarize", self)
        summarize_action.triggered.connect(self.summarize_text)
        ai_menu.addAction(summarize_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_toolbar(self):
        """Setup application toolbar."""
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # Add toolbar actions
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)
        
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)
        
        toolbar.addSeparator()
        
        ai_action = QAction("AI Helper", self)
        ai_action.triggered.connect(self.show_ai_assistant)
        toolbar.addAction(ai_action)
    
    def new_file(self):
        """Create new file."""
        self.statusBar().showMessage("New file created")
    
    def open_file(self):
        """Open file dialog."""
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                   "All Files (*);;Text Files (*.txt);;Word Files (*.docx)")
        if filename:
            self.statusBar().showMessage(f"Opened: {filename}")
    
    def save_file(self):
        """Save file dialog."""
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                   "Text Files (*.txt);;Word Files (*.docx)")
        if filename:
            self.statusBar().showMessage(f"Saved: {filename}")
    
    def show_ai_assistant(self):
        """Show AI assistant dialog."""
        QMessageBox.information(self, "AI Assistant", 
                               "AI Assistant is ready to help!\n\nSelect text and use AI menu options.")
    
    def improve_writing(self):
        """Improve writing of selected text."""
        self.statusBar().showMessage("Improving writing...")
    
    def summarize_text(self):
        """Summarize selected text."""
        self.statusBar().showMessage("Summarizing text...")
    
    def show_about(self):
        """Show about dialog."""
        QMessageBox.about(self, "About AI Office Suite",
                         "AI Office Suite v1.0\n\n"
                         "A powerful desktop application combining Word, PowerPoint, and Excel "
                         "with advanced AI capabilities.\n\n"
                         "Features:\n"
                         "• Rich Text Document Editor\n"
                         "• Presentation Builder\n"
                         "• Spreadsheet Editor\n"
                         "• AI Writing Assistant\n"
                         "• Data Analysis with AI")
