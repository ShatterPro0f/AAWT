"""
Automated Novel Workflow for AAWT
Implements 11-step writing process with AI assistance, progress tracking, and recovery.
"""

import logging
import json
from typing import Dict, Any, List, Optional, Callable
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class WorkflowStep(Enum):
    """11-step writing process."""
    PROJECT_INITIALIZATION = 1
    CHARACTER_DEVELOPMENT = 2
    WORLD_BUILDING = 3
    PLOT_OUTLINING = 4
    SCENE_PLANNING = 5
    FIRST_DRAFT_WRITING = 6
    EDITING_PASS_1 = 7
    EDITING_PASS_2 = 8
    BETA_READER_FEEDBACK = 9
    FINAL_REVISIONS = 10
    EXPORT_PUBLISHING = 11


class WorkflowManager:
    """Manages automated writing workflow."""
    
    def __init__(self, database_manager, api_manager, settings_manager):
        """
        Initialize workflow manager.
        
        Args:
            database_manager: Database manager instance
            api_manager: API manager instance
            settings_manager: Settings manager instance
        """
        self.database = database_manager
        self.api = api_manager
        self.settings = settings_manager
        
        self.current_step = WorkflowStep.PROJECT_INITIALIZATION
        self.workflow_state = {}
        self.step_callbacks = {}
        self.is_running = False
        self.is_paused = False
        
        logger.info("Workflow Manager initialized")
    
    def start_workflow(self, project_id: int) -> bool:
        """
        Start automated workflow for a project.
        
        Args:
            project_id: Project ID
        
        Returns:
            True if started successfully
        """
        if self.is_running:
            logger.warning("Workflow already running")
            return False
        
        try:
            # Load workflow state if exists
            self.workflow_state = self._load_workflow_state(project_id)
            
            if not self.workflow_state:
                # Initialize new workflow
                self.workflow_state = {
                    'project_id': project_id,
                    'current_step': WorkflowStep.PROJECT_INITIALIZATION.value,
                    'completed_steps': [],
                    'started_at': datetime.now().isoformat(),
                    'step_data': {}
                }
            
            self.current_step = WorkflowStep(self.workflow_state['current_step'])
            self.is_running = True
            self.is_paused = False
            
            logger.info(f"Workflow started for project {project_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to start workflow: {e}")
            return False
    
    def pause_workflow(self) -> bool:
        """Pause the workflow."""
        if not self.is_running:
            return False
        
        self.is_paused = True
        self._save_workflow_state()
        logger.info("Workflow paused")
        return True
    
    def resume_workflow(self) -> bool:
        """Resume paused workflow."""
        if not self.is_running or not self.is_paused:
            return False
        
        self.is_paused = False
        logger.info("Workflow resumed")
        return True
    
    def stop_workflow(self) -> bool:
        """Stop the workflow."""
        if not self.is_running:
            return False
        
        self._save_workflow_state()
        self.is_running = False
        self.is_paused = False
        logger.info("Workflow stopped")
        return True
    
    def next_step(self) -> bool:
        """Advance to next step."""
        if not self.is_running or self.is_paused:
            return False
        
        # Mark current step as completed
        if self.current_step.value not in self.workflow_state['completed_steps']:
            self.workflow_state['completed_steps'].append(self.current_step.value)
        
        # Move to next step
        if self.current_step.value < WorkflowStep.EXPORT_PUBLISHING.value:
            self.current_step = WorkflowStep(self.current_step.value + 1)
            self.workflow_state['current_step'] = self.current_step.value
            self._save_workflow_state()
            logger.info(f"Advanced to step: {self.current_step.name}")
            return True
        else:
            # Workflow complete
            self.stop_workflow()
            logger.info("Workflow completed")
            return False
    
    def previous_step(self) -> bool:
        """Go back to previous step."""
        if not self.is_running or self.is_paused:
            return False
        
        if self.current_step.value > WorkflowStep.PROJECT_INITIALIZATION.value:
            self.current_step = WorkflowStep(self.current_step.value - 1)
            self.workflow_state['current_step'] = self.current_step.value
            self._save_workflow_state()
            logger.info(f"Went back to step: {self.current_step.name}")
            return True
        
        return False
    
    def execute_current_step(self, user_input: str = "") -> Dict[str, Any]:
        """
        Execute the current workflow step.
        
        Args:
            user_input: User input for the step
        
        Returns:
            Step execution result
        """
        if not self.is_running or self.is_paused:
            return {'success': False, 'error': 'Workflow not running'}
        
        step_methods = {
            WorkflowStep.PROJECT_INITIALIZATION: self._step_project_init,
            WorkflowStep.CHARACTER_DEVELOPMENT: self._step_character_dev,
            WorkflowStep.WORLD_BUILDING: self._step_world_building,
            WorkflowStep.PLOT_OUTLINING: self._step_plot_outlining,
            WorkflowStep.SCENE_PLANNING: self._step_scene_planning,
            WorkflowStep.FIRST_DRAFT_WRITING: self._step_first_draft,
            WorkflowStep.EDITING_PASS_1: self._step_editing_1,
            WorkflowStep.EDITING_PASS_2: self._step_editing_2,
            WorkflowStep.BETA_READER_FEEDBACK: self._step_beta_feedback,
            WorkflowStep.FINAL_REVISIONS: self._step_final_revisions,
            WorkflowStep.EXPORT_PUBLISHING: self._step_export_publish
        }
        
        method = step_methods.get(self.current_step)
        if method:
            return method(user_input)
        
        return {'success': False, 'error': 'Unknown step'}
    
    def get_workflow_progress(self) -> Dict[str, Any]:
        """Get workflow progress information."""
        if not self.workflow_state:
            return {
                'started': False,
                'progress_percent': 0,
                'current_step': None,
                'completed_steps': []
            }
        
        total_steps = len(WorkflowStep)
        completed_count = len(self.workflow_state['completed_steps'])
        progress_percent = (completed_count / total_steps) * 100
        
        return {
            'started': self.is_running,
            'paused': self.is_paused,
            'progress_percent': round(progress_percent, 2),
            'current_step': self.current_step.name if self.is_running else None,
            'current_step_number': self.current_step.value if self.is_running else 0,
            'completed_steps': self.workflow_state['completed_steps'],
            'total_steps': total_steps
        }
    
    # Individual step implementations
    
    def _step_project_init(self, user_input: str) -> Dict[str, Any]:
        """Step 1: Project Initialization."""
        logger.info("Executing: Project Initialization")
        
        prompt = f"""Help initialize a writing project with these details:
{user_input}

Provide:
1. Project structure recommendations
2. Target audience considerations
3. Genre-specific elements to include
4. Estimated timeline
"""
        
        result = self.api.call_ai(prompt, system_prompt="You are a writing coach helping with project setup.")
        
        if result.get('success'):
            self.workflow_state['step_data']['project_init'] = {
                'user_input': user_input,
                'ai_response': result.get('text'),
                'completed_at': datetime.now().isoformat()
            }
            self._save_workflow_state()
        
        return result
    
    def _step_character_dev(self, user_input: str) -> Dict[str, Any]:
        """Step 2: Character Development."""
        logger.info("Executing: Character Development")
        
        prompt = f"""Help develop characters for a story:
{user_input}

Provide detailed character profiles including:
1. Physical description
2. Personality traits
3. Background and motivation
4. Character arc
5. Relationships with other characters
"""
        
        result = self.api.call_ai(prompt, system_prompt="You are a character development expert.")
        
        if result.get('success'):
            self.workflow_state['step_data']['character_dev'] = {
                'user_input': user_input,
                'ai_response': result.get('text'),
                'completed_at': datetime.now().isoformat()
            }
            self._save_workflow_state()
        
        return result
    
    def _step_world_building(self, user_input: str) -> Dict[str, Any]:
        """Step 3: World Building."""
        logger.info("Executing: World Building")
        
        prompt = f"""Help build a fictional world:
{user_input}

Provide:
1. Setting description (geography, climate, etc.)
2. Society and culture
3. History and lore
4. Magic system or technology (if applicable)
5. Important locations
"""
        
        result = self.api.call_ai(prompt, system_prompt="You are a world-building specialist.")
        
        if result.get('success'):
            self.workflow_state['step_data']['world_building'] = {
                'user_input': user_input,
                'ai_response': result.get('text'),
                'completed_at': datetime.now().isoformat()
            }
            self._save_workflow_state()
        
        return result
    
    def _step_plot_outlining(self, user_input: str) -> Dict[str, Any]:
        """Step 4: Plot Outlining."""
        logger.info("Executing: Plot Outlining")
        
        prompt = f"""Help create a plot outline:
{user_input}

Provide:
1. Three-act structure breakdown
2. Major plot points and turning points
3. Subplots
4. Conflict and resolution
5. Climax planning
"""
        
        result = self.api.call_ai(prompt, system_prompt="You are a plot structure expert.")
        
        if result.get('success'):
            self.workflow_state['step_data']['plot_outlining'] = {
                'user_input': user_input,
                'ai_response': result.get('text'),
                'completed_at': datetime.now().isoformat()
            }
            self._save_workflow_state()
        
        return result
    
    def _step_scene_planning(self, user_input: str) -> Dict[str, Any]:
        """Step 5: Scene Planning."""
        logger.info("Executing: Scene Planning")
        
        prompt = f"""Help plan individual scenes:
{user_input}

For each scene provide:
1. Purpose in story
2. Characters involved
3. Setting
4. Conflict/tension
5. Outcome/transition
"""
        
        result = self.api.call_ai(prompt, system_prompt="You are a scene planning expert.")
        
        if result.get('success'):
            self.workflow_state['step_data']['scene_planning'] = {
                'user_input': user_input,
                'ai_response': result.get('text'),
                'completed_at': datetime.now().isoformat()
            }
            self._save_workflow_state()
        
        return result
    
    def _step_first_draft(self, user_input: str) -> Dict[str, Any]:
        """Step 6: First Draft Writing."""
        logger.info("Executing: First Draft Writing")
        
        return {
            'success': True,
            'text': 'First draft step - write freely without editing. Focus on getting the story down.',
            'guidance': [
                'Write without stopping to edit',
                'Focus on plot progression',
                'Develop character voices',
                'Keep momentum going',
                'Save editing for later passes'
            ]
        }
    
    def _step_editing_1(self, user_input: str) -> Dict[str, Any]:
        """Step 7: Editing Pass 1 - Structure and Plot."""
        logger.info("Executing: Editing Pass 1")
        
        return {
            'success': True,
            'text': 'First editing pass - focus on big picture elements',
            'checklist': [
                'Plot consistency',
                'Character development arcs',
                'Pacing issues',
                'Scene order',
                'Major plot holes'
            ]
        }
    
    def _step_editing_2(self, user_input: str) -> Dict[str, Any]:
        """Step 8: Editing Pass 2 - Line Level."""
        logger.info("Executing: Editing Pass 2")
        
        return {
            'success': True,
            'text': 'Second editing pass - focus on prose and style',
            'checklist': [
                'Sentence structure',
                'Word choice',
                'Dialogue quality',
                'Description balance',
                'Grammar and punctuation'
            ]
        }
    
    def _step_beta_feedback(self, user_input: str) -> Dict[str, Any]:
        """Step 9: Beta Reader Feedback."""
        logger.info("Executing: Beta Reader Feedback")
        
        return {
            'success': True,
            'text': 'Collect and organize beta reader feedback',
            'guidance': [
                'Select 3-5 beta readers from target audience',
                'Provide feedback forms or questions',
                'Collect responses systematically',
                'Look for patterns in feedback',
                'Prioritize actionable suggestions'
            ]
        }
    
    def _step_final_revisions(self, user_input: str) -> Dict[str, Any]:
        """Step 10: Final Revisions."""
        logger.info("Executing: Final Revisions")
        
        return {
            'success': True,
            'text': 'Make final revisions based on feedback',
            'checklist': [
                'Address beta reader feedback',
                'Proofread thoroughly',
                'Check formatting consistency',
                'Verify chapter/section order',
                'Final read-through'
            ]
        }
    
    def _step_export_publish(self, user_input: str) -> Dict[str, Any]:
        """Step 11: Export & Publishing."""
        logger.info("Executing: Export & Publishing")
        
        return {
            'success': True,
            'text': 'Prepare for publication',
            'steps': [
                'Export to required formats',
                'Format for publication platform',
                'Prepare cover and metadata',
                'Review publishing checklist',
                'Submit or self-publish'
            ]
        }
    
    def _load_workflow_state(self, project_id: int) -> Optional[Dict]:
        """Load workflow state from database."""
        try:
            cached = self.database.get_cached_content('workflow_state', str(project_id))
            return cached
        except Exception as e:
            logger.error(f"Failed to load workflow state: {e}")
            return None
    
    def _save_workflow_state(self) -> bool:
        """Save workflow state to database."""
        try:
            if not self.workflow_state:
                return False
            
            project_id = self.workflow_state.get('project_id')
            if not project_id:
                return False
            
            self.database.cache_content(
                'workflow_state',
                str(project_id),
                self.workflow_state,
                ttl_days=365  # Keep for a year
            )
            
            logger.debug("Workflow state saved")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save workflow state: {e}")
            return False
    
    def get_step_description(self, step: WorkflowStep) -> str:
        """Get description for a workflow step."""
        descriptions = {
            WorkflowStep.PROJECT_INITIALIZATION: "Set up your project structure and goals",
            WorkflowStep.CHARACTER_DEVELOPMENT: "Create and develop your characters",
            WorkflowStep.WORLD_BUILDING: "Build your story's world and setting",
            WorkflowStep.PLOT_OUTLINING: "Outline your plot structure",
            WorkflowStep.SCENE_PLANNING: "Plan individual scenes and chapters",
            WorkflowStep.FIRST_DRAFT_WRITING: "Write your first draft",
            WorkflowStep.EDITING_PASS_1: "Edit for structure and plot",
            WorkflowStep.EDITING_PASS_2: "Edit for style and prose",
            WorkflowStep.BETA_READER_FEEDBACK: "Collect and review feedback",
            WorkflowStep.FINAL_REVISIONS: "Make final improvements",
            WorkflowStep.EXPORT_PUBLISHING: "Prepare for publication"
        }
        return descriptions.get(step, "Unknown step")
