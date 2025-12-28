---
description: "Task list for implementing the Delete Todo Item feature."
---

# Tasks: Delete Todo Item

**Input**: Design documents from `specs/002-delete-todo/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli.md

**Tests**: Tests are included as per the TDD principle noted in the implementation plan.

**Organization**: All tasks are part of a single user story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

*This phase is skipped as the project and core structure are already in place.*

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that must be complete before user stories.

*This phase is skipped as the necessary service and CLI files already exist.*

---

## Phase 3: User Story 1 - Delete an existing todo item (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to be able to delete a specific todo item from my list so that I can keep my todo list clean and up-to-date.

**Independent Test**: This can be tested by adding a todo item, deleting it by its ID, and then verifying it is no longer in the list when viewing all todos.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T001 [P] [US1] Add unit test for `delete_todo` method in `tests/unit/test_service.py`. The test should create a todo, delete it, and verify it's no longer in the service's list.
- [ ] T002 [P] [US1] Add integration test for the `todo delete <id>` command in `tests/integration/test_cli.py`. This test should invoke the CLI command and check for a success message and the removal of the item.

### Implementation for User Story 1

- [ ] T003 [US1] Implement the `delete_todo(todo_id: int)` method in `src/todo/service.py` to remove a todo item from the in-memory list.
- [ ] T004 [US1] Add the `delete` sub-command to the argument parser in `src/todo/cli.py` and call the `todo_service.delete_todo` method.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase N: Polish & Cross-Cutting Concerns

*This phase is skipped as no polishing or cross-cutting concerns have been identified for this simple feature.*

---

## Dependencies & Execution Order

### Phase Dependencies

- **User Story 1**: Can start immediately.

### Within User Story 1

- **T001** and **T002** can be done in parallel.
- **T003** (Service implementation) should be done after **T001** (Service test) is written and failing.
- **T004** (CLI implementation) should be done after **T002** (CLI test) is written and failing, and after **T003** is complete.
- **Order**: (T001 -> T003), (T002 -> T004).

### Parallel Opportunities

- The two test creation tasks (T001, T002) can be worked on in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Write and fail the tests in **T001** and **T002**.
2.  Implement the service logic in **T003** to make the unit test pass.
3.  Implement the CLI logic in **T004** to make the integration test pass.
4.  **STOP and VALIDATE**: Manually run `todo add "test"` and `todo delete 1` to confirm functionality.
