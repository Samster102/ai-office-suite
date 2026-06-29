from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QLabel, QSpinBox
)
from PyQt6.QtCore import Qt

from ai_office_suite.ai.ai_engine import AIEngine
from ai_office_suite.utils.config_manager import ConfigManager
from ai_office_suite.models.spreadsheet import Spreadsheet


class SpreadsheetEditor(QWidget):
    """Spreadsheet editor widget."""
    
    def __init__(self, ai_engine: AIEngine, config: ConfigManager):
        """Initialize spreadsheet editor.
        
        Args:
            ai_engine: AI engine instance
            config: Configuration manager
        """
        super().__init__()
        self.ai_engine = ai_engine
        self.config = config
        self.spreadsheet = Spreadsheet("New Spreadsheet")
        self.setup_ui()
    
    def setup_ui(self):
        """Setup spreadsheet editor UI."""
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar_layout = QHBoxLayout()
        
        add_row_btn = QPushButton("+ Add Row")
        add_row_btn.clicked.connect(self.add_row)
        toolbar_layout.addWidget(add_row_btn)
        
        add_col_btn = QPushButton("+ Add Column")
        add_col_btn.clicked.connect(self.add_column)
        toolbar_layout.addWidget(add_col_btn)
        
        ai_analyze_btn = QPushButton("🧠 AI Analysis")
        ai_analyze_btn.clicked.connect(self.ai_analyze)
        toolbar_layout.addWidget(ai_analyze_btn)
        
        ai_insights_btn = QPushButton("💡 Get Insights")
        ai_insights_btn.clicked.connect(self.ai_get_insights)
        toolbar_layout.addWidget(ai_insights_btn)
        
        toolbar_layout.addStretch()
        layout.addLayout(toolbar_layout)
        
        # Table widget
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels([f"Col {i}" for i in range(1, 6)])
        layout.addWidget(self.table)
        
        # Status label
        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
    
    def add_row(self):
        """Add new row to spreadsheet."""
        self.table.insertRow(self.table.rowCount())
        self.status_label.setText("Row added")
    
    def add_column(self):
        """Add new column to spreadsheet."""
        self.table.insertColumn(self.table.columnCount())
        col_num = self.table.columnCount()
        self.table.setHorizontalHeaderItem(col_num - 1, QTableWidgetItem(f"Col {col_num}"))
        self.status_label.setText("Column added")
    
    def get_table_data(self):
        """Get data from table."""
        data = []
        # Add headers
        headers = []
        for col in range(self.table.columnCount()):
            item = self.table.horizontalHeaderItem(col)
            headers.append(item.text() if item else f"Col {col + 1}")
        data.append(headers)
        
        # Add rows
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        
        return data
    
    def ai_analyze(self):
        """Analyze spreadsheet with AI."""
        from ai_office_suite.ai.data_analyzer import DataAnalyzer
        
        data = self.get_table_data()
        analyzer = DataAnalyzer(self.ai_engine)
        analysis = analyzer.analyze_data(data)
        
        self.status_label.setText(f"Analysis: {analysis['shape']} - Rows: {analysis['shape'][0]}, Cols: {analysis['shape'][1]}")
    
    def ai_get_insights(self):
        """Get AI insights from spreadsheet."""
        from ai_office_suite.ai.data_analyzer import DataAnalyzer
        
        data = self.get_table_data()
        analyzer = DataAnalyzer(self.ai_engine)
        insights = analyzer.get_insights(data)
        
        self.status_label.setText(f"Insights generated: {len(insights)} characters")
