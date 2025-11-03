"""Manage sample project formats for WriterMD."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

@dataclass
class SampleFile:
    name: str
    content: str

# Sample for a book project
@dataclass
class SampleProject:
    """Complete sample project structure."""
    name: str
    
