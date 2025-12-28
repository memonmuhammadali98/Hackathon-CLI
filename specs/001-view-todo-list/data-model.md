# Data Model: Todo Item

This document describes the data model for a single Todo item, based on the feature specification for "View Todo List" and the existing `src/todo/models.py`.

## Entity: `TodoItem`

Represents a single task or to-do item within the application.

### Attributes

*   **`id`** (Integer):
    *   **Description**: A unique identifier for the Todo item.
    *   **Validation Rules**: Must be an integer. Must be unique within the current session's list of Todo items.
    *   **Source**: `src/todo/models.py`
*   **`title`** (String):
    *   **Description**: A concise summary or name of the Todo item.
    *   **Validation Rules**: Required. Must be a non-empty string.
    *   **Source**: `src/todo/models.py`
*   **`description`** (String, Optional):
    *   **Description**: A detailed explanation or additional notes for the Todo item.
    *   **Validation Rules**: Optional. Can be an empty string.
    *   **Source**: `src/todo/models.py`
*   **`status`** (String Literal: "incomplete" or "completed"):
    *   **Description**: Indicates the current completion status of the Todo item.
    *   **Validation Rules**: Must be either "incomplete" or "completed". Defaults to "incomplete".
    *   **Source**: `src/todo/models.py` (type `Status = Literal["incomplete", "completed"]`)

### Relationships

*   None: `TodoItem` is a standalone entity within the in-memory list.

### State Transitions

*   **From "incomplete" to "completed"**: A Todo item can transition from "incomplete" to "completed". (This is implied by the status attribute and future features like "mark complete").
*   **From "completed" to "incomplete"**: A Todo item can transition from "completed" to "incomplete". (Also implied for flexibility).

### Example Representation (Conceptual)

```python
TodoItem(id=1, title="Buy groceries", description="Milk, eggs, bread", status="incomplete")
TodoItem(id=2, title="Finish report", description="Draft executive summary", status="completed")
```