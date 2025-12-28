from typing import List, Optional
import json
import os
import dataclasses # Import dataclasses
from src.todo.models import Todo

class TodoNotFoundException(Exception):
    """Custom exception raised when a Todo item is not found."""
    pass

STORAGE_FILE = "todos.json"

class TodoService:
    def __init__(self, storage_file: str = "todos.json"):
        self._storage_file = storage_file
        self._todos: List[Todo] = []
        self._next_id = 1
        self._load_todos()

    def _load_todos(self):
        if os.path.exists(self._storage_file):
            with open(self._storage_file, "r") as f:
                data = json.load(f)
                self._todos = [Todo(**item) for item in data["todos"]]
                # Ensure _next_id is at least 1, or max ID + 1
                if self._todos:
                    self._next_id = max(todo.id for todo in self._todos) + 1
                else:
                    self._next_id = 1
        else:
            self._todos = []
            self._next_id = 1

    def _save_todos(self):
        with open(self._storage_file, "w") as f:
            data = {"todos": [dataclasses.asdict(todo) for todo in self._todos], "next_id": self._next_id}
            json.dump(data, f, indent=4)

    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        todo = Todo(id=self._next_id, title=title, description=description)
        self._todos.append(todo)
        self._next_id += 1
        self._save_todos()  # Save after adding
        return todo

    def get_all_todos(self) -> List[Todo]:
        self._load_todos() # Ensure latest todos are loaded before returning
        return self._todos

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        return next((todo for todo in self._todos if todo.id == todo_id), None)

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Todo]:
        for todo in self._todos:
            if todo.id == todo_id:
                if title is not None:
                    if not title.strip():
                        raise ValueError("Title cannot be empty.")
                    todo.title = title
                if description is not None:
                    todo.description = description
                self._save_todos()  # Save after updating
                return todo
        return None # Todo not found

    def update_todo_status(self, todo_id: int, completed: bool) -> Todo:
        for todo in self._todos:
            if todo.id == todo_id:
                todo.completed = completed
                self._save_todos()  # Save after updating status
                return todo
        raise ValueError(f"Todo with ID {todo_id} not found.")

    def delete_todo(self, todo_id: int) -> None:
        initial_len = len(self._todos)
        self._todos = [todo for todo in self._todos if todo.id != todo_id]
        if len(self._todos) == initial_len:
            raise TodoNotFoundException(f"Todo with ID {todo_id} not found.")
        self._save_todos()

# Global instance for simplicity in a CLI app
todo_service = TodoService()