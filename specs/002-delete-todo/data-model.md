# Data Model: Delete Todo Item

**Feature Branch**: `002-delete-todo`
**Created**: 2025-12-28
**Source**: Feature Specification (specs/002-delete-todo/spec.md)

## Key Entities

### Todo Item

Represents a single task managed by the CLI application. This is the entity the "Delete Todo" feature acts upon.

**Attributes**:

*   **ID**:
    *   **Type**: Integer
    *   **Description**: A unique identifier for the todo item.
    *   **Constraints**: Must be a positive integer, unique across all todo items. This is used to target which item to delete.
*   **Title**:
    *   **Type**: String
    *   **Description**: A concise, mandatory description of the task.
*   **Description**:
    *   **Type**: String
    *   **Description**: An optional, longer string providing additional details or context for the task.
*   **Completion Status**:
    *   **Type**: Boolean
    *   **Description**: Indicates whether the task has been marked as complete.

## Relationships

*   **Todo List**: The application maintains an in-memory collection (e.g., a list or dictionary) of `Todo Item` entities. The `Delete Todo` feature interacts with this collection to locate and remove a specific `Todo Item` by its ID.

## State Transitions (for `Todo Item`)

*   A `Todo Item` is created with an ID, Title, Description (optional), and initial Completion Status.
*   The `Delete Todo` feature identifies a `Todo Item` by its `ID`.
*   Upon successful deletion, the `Todo Item` is permanently removed from the in-memory `Todo List` collection. The state of the item ceases to exist within the application's runtime memory.
