# Data Model: Update Todo Item

**Feature Branch**: `001-update-todo-item`  
**Created**: 2025-12-27  
**Source**: Feature Specification (specs/001-update-todo-item/spec.md)

## Key Entities

### Todo Item

Represents a single task managed by the CLI application. This is the primary entity for the "Update Todo Item" feature.

**Attributes**:

*   **ID**:
    *   **Type**: Integer
    *   **Description**: A unique identifier for the todo item. Generated upon creation.
    *   **Constraints**: Must be a positive integer, unique across all todo items.
*   **Title**:
    *   **Type**: String
    *   **Description**: A concise, mandatory description of the task.
    *   **Constraints**: Cannot be empty or consist solely of whitespace. Maximum length might be implicitly limited by display capabilities of the CLI.
*   **Description**:
    *   **Type**: String
    *   **Description**: An optional, longer string providing additional details or context for the task.
    *   **Constraints**: Can be empty. Maximum length might be implicitly limited by display capabilities of the CLI.
*   **Completion Status**:
    *   **Type**: Boolean
    *   **Description**: Indicates whether the task has been marked as complete.
    *   **Constraints**: This attribute is explicitly NOT modified by the "Update Todo Item" feature. Its state remains unchanged.

## Relationships

*   **Todo List**: The application maintains an in-memory collection (e.g., a list or dictionary) of `Todo Item` entities. The `Update Todo Item` feature interacts with this collection to locate and modify a specific `Todo Item` by its ID.

## State Transitions (for `Todo Item`)

*   A `Todo Item` is created with an ID, Title, Description (optional), and initial Completion Status (e.g., False).
*   The `Title` and `Description` attributes of an existing `Todo Item` can be modified.
*   The `ID` and `Completion Status` of an existing `Todo Item` are immutable by this feature.
