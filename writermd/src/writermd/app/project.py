import importlib.resources
import yaml
import shutil
from typing import Optional
from pathlib import Path
from dataclasses import dataclass, asdict

from writermd.exceptions import WriterMDError

SAMPLE_WIP_PATH = Path(__file__).parent.parent.parent.parent / "wip-template"
CONFIG_FILE_NAME = "writermd.yml"
DEFAULT_SOURCES_DIR = "chapters"

@dataclass
class WriterMDProject:
    """Configuration for a WriterMD project."""
    name: str
    author: str
    publishDir: str = "publish"
    draftDir: str = "drafts"
    sourceDir: str = "chapters"

    # epub specific settings: located under publish
    epubFrontmatter: str = "epub-frontmatter.md"
    epubEndmatter: str = "epub-endmatter.md"

    # web specific settings: located under publish
    webLocation: str = ""
    webFrontmatter: str = "web-frontmatter.md"
    webEndmatter: str = "web-endmatter.md"

writermd_config: Optional[WriterMDProject] = None

def get_wip_template_path() -> Path:
    try:
        # For installed packages, use importlib.resources to get the package data
        with importlib.resources.path("writermd.data", "wip-template") as p:
            return p
    except (FileNotFoundError, ImportError):
        # Fallback to relative path if not installed as a package
        return Path(__file__).parent.parent.parent.parent.parent / "wip-template"


def load_project(config_path: Path) -> WriterMDProject:
    """Loads the WriterMD configuration from a YAML file.

    :param config_path: Path to the configuration YAML file.
    :return: WriterMDConfig object with the loaded configuration.
    """
    global writermd_config

    with open(config_path, "r") as f:
        config_data = yaml.safe_load(f)

    writermd_config = WriterMDProject(**config_data)
    return writermd_config

def write_config(config_path: Path):
    """Writes the WriterMD project to a YAML file.

    :param config: WriterMDConfig object to write.
    :param config_path: Path to the configuration YAML file.
    """
    global writermd_config
    if writermd_config is None:
        raise ValueError("WriterMD configuration has not been loaded.")
    with open(config_path, "w") as f:
        yaml.safe_dump(asdict(writermd_config), f)

def get_project() -> WriterMDProject:
    """Gets the currently loaded WriterMD configuration.

    :return: WriterMDConfig object.
    :raises WriterMDError: If the configuration has not been loaded yet.
    """
    if writermd_config is None:
        raise ValueError("WriterMD configuration has not been loaded.")
    return writermd_config

def validate_project_structure(project_path: Path):
    """Validates that the given path contains a valid WriterMD project structure.

    :param project_path: Path to the project directory.
    :return: WriterMDConfig object if the structure is valid.
    :raises FileNotFoundError: If the configuration file is not found.
    :raises ValueError: If the configuration file is invalid.
    """
    config_path = project_path / "writermd.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found at {config_path}")

    try:
        return load_project(config_path)
    except Exception as e:
        raise WriterMDError(f"Invalid configuration file: {e}")

def create_sample_project(name: str, path: Path, sources_dir: Optional[str] = None, template_path: Path|str = None):
    """Creates a sample WriterMD project structure.

    :param name: Name of the project.
    :param path: Path where the project should be created.
    :param sources_dir: Optional custom sources directory name.
    """

    if not template_path or not Path(template_path).is_dir():
        template_path = get_wip_template_path()
    else:
        template_path = Path(template_path)

    print("Creating new WriterMD project at:", path)

    # Copy the sample WIP structure to the new project directory
    destination = path
    shutil.copytree(template_path, path)

    # Rename sources directory if specified
    if sources_dir:
        (destination / DEFAULT_SOURCES_DIR).rename(destination / sources_dir)

    # Edit the config file to set the project name
    config_yaml = destination / CONFIG_FILE_NAME
    config = load_project(config_yaml)
    config.name = name

    write_config(config_yaml)
