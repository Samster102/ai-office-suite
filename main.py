#!/usr/bin/env python3
"""
AI Office Suite - Main Application Entry Point

A powerful desktop application combining Word, PowerPoint, and Excel
with advanced AI capabilities.
"""

import sys
from PyQt6.QtWidgets import QApplication

from ai_office_suite.ui.main_window import MainWindow


def main():
    """Main application entry point."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
