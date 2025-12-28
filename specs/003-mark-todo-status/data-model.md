# Data Model: Mark Todo as Complete / Incomplete

**Date**: 2025-12-28
**Feature**: Mark Todo as Complete / Incomplete
**Branch**: 003-mark-todo-status

## Key Entities

### Todo

Represents a single task item within the in-memory todo list.

**Attributes**:

*   `id` (int): A unique identifier for the todo item. Assigned automatically upon creation.
*   `title` (str): The primary description of the task. Must be a non-empty string.
*   `description` (Optional[str]): An optional, more detailed description of the task. Can be `None`.
*   `completed` (bool): The completion status of the task. `True` if the task is complete, `False` otherwise. Defaults to `False` upon creation.

**Relationships**:

*   None directly relevant to this feature (Todo is a standalone entity within the application's in-memory state).

**Validation Rules**:

*   `id`: Must be a positive integer. When updating, the provided `id` must correspond to an existing `Todo` item in the current list.
*   `title`: Must not be an empty string or contain only whitespace. (Validation already present in `__post_init__` of `Todo` dataclass).
*   `completed`: Must be a boolean value (`True` or `False`).

**State Transitions**:

*   The `completed` attribute can transition from `False` to `True` (marked as complete) and from `True` to `False` (marked as incomplete).
