# Quickstart: Delete Todo

This guide provides a quick overview of how to use the "Delete Todo" feature from the command line.

## Prerequisites

*   A running instance of the Todo CLI application.
*   Existing Todo items in your list, ideally with their IDs known (you can usually view these with a `todo list` command, if available).

## How to Delete a Todo

To delete a Todo item, use the `todo delete` command followed by the unique ID of the Todo you wish to remove.

**Syntax**:

```bash
todo delete <todo_id>
```

Replace `<todo_id>` with the actual numeric ID of the Todo item.

**Example**:

If you have a Todo item with ID `123` that you want to delete, you would run:

```bash
todo delete 123
```

### Expected Output

*   **Successful Deletion**:
    If the Todo item with the specified ID exists and is successfully deleted, you will see a confirmation message:
    ```
    Todo with ID 123 deleted successfully.
    ```
*   **Todo Not Found**:
    If you try to delete a Todo with an ID that does not exist in your list, you will receive an error:
    ```
    Error: Todo with ID 999 not found.
    ```
*   **Invalid Input**:
    If you provide non-numeric input or an empty value for the Todo ID, you will get an error message:
    ```
    Error: Invalid input. Please provide a numeric Todo ID.
    ```

## Example Walkthrough

1.  **View your current Todo list (if available)**:
    ```bash
    todo list
    # Example output:
    # ID   Description
    # --   -----------
    # 123  Buy groceries
    # 456  Walk the dog
    ```
2.  **Delete a Todo item**:
    Let's delete "Buy groceries" which has an ID of `123`.
    ```bash
    todo delete 123
    ```
3.  **Confirm deletion**:
    You should see:
    ```
    Todo with ID 123 deleted successfully.
    ```
4.  **Verify the list (optional)**:
    If you view your list again, "Buy groceries" should be gone:
    ```bash
    todo list
    # Example output:
    # ID   Description
    # --   -----------
    # 456  Walk the dog
    ```
