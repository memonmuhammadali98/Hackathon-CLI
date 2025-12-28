# CLI Contract: Update Todo Item

**Feature Branch**: `001-update-todo-item`  
**Created**: 2025-12-27  
**Source**: Feature Specification (specs/001-update-todo-item/spec.md)

## Command: `todo update`

### Purpose

To modify the title and/or description of an existing todo item identified by its unique ID.

### Usage

`todo update <ID> [--title "New Title"] [--description "New Description"]`

### Arguments

*   **`<ID>` (Positional)**:
    *   **Type**: Integer
    *   **Required**: Yes
    *   **Description**: The unique identifier of the todo item to be updated.
    *   **Validation**: Must be a positive integer corresponding to an existing todo item.

### Options

*   **`--title <TEXT>` (Optional)**:
    *   **Type**: String
    *   **Description**: The new title for the todo item. If provided, the existing title will be replaced.
    *   **Validation**: Cannot be empty or consist solely of whitespace.
*   **`--description <TEXT>` (Optional)**:
    *   **Type**: String
    *   **Description**: The new description for the todo item. If provided, the existing description will be replaced. Can be an empty string to clear the description.

### Behavior

*   If only `--title` is provided, only the title is updated.
*   If only `--description` is provided, only the description is updated.
*   If both `--title` and `--description` are provided, both are updated.
*   If neither `--title` nor `--description` is provided (after `<ID>`), the command should provide an error message (e.g., "Nothing to update. Please provide --title or --description.").
*   The `completion status` of the todo item remains unchanged.

### Output (Success)

Upon successful update, the CLI will output a confirmation message including the updated todo details (ID, new title, new description).

**Example**:
`Todo [ID] updated successfully:`
`  ID: <ID>`
`  Title: "New Title"`
`  Description: "New Description"`

### Output (Error)

*   **Invalid ID**: If `<ID>` is not a valid integer or does not correspond to an existing todo.
    *   **Example**: `Error: Todo with ID <ID> not found.`
*   **Empty/Invalid Title**: If `--title` is provided but is empty or only whitespace.
    *   **Example**: `Error: Title cannot be empty.`
*   **No Update Arguments**: If neither `--title` nor `--description` is provided.
    *   **Example**: `Error: Nothing to update. Please provide --title or --description.`
*   **General Error**: For other unexpected issues.
    *   **Example**: `Error: An unexpected error occurred.`
