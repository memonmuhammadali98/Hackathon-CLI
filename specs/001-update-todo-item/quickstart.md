# Quickstart: Update Todo Item

**Feature Branch**: `001-update-todo-item`  
**Created**: 2025-12-27  
**Source**: Feature Specification (specs/001-update-todo-item/spec.md)

This quickstart guide provides basic examples of how to use the `todo update` command to modify existing todo items.

---

## 1. Prerequisites

Before using the `update` command, ensure you have an existing todo item. If not, you can create one (assuming a `todo add` command exists):

```bash
todo add "Buy groceries" --description "Milk, eggs, bread"
# Expected output:
# Todo added:
#   ID: 1
#   Title: "Buy groceries"
#   Description: "Milk, eggs, bread"
```

## 2. Update a Todo Item's Title

To change only the title of an existing todo item, use its ID and the `--title` option:

```bash
todo update 1 --title "Buy healthy groceries"
# Expected output:
# Todo 1 updated successfully:
#   ID: 1
#   Title: "Buy healthy groceries"
#   Description: "Milk, eggs, bread"
```

## 3. Update a Todo Item's Description

To change only the description of an existing todo item, use its ID and the `--description` option:

```bash
todo update 1 --description "Milk, eggs, whole wheat bread"
# Expected output:
# Todo 1 updated successfully:
#   ID: 1
#   Title: "Buy healthy groceries"
#   Description: "Milk, eggs, whole wheat bread"
```

## 4. Clear a Todo Item's Description

To remove an existing description, you can provide an empty string to the `--description` option:

```bash
todo update 1 --description ""
# Expected output:
# Todo 1 updated successfully:
#   ID: 1
#   Title: "Buy healthy groceries"
#   Description: ""
```

## 5. Update Both Title and Description

You can update both the title and description in a single command:

```bash
todo update 1 --title "Buy fruit and veggies" --description "Apples, bananas, spinach"
# Expected output:
# Todo 1 updated successfully:
#   ID: 1
#   Title: "Buy fruit and veggies"
#   Description: "Apples, bananas, spinach"
```

## 6. Handling Invalid ID

Attempting to update a todo with a non-existent ID will result in an error:

```bash
todo update 99 --title "Non-existent todo"
# Expected output:
# Error: Todo with ID 99 not found.
```

## 7. Handling Empty Title

Attempting to update a todo with an empty title will result in an error:

```bash
todo update 1 --title ""
# Expected output:
# Error: Title cannot be empty.
```
