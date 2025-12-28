# Quickstart: View Todo List Feature

This guide provides a quick overview of how to use the "View Todo List" feature in the CLI Todo application.

## Prerequisites

*   The CLI Todo application must be installed and accessible via the `todo` command.
*   You should have some todo items added to the in-memory list (e.g., using the `todo add` command if available).

## Viewing Your Todo List

To view all your current todo items, simply run the `view` command:

```bash
todo view
```

### Example Output (with items)

If you have added some todo items, the output will look similar to this:

```
[ ] 1: Buy groceries - Milk, eggs, bread
[x] 2: Finish report - Draft executive summary
[ ] 3: Call mom
```

*   `[ ]` indicates an incomplete todo item.
*   `[x]` indicates a completed todo item.
*   The number is the unique ID of the todo item.
*   The text after the ID is the title.
*   The text after the title (if present) is the description.

### Example Output (empty list)

If there are no todo items in your list, the application will inform you:

```
No todo items found.
```

## Next Steps

*   To add new todo items, refer to the documentation for the `todo add` command.
*   To mark todo items as complete, refer to the documentation for the `todo complete` command (future feature).