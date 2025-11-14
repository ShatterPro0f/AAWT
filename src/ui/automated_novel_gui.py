"""
Automated Novel Workflow GUI
Provides interface for the 11-step automated writing process.
"""

import logging
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTextEdit, QProgressBar, QListWidget, QGroupBox, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

logger = logging.getLogger(__name__)


class AutomatedNovelGUI(QWidget):
    """GUI for automated novel writing workflow."""
    
    def __init__(self, workflow_manager):
        """
        Initialize automated novel GUI.
        
        Args:
            workflow_manager: WorkflowManager instance
        """
        super().__init__()
        
        self.workflow = workflow_manager
        self.update_timer = None
        
        self.init_ui()
        
        logger.info("Automated Novel GUI initialized")
    
    def init_ui(self):
        """Initialize user interface."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Automated Novel Workflow")
        title.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)
        
        # Progress section
        progress_group = QGroupBox("Workflow Progress")
        progress_layout = QVBoxLayout()
        
        self.progress_label = QLabel("Workflow not started")
        self.progress_label.setStyleSheet("font-size: 14px; padding: 5px;")
        progress_layout.addWidget(self.progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        progress_layout.addWidget(self.progress_bar)
        
        progress_group.setLayout(progress_layout)
        layout.addWidget(progress_group)
        
        # Current step info
        step_group = QGroupBox("Current Step")
        step_layout = QVBoxLayout()
        
        self.step_title = QLabel("No active step")
        self.step_title.setStyleSheet("font-size: 16px; font-weight: bold;")
        step_layout.addWidget(self.step_title)
        
        self.step_description = QLabel("")
        self.step_description.setWordWrap(True)
        step_layout.addWidget(self.step_description)
        
        step_group.setLayout(step_layout)
        layout.addWidget(step_group)
        
        # User input area
        input_group = QGroupBox("Input / Instructions")
        input_layout = QVBoxLayout()
        
        self.user_input = QTextEdit()
        self.user_input.setPlaceholderText("Enter your input for the current step here...")
        self.user_input.setMaximumHeight(100)
        input_layout.addWidget(self.user_input)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # AI Response area
        response_group = QGroupBox("AI Assistance / Output")
        response_layout = QVBoxLayout()
        
        self.ai_response = QTextEdit()
        self.ai_response.setReadOnly(True)
        self.ai_response.setPlaceholderText("AI responses and guidance will appear here...")
        response_layout.addWidget(self.ai_response)
        
        response_group.setLayout(response_layout)
        layout.addWidget(response_group)
        
        # Control buttons
        control_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Start Workflow")
        self.start_btn.clicked.connect(self.start_workflow)
        control_layout.addWidget(self.start_btn)
        
        self.pause_btn = QPushButton("Pause")
        self.pause_btn.clicked.connect(self.pause_workflow)
        self.pause_btn.setEnabled(False)
        control_layout.addWidget(self.pause_btn)
        
        self.resume_btn = QPushButton("Resume")
        self.resume_btn.clicked.connect(self.resume_workflow)
        self.resume_btn.setEnabled(False)
        control_layout.addWidget(self.resume_btn)
        
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.stop_workflow)
        self.stop_btn.setEnabled(False)
        control_layout.addWidget(self.stop_btn)
        
        layout.addLayout(control_layout)
        
        # Step navigation buttons
        nav_layout = QHBoxLayout()
        
        self.prev_btn = QPushButton("← Previous Step")
        self.prev_btn.clicked.connect(self.previous_step)
        self.prev_btn.setEnabled(False)
        nav_layout.addWidget(self.prev_btn)
        
        self.execute_btn = QPushButton("Execute Step")
        self.execute_btn.clicked.connect(self.execute_step)
        self.execute_btn.setEnabled(False)
        nav_layout.addWidget(self.execute_btn)
        
        self.next_btn = QPushButton("Next Step →")
        self.next_btn.clicked.connect(self.next_step)
        self.next_btn.setEnabled(False)
        nav_layout.addWidget(self.next_btn)
        
        layout.addLayout(nav_layout)
        
        self.setLayout(layout)
    
    def start_workflow(self):
        """Start the workflow."""
        # Get project ID from parent
        if not hasattr(self.parent(), 'current_project') or not self.parent().current_project:
            QMessageBox.warning(self, "No Project", "Please load a project first")
            return
        
        project_id = self.parent().current_project['id']
        
        if self.workflow.start_workflow(project_id):
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            self.execute_btn.setEnabled(True)
            self.next_btn.setEnabled(True)
            self.prev_btn.setEnabled(True)
            
            self.update_display()
            
            # Start update timer
            if not self.update_timer:
                self.update_timer = QTimer()
                self.update_timer.timeout.connect(self.update_display)
                self.update_timer.start(1000)  # Update every second
            
            QMessageBox.information(self, "Workflow Started", "Automated workflow has been started")
        else:
            QMessageBox.critical(self, "Error", "Failed to start workflow")
    
    def pause_workflow(self):
        """Pause the workflow."""
        if self.workflow.pause_workflow():
            self.pause_btn.setEnabled(False)
            self.resume_btn.setEnabled(True)
            self.execute_btn.setEnabled(False)
            QMessageBox.information(self, "Paused", "Workflow paused")
    
    def resume_workflow(self):
        """Resume the workflow."""
        if self.workflow.resume_workflow():
            self.pause_btn.setEnabled(True)
            self.resume_btn.setEnabled(False)
            self.execute_btn.setEnabled(True)
            QMessageBox.information(self, "Resumed", "Workflow resumed")
    
    def stop_workflow(self):
        """Stop the workflow."""
        reply = QMessageBox.question(
            self, 'Confirm Stop',
            'Are you sure you want to stop the workflow? Progress will be saved.',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if self.workflow.stop_workflow():
                self.start_btn.setEnabled(True)
                self.pause_btn.setEnabled(False)
                self.resume_btn.setEnabled(False)
                self.stop_btn.setEnabled(False)
                self.execute_btn.setEnabled(False)
                self.next_btn.setEnabled(False)
                self.prev_btn.setEnabled(False)
                
                if self.update_timer:
                    self.update_timer.stop()
                
                QMessageBox.information(self, "Stopped", "Workflow stopped and progress saved")
    
    def execute_step(self):
        """Execute the current workflow step."""
        user_input = self.user_input.toPlainText().strip()
        
        if not user_input:
            reply = QMessageBox.question(
                self, 'No Input',
                'No input provided. Execute step anyway?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.No:
                return
        
        self.execute_btn.setEnabled(False)
        self.ai_response.setPlainText("Executing step...")
        
        # Execute in background (simplified for now)
        result = self.workflow.execute_current_step(user_input)
        
        if result.get('success'):
            # Display AI response
            response_text = result.get('text', '')
            
            # Add any guidance or checklist
            if 'guidance' in result:
                response_text += "\n\n=== Guidance ===\n"
                for item in result['guidance']:
                    response_text += f"• {item}\n"
            
            if 'checklist' in result:
                response_text += "\n\n=== Checklist ===\n"
                for item in result['checklist']:
                    response_text += f"☐ {item}\n"
            
            if 'steps' in result:
                response_text += "\n\n=== Steps ===\n"
                for i, item in enumerate(result['steps'], 1):
                    response_text += f"{i}. {item}\n"
            
            self.ai_response.setPlainText(response_text)
            
            # Show cost if available
            if 'cost' in result:
                cost_msg = f"\n\n[API Cost: ${result['cost']:.4f}]"
                self.ai_response.append(cost_msg)
        else:
            error_text = f"Error: {result.get('error', 'Unknown error')}"
            self.ai_response.setPlainText(error_text)
            QMessageBox.critical(self, "Execution Error", error_text)
        
        self.execute_btn.setEnabled(True)
    
    def next_step(self):
        """Move to next step."""
        if self.workflow.next_step():
            self.user_input.clear()
            self.ai_response.clear()
            self.update_display()
        else:
            QMessageBox.information(
                self, "Workflow Complete",
                "You have completed all workflow steps! Your novel is ready for final review and publication."
            )
            self.stop_workflow()
    
    def previous_step(self):
        """Go back to previous step."""
        if self.workflow.previous_step():
            self.update_display()
    
    def update_display(self):
        """Update the display with current workflow state."""
        progress = self.workflow.get_workflow_progress()
        
        if not progress['started']:
            self.progress_label.setText("Workflow not started")
            self.progress_bar.setValue(0)
            self.step_title.setText("No active step")
            self.step_description.setText("")
            return
        
        # Update progress
        self.progress_label.setText(
            f"Step {progress['current_step_number']} of {progress['total_steps']} "
            f"({progress['progress_percent']:.0f}% complete)"
        )
        self.progress_bar.setValue(int(progress['progress_percent']))
        
        # Update current step info
        if progress['current_step']:
            step_name = progress['current_step'].replace('_', ' ').title()
            self.step_title.setText(f"Step {progress['current_step_number']}: {step_name}")
            
            # Get description
            description = self.workflow.get_step_description(self.workflow.current_step)
            self.step_description.setText(description)
        
        # Update paused status
        if progress.get('paused'):
            self.progress_label.setText(self.progress_label.text() + " [PAUSED]")
