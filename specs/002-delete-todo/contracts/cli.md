# CLI Contract: Delete Todo Item

**Feature Branch**: `002-delete-todo`
**Created**: 2025-12-28
**Source**: Feature Specification (specs/002-delete-todo/spec.md)

## Command: `todo delete`

### Purpose

To permanently remove an existing todo item from the in-memory list, identified by its unique ID.

### Usage

`todo delete <ID>`

### Arguments

*   **`<ID>` (Positional)**:
    *   **Type**: Integer
    *   **Required**: Yes
    *   **Description**: The unique identifier of the todo item to be deleted.
    *   **Validation**: Must be a positive integer corresponding to an existing todo item.

### Options

This command has no options.

### Behavior

*   The command will look for a todo item matching the provided `<ID>`.
*   If found, the todo item will be removed from the list.
*   If not found, an error message will be displayed.

### Output (Success)

Upon successful deletion, the CLI will output a confirmation message including the ID of the item that was removed.

**Example**:
`Success: Todo item with ID <ID> has been deleted.`

### Output (Error)

*   **Invalid ID (Not Found)**: If `<ID>` does not correspond to an existing todo item.
    *   **Example**: `Error: Todo item with ID <ID> not found.`
*   **Invalid ID (Format)**: If `<ID>` is not a valid integer.
    *   **Example**: `Error: Invalid ID. Please provide a valid integer.`
*   **Missing ID**: If no `<ID>` is provided with the command.
    *   **Example**: `Error: Missing required argument <ID>.`
*   **General Error**: For other unexpected issues.
    *   **Example**: `An unexpected error occurred.`
