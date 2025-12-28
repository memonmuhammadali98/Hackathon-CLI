# CLI Contract: Mark Todo as Complete / Incomplete

**Date**: 2025-12-28
**Feature**: Mark Todo as Complete / Incomplete
**Branch**: 003-mark-todo-status

## Command

The new functionality will be exposed as a sub-command under the main `todo` CLI utility.

### `todo mark-status <ID> --status <STATUS>`

**Description**: Updates the completion status of a specific todo item.

**Arguments**:

*   `<ID>` (required, integer): The unique identifier of the todo item to update.
*   `--status` (required, string): The desired status for the todo item.
    *   **Allowed values**: `complete`, `incomplete`

**Example Usage**:

```bash
todo mark-status 1 --status complete
todo mark-status 5 --status incomplete
```

## Output & Feedback

### Success Messages

*   **Syntax**: `Todo <ID> marked as <status>.`
*   **Example**:
    ```
    Todo 1 marked as complete.
    Todo 5 marked as incomplete.
    ```
*   **Note**: If the todo is already in the requested status, the system will still confirm the status (e.g., "Todo 1 marked as complete." even if it was already complete). This is acceptable as per `spec.md` User Story 1, Acceptance Scenario 3 and User Story 2, Acceptance Scenario 2.

### Error Messages

*   **Scenario**: Todo with specified ID not found.
    *   **Syntax**: `Error: Todo with ID <ID> not found.`
    *   **Example**: `Error: Todo with ID 99 not found.`
*   **Scenario**: Invalid status value provided.
    *   **Syntax**: `Error: Invalid status. Please use 'complete' or 'incomplete'.`
    *   **Example**: `Error: Invalid status. Please use 'complete' or 'incomplete'.`
*   **Scenario**: ID is not a valid integer.
    *   **Syntax**: `Error: <INVALID_ID_INPUT> is not a valid integer for Todo ID.`
    *   **Example**: `Error: abc is not a valid integer for Todo ID.`
