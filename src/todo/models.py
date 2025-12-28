from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Todo:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty.")
