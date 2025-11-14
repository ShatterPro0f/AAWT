"""
File Operations Module
Handles project file I/O, backups, and file locking.
"""

import os
import json
import logging
import shutil
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import zipfile

logger = logging.getLogger(__name__)


class FileOperations:
    """Manages project file operations."""
    
    def __init__(self, projects_dir: str = "projects"):
        """
        Initialize file operations.
        
        Args:
            projects_dir: Base directory for projects
        """
        self.projects_dir = Path(projects_dir)
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"File operations initialized: {projects_dir}")
    
    def get_project_dir(self, project_name: str) -> Path:
        """Get project directory path."""
        # Sanitize project name for filesystem
        safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_')).strip()
        return self.projects_dir / safe_name
    
    def create_project_structure(self, project_name: str) -> bool:
        """
        Create project directory structure.
        
        Args:
            project_name: Project name
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            project_dir.mkdir(parents=True, exist_ok=True)
            
            # Create subdirectories
            (project_dir / 'sessions').mkdir(exist_ok=True)
            (project_dir / 'backups').mkdir(exist_ok=True)
            (project_dir / 'exports').mkdir(exist_ok=True)
            
            logger.info(f"Created project structure for: {project_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to create project structure: {e}")
            return False
    
    def save_project_content(self, project_name: str, content: str) -> bool:
        """
        Save project content to file.
        
        Args:
            project_name: Project name
            content: Content to save
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            content_file = project_dir / 'content.txt'
            
            with open(content_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.debug(f"Saved content for project: {project_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to save project content: {e}")
            return False
    
    def load_project_content(self, project_name: str) -> Optional[str]:
        """
        Load project content from file.
        
        Args:
            project_name: Project name
        
        Returns:
            Content string or None if not found
        """
        try:
            project_dir = self.get_project_dir(project_name)
            content_file = project_dir / 'content.txt'
            
            if content_file.exists():
                with open(content_file, 'r', encoding='utf-8') as f:
                    return f.read()
            
            return ''
        except Exception as e:
            logger.error(f"Failed to load project content: {e}")
            return None
    
    def save_project_metadata(self, project_name: str, metadata: Dict) -> bool:
        """
        Save project metadata to file.
        
        Args:
            project_name: Project name
            metadata: Metadata dictionary
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            metadata_file = project_dir / 'metadata.json'
            
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            logger.debug(f"Saved metadata for project: {project_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to save project metadata: {e}")
            return False
    
    def load_project_metadata(self, project_name: str) -> Optional[Dict]:
        """
        Load project metadata from file.
        
        Args:
            project_name: Project name
        
        Returns:
            Metadata dictionary or None if not found
        """
        try:
            project_dir = self.get_project_dir(project_name)
            metadata_file = project_dir / 'metadata.json'
            
            if metadata_file.exists():
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            
            return {}
        except Exception as e:
            logger.error(f"Failed to load project metadata: {e}")
            return None
    
    def create_backup(self, project_name: str) -> Optional[str]:
        """
        Create a backup of the project.
        
        Args:
            project_name: Project name
        
        Returns:
            Backup file path or None if failed
        """
        try:
            project_dir = self.get_project_dir(project_name)
            if not project_dir.exists():
                logger.error(f"Project directory not found: {project_name}")
                return None
            
            backup_dir = project_dir / 'backups'
            backup_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = backup_dir / f'backup_{timestamp}.zip'
            
            # Create zip archive
            with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add content file
                content_file = project_dir / 'content.txt'
                if content_file.exists():
                    zipf.write(content_file, 'content.txt')
                
                # Add metadata file
                metadata_file = project_dir / 'metadata.json'
                if metadata_file.exists():
                    zipf.write(metadata_file, 'metadata.json')
            
            logger.info(f"Created backup: {backup_file}")
            return str(backup_file)
        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            return None
    
    def restore_backup(self, project_name: str, backup_path: str) -> bool:
        """
        Restore project from backup.
        
        Args:
            project_name: Project name
            backup_path: Path to backup file
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            
            # Extract backup
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                zipf.extractall(project_dir)
            
            logger.info(f"Restored backup: {backup_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to restore backup: {e}")
            return False
    
    def list_backups(self, project_name: str) -> list:
        """
        List available backups for a project.
        
        Args:
            project_name: Project name
        
        Returns:
            List of backup file paths
        """
        try:
            project_dir = self.get_project_dir(project_name)
            backup_dir = project_dir / 'backups'
            
            if not backup_dir.exists():
                return []
            
            backups = []
            for backup_file in backup_dir.glob('backup_*.zip'):
                backups.append({
                    'path': str(backup_file),
                    'name': backup_file.name,
                    'size': backup_file.stat().st_size,
                    'created': datetime.fromtimestamp(backup_file.stat().st_mtime).isoformat()
                })
            
            # Sort by creation time, newest first
            backups.sort(key=lambda x: x['created'], reverse=True)
            return backups
        except Exception as e:
            logger.error(f"Failed to list backups: {e}")
            return []
    
    def delete_project_files(self, project_name: str) -> bool:
        """
        Delete all project files.
        
        Args:
            project_name: Project name
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            
            if project_dir.exists():
                shutil.rmtree(project_dir)
                logger.info(f"Deleted project files: {project_name}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Failed to delete project files: {e}")
            return False
    
    def is_project_locked(self, project_name: str) -> bool:
        """
        Check if project is locked (open in another instance).
        
        Args:
            project_name: Project name
        
        Returns:
            True if locked
        """
        try:
            project_dir = self.get_project_dir(project_name)
            lock_file = project_dir / '.lock'
            
            if not lock_file.exists():
                return False
            
            # Check if lock is stale
            lock_time = lock_file.stat().st_mtime
            current_time = datetime.now().timestamp()
            
            # Consider lock stale after 1 hour
            if current_time - lock_time > 3600:
                logger.warning(f"Stale lock file detected for: {project_name}")
                lock_file.unlink()
                return False
            
            return True
        except Exception as e:
            logger.error(f"Failed to check project lock: {e}")
            return False
    
    def lock_project(self, project_name: str) -> bool:
        """
        Create lock file for project.
        
        Args:
            project_name: Project name
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            lock_file = project_dir / '.lock'
            
            # Create lock file with PID
            with open(lock_file, 'w') as f:
                f.write(str(os.getpid()))
            
            logger.debug(f"Locked project: {project_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to lock project: {e}")
            return False
    
    def unlock_project(self, project_name: str) -> bool:
        """
        Remove lock file for project.
        
        Args:
            project_name: Project name
        
        Returns:
            True if successful
        """
        try:
            project_dir = self.get_project_dir(project_name)
            lock_file = project_dir / '.lock'
            
            if lock_file.exists():
                lock_file.unlink()
                logger.debug(f"Unlocked project: {project_name}")
            
            return True
        except Exception as e:
            logger.error(f"Failed to unlock project: {e}")
            return False
    
    def get_project_size(self, project_name: str) -> int:
        """
        Get total size of project files in bytes.
        
        Args:
            project_name: Project name
        
        Returns:
            Total size in bytes
        """
        try:
            project_dir = self.get_project_dir(project_name)
            
            if not project_dir.exists():
                return 0
            
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(project_dir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if os.path.exists(filepath):
                        total_size += os.path.getsize(filepath)
            
            return total_size
        except Exception as e:
            logger.error(f"Failed to get project size: {e}")
            return 0
