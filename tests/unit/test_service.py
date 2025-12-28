import pytest
from src.todo.models import Todo
from src.todo.service import TodoService, TodoNotFoundException
import os

@pytest.fixture
def todo_service_instance(tmp_path):
    # Create a temporary file for todos.json for each test
    temp_storage_file = tmp_path / "todos.json"
    service = TodoService(str(temp_storage_file))
    yield service
    # Ensure the temporary file is removed after the test
    if os.path.exists(temp_storage_file):
        os.remove(temp_storage_file)

def test_add_todo(todo_service_instance):
    service = todo_service_instance
    todo = service.add_todo("Test Title", "Test Description")
    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert todo.title == "Test Title"
    assert todo.description == "Test Description"
    assert not todo.completed
    assert len(service.get_all_todos()) == 1

def test_update_todo_status(todo_service_instance):
    service = todo_service_instance
    todo = service.add_todo("Test status update")
    assert not todo.completed

    # Mark as complete
    updated_todo = service.update_todo_status(todo.id, True)
    assert updated_todo.completed
    assert service.get_todo_by_id(todo.id).completed

    # Mark as incomplete
    updated_todo = service.update_todo_status(todo.id, False)
    assert not updated_todo.completed
    assert not service.get_todo_by_id(todo.id).completed

def test_update_todo_status_non_existent_id(todo_service_instance):
    service = todo_service_instance
    with pytest.raises(ValueError, match="Todo with ID 999 not found."):
        service.update_todo_status(999, True)

def test_get_all_todos_empty(todo_service_instance):
    service = todo_service_instance
    todos = service.get_all_todos()
    assert len(todos) == 0
    assert todos == []

def test_get_all_todos_with_items(todo_service_instance):
    service = todo_service_instance
    service.add_todo("First Todo")
    service.add_todo("Second Todo", "Second Description")
    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todos[0].title == "First Todo"
    assert todos[1].title == "Second Todo"
    assert todos[1].description == "Second Description"

def test_update_todo_title():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, title="New Title")
    assert updated_todo is not None
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "Original Description"
    assert not updated_todo.completed

def test_update_todo_description():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, description="New Description")
    assert updated_todo is not None
    assert updated_todo.title == "Original Title"
    assert updated_todo.description == "New Description"
    assert not updated_todo.completed

def test_update_todo_title_and_description():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, title="New Title", description="New Description")
    assert updated_todo is not None
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Description"
    assert not updated_todo.completed

def test_update_todo_title():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, title="New Title")
    assert updated_todo is not None
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "Original Description"
    assert not updated_todo.completed

def test_update_todo_description():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, description="New Description")
    assert updated_todo is not None
    assert updated_todo.title == "Original Title"
    assert updated_todo.description == "New Description"
    assert not updated_todo.completed

def test_update_todo_title_and_description():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    updated_todo = service.update_todo(todo.id, title="New Title", description="New Description")
    assert updated_todo is not None
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Description"
    assert not updated_todo.completed

def test_update_todo_non_existent_id():
    service = TodoService()
    updated_todo = service.update_todo(999, title="Non Existent")
    assert updated_todo is None

def test_update_todo_empty_title():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    with pytest.raises(ValueError, match="Title cannot be empty."):
        service.update_todo(todo.id, title="")

def test_update_todo_whitespace_title():
    service = TodoService()
    todo = service.add_todo("Original Title", "Original Description")
    with pytest.raises(ValueError, match="Title cannot be empty."):
        service.update_todo(todo.id, title="   ")

def test_delete_todo_success():
    service = TodoService()
    todo1 = service.add_todo("Todo 1")
    todo2 = service.add_todo("Todo 2")

    service.delete_todo(todo1.id)

    assert service.get_todo_by_id(todo1.id) is None
    assert len(service.get_all_todos()) == 1

def test_delete_todo_non_existent():
    service = TodoService()
    service.add_todo("Existing Todo")
    with pytest.raises(TodoNotFoundException, match="Todo with ID 999 not found."):
        service.delete_todo(999)

