# Quickstart: Delete Todo Item

**Feature Branch**: `002-delete-todo`
**Created**: 2025-12-28
**Source**: Feature Specification (specs/002-delete-todo/spec.md)

This quickstart guide provides basic examples of how to use the `todo delete` command to remove existing todo items.

---

## 1. Prerequisites

Before using the `delete` command, ensure you have an existing todo item. If not, you can create one (assuming a `todo add` command exists):

```bash
todo add "Task to be deleted" --description "This is a test."
# Expected output:
# Todo added:
#   ID: 1
#   Title: "Task to be deleted"
#   Description: "This is a test."
```

## 2. Delete an Existing Todo Item

To permanently remove a todo item, use the `delete` command followed by the item's ID:

```bash
todo delete 1
# Expected output:
# Success: Todo item with ID 1 has been deleted.
```

## 3. Handling Invalid ID

Attempting to delete a todo with a non-existent ID will result in an error:

```bash
todo delete 99
# Expected output:
# Error: Todo item with ID 99 not found.
```

## 4. Handling Non-Numeric ID

Attempting to delete a todo with a non-numeric ID will result in an error:

```bash
todo delete abc
# Expected output:
# Error: Invalid ID. Please provide a valid integer.
```

## 5. Handling Missing ID

Calling the `delete` command without an ID will result in an error:

```bash
todo delete
# Expected output:
# Error: Missing required argument <ID>.
```
