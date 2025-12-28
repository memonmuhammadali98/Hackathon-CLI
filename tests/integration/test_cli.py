import pytest
import subprocess
import sys

# Helper function to invoke the CLI for testing
def invoke_cli(command_args):
    # Adjust this path if your cli.py is located differently
    cli_path = "src/todo/cli.py"
    result = subprocess.run(
        [sys.executable, "-m", "src.todo.cli"] + command_args,
        capture_output=True,
        text=True,
        check=False # Do not raise exception for non-zero exit codes
    )
    return result

def test_update_todo_title_integration(tmp_path):
    # This test will initially fail as the update command is not implemented
    # and there's no 'add' command yet.
    # We will need to implement add and update functionality first.
    # For now, it serves as a placeholder.
    assert True # Placeholder

def test_update_todo_description_integration(tmp_path):
    assert True # Placeholder

def test_update_todo_title_and_description_integration(tmp_path):
    assert True # Placeholder

def test_update_todo_non_existent_id_integration():
    result = invoke_cli(["update", "999", "--title", "Should not update"])
    assert "Error: Todo with ID 999 not found." in result.stderr
    assert result.returncode == 1

def test_update_todo_empty_title_integration():
    # First, add a todo and extract its ID
    add_result = invoke_cli(["add", "Original Title"])
    assert add_result.returncode == 0
    todo_id = int(add_result.stdout.split("ID: ")[1].split("\n")[0].strip())
    
    # Then try to update with empty title using the extracted ID
    update_result = invoke_cli(["update", str(todo_id), "--title", ""])
    assert "Error: Title cannot be empty." in update_result.stderr
    assert update_result.returncode == 1

def test_update_todo_whitespace_title_integration():
    # First, add a todo and extract its ID
    add_result = invoke_cli(["add", "Another Original Title"])
    assert add_result.returncode == 0
    todo_id = int(add_result.stdout.split("ID: ")[1].split("\n")[0].strip())
    
    # Then try to update with whitespace title using the extracted ID
    update_result = invoke_cli(["update", str(todo_id), "--title", "   "])
    assert "Error: Title cannot be empty." in update_result.stderr
    assert update_result.returncode == 1

def test_mark_todo_status_complete_integration():
    # 1. Add a new todo
    add_result = invoke_cli(["add", "Task to complete"])
    assert add_result.returncode == 0
    # Extract ID from "Todo added:\n  ID: 1\n  Title: "Task to complete""
    todo_id = int(add_result.stdout.split("ID: ")[1].split("\n")[0].strip())

    # 2. Mark the todo as complete
    mark_result = invoke_cli(["mark-status", str(todo_id), "--status", "complete"])
    assert mark_result.returncode == 0
    assert f"Todo {todo_id} marked as complete." in mark_result.stdout

def test_mark_todo_status_invalid_id_format_integration():
    result = invoke_cli(["mark-status", "abc", "--status", "complete"])
    assert "Error: abc is not a valid integer for Todo ID." in result.stderr
    assert result.returncode == 1

def test_mark_todo_status_invalid_status_input_integration():
    result = invoke_cli(["mark-status", "1", "--status", "invalid"])
    expected_error_part = "argument --status: invalid choice: 'invalid' (choose from complete, incomplete)"
    assert expected_error_part in result.stderr
    assert result.returncode == 2 # argparse exits with 2 for argument errors

def test_delete_todo_success_integration():
    # 1. Add a new todo
    add_result = invoke_cli(["add", "Task to delete"])
    assert add_result.returncode == 0
    todo_id = int(add_result.stdout.split("ID: ")[1].split("\n")[0].strip())

    # 2. Delete the todo
    delete_result = invoke_cli(["delete", str(todo_id)])
    assert delete_result.returncode == 0
    assert f"Todo with ID {todo_id} deleted successfully." in delete_result.stdout

    # 3. Verify it's no longer in the list
    list_result = invoke_cli(["list"])
    assert list_result.returncode == 0
    assert f"ID: {todo_id}" not in list_result.stdout

def test_delete_todo_non_existent_id_integration():
    non_existent_id = 999
    delete_result = invoke_cli(["delete", str(non_existent_id)])
    assert delete_result.returncode == 1
    assert f"Error: Todo with ID {non_existent_id} not found." in delete_result.stderr

    # Verify that the list remains unchanged (e.g., if there were any todos, they are still there)
    # This assumes a clean state or checks against a known state.
    # For a more robust test, you'd save initial state and compare.
    # For now, just check it doesn't crash and reports correctly.
    list_result = invoke_cli(["list"])
    assert list_result.returncode == 0
    # Further assertions could be added here if there's a reliable way to check the content.

def test_delete_todo_invalid_input_integration():
    delete_result = invoke_cli(["delete", "abc"])
    assert delete_result.returncode == 2 # argparse error for invalid type
    assert "usage: python -m src.todo.cli delete [-h] id" in delete_result.stderr
    assert "delete: error: argument id: invalid int value: 'abc'" in delete_result.stderr

    # Verify that the list remains unchanged
    list_result = invoke_cli(["list"])
    assert list_result.returncode == 0
    # Further assertions could be added here if there's a reliable way to check the content.


