#!/usr/bin/env python3
"""
AAWT - AI-Assisted Writing Tool
Main application entry point.

A comprehensive desktop application for writers with real-time analysis,
project management, AI integration, and multi-format export capabilities.
"""

import sys
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/aawt.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Ensure logs directory exists
Path('logs').mkdir(exist_ok=True)

def main():
    """Main application entry point."""
    try:
        logger.info("="*60)
        logger.info("Starting AAWT - AI-Assisted Writing Tool")
        logger.info("="*60)
        
        # Import PyQt5
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtCore import Qt
        
        # Import application components
        from src.database.database_manager import DatabaseManager
        from src.system.settings_manager import SettingsManager
        from src.system.api_manager import APIManager
        from src.system.export_manager import ExportManager
        from src.system.file_operations import FileOperations
        from src.system.automated_workflow import WorkflowManager
        from src.system.text_analyzers import GrammarAnalyzer
        from src.text.text_processing import TextAnalyzer
        from src.ui.main_window import MainWindow
        
        # Initialize application
        app = QApplication(sys.argv)
        app.setApplicationName("AAWT")
        app.setOrganizationName("AAWT")
        app.setApplicationVersion("2.0")
        
        # Enable high DPI scaling
        try:
            app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
            app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        except:
            pass
        
        logger.info("Initializing application components...")
        
        # Initialize managers
        settings_manager = SettingsManager('config/user_settings.json')
        database_path = settings_manager.get('advanced.database_path', 'config/aawt.db')
        pool_size = settings_manager.get('performance.connection_pool_size', 5)
        
        database_manager = DatabaseManager(database_path, pool_size)
        text_analyzer = TextAnalyzer()
        grammar_analyzer = GrammarAnalyzer(settings_manager)
        export_manager = ExportManager(settings_manager)
        file_operations = FileOperations('projects')
        api_manager = APIManager(settings_manager, database_manager)
        workflow_manager = WorkflowManager(database_manager, api_manager, settings_manager)
        
        logger.info("All components initialized successfully")
        
        # Create and show main window
        window = MainWindow(
            settings_manager,
            database_manager,
            api_manager,
            text_analyzer,
            export_manager,
            file_operations,
            workflow_manager,
            grammar_analyzer
        )
        
        window.show()
        
        logger.info("Application window displayed")
        logger.info("Application ready")
        
        # Run application
        exit_code = app.exec_()
        
        logger.info("Application closing...")
        logger.info(f"Exit code: {exit_code}")
        
        return exit_code
        
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        
        # Try to show error dialog
        try:
            from PyQt5.QtWidgets import QApplication, QMessageBox
            if not QApplication.instance():
                app = QApplication(sys.argv)
            
            QMessageBox.critical(
                None,
                "Fatal Error",
                f"AAWT encountered a fatal error and must close:\n\n{str(e)}\n\nPlease check the log file for details."
            )
        except:
            print(f"Fatal error: {e}")
        
        return 1


if __name__ == '__main__':
    sys.exit(main())
