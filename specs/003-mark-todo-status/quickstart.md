# Quickstart Guide: Mark Todo as Complete / Incomplete

**Date**: 2025-12-28
**Feature**: Mark Todo as Complete / Incomplete
**Branch**: 003-mark-todo-status

This guide provides a quick way to set up and interact with the "Mark Todo as Complete / Incomplete" feature of the Todo CLI application.

## Prerequisites

*   Python 3.9+ installed on your system.

## Setup

1.  **Clone the repository**:
    If you haven't already, clone the project repository:
    ```bash
    git clone <repository_url>
    cd todo-cli
    ```
    (Note: Assuming you are already in the `todo-cli` directory)

2.  **Install project dependencies**:
    Install the application in editable mode to make it available as a command:
    ```bash
    pip install -e .
    ```

## Usage

Once set up, you can use the `todo` command.

1.  **Add a new todo item**:
    ```bash
    todo add "Buy groceries" --description "Milk, eggs, bread"
    ```
    (Note the ID returned by the system for the newly added todo.)

2.  **Mark a todo as complete**:
    Replace `[TODO_ID]` with the actual ID of the todo you want to mark.
    ```bash
    todo mark-status [TODO_ID] --status complete
    ```

3.  **Mark a todo as incomplete**:
    Replace `[TODO_ID]` with the actual ID of the todo you want to mark.
    ```bash
    todo mark-status [TODO_ID] --status incomplete
    ```

4.  **Verify the status (if a view command exists)**:
    If there is a command to view the todo list, use it to confirm the status change. (e.g., `todo list` or `todo view`)
    ```bash
    # Example (assuming a 'list' command exists)
    todo list
    ```
    (The output should show the updated completion status for your todo.)

## Troubleshooting

*   If the `todo` command is not found, ensure you have activated your Python virtual environment (if using one) and that `pip install -e .` ran successfully.
*   Check that the Todo ID you are using actually exists in your current in-memory list. Remember, data is not persistent.
