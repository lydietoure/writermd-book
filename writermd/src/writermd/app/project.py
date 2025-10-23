from typing import Optional
import yaml
from pathlib import Path
from dataclasses import dataclass, asdict

from writermd.exceptions import WriterMDError

SAMPLE_WIP_PATH = Path(__file__).parent.parent / "sample-wip"
CONFIG_FILE_NAME = "writermd.yaml"


@dataclass
class WriterMDProject:
    """Configuration for a WriterMD project."""
    name: str
    publishDir: str = "publish"
    draftsDir: str = "drafts"
    sourceDir: str = "chapters"

    # epub specific settings: located under publish
    epub_frontmatter: str = "epub-frontmatter.md"
    epub_endmatter: str = "epub-endmatter.md"

    # web specific settings: located under publish
    web_location: str = ""
    web_frontmatter: str = "web-frontmatter.md"
    web_endmatter: str = "web-endmatter.md"

writermd_config: Optional[WriterMDProject] = None

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
