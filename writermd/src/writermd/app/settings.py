"""Application settings for WriterMD."""

import yaml
import platformdirs
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Set

APPLICATION_SETTINGS_FILE_NAME = "writermd-config.yaml"

from writermd.app.project import validate_project_structure, WriterMDProject

@dataclass
class ApplicationSettings:
    # Application defaults
    author: str = ""
    email: str = ""

    projects: Set[Path] = field(default_factory=set)

def get_settings_file_path() -> Path:
    """Get the path to the application settings file."""
    config_dir = Path(platformdirs.user_config_dir("writermd"))
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / APPLICATION_SETTINGS_FILE_NAME

def load_application_settings() -> ApplicationSettings:
    """Load application settings from the settings file."""
    settings_file_path = get_settings_file_path()
    if settings_file_path.exists():
        with open(settings_file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            return ApplicationSettings(**data)
    return ApplicationSettings()

def save_application_settings(settings: ApplicationSettings) -> None:
    """Save application settings to the settings file."""
    settings_file_path = get_settings_file_path()
    with open(settings_file_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(settings.__dict__, f)

def add_project(settings: ApplicationSettings, project_path: Path) -> None:
    """Add a new project path to the application settings."""
    if project_path in settings.projects:
        return

    validate_project_structure(project_path)

    settings.projects.add(project_path)
    save_application_settings(settings)

def remove_project(settings: ApplicationSettings, project_path: Path) -> None:
    """Remove a project path from the application settings."""
    settings.projects.remove(project_path)
    save_application_settings(settings)

def get_project_by_path(settings: ApplicationSettings, project_path: Path) -> Optional[WriterMDProject]:
    """Get a WriterMDProject instance by its path from the application settings."""
    if project_path not in settings.projects:
        return None

    return WriterMDProject.load_from_path(project_path)

def list_projects(settings: ApplicationSettings) -> List[WriterMDProject]:
    """List all projects in the application settings."""

    return [
        pr for p in settings.projects
        if (pr:=get_project_by_path(settings, p)) is not None
    ]
