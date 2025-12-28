---

description: "Task list for the View Todo List feature implementation"
---

# Tasks: View Todo List

**Input**: Design documents from `/specs/001-view-todo-list/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification does not explicitly request generating test tasks. Tests will be covered during implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure verification.

- [x] T001 Verify Python 3.11 environment in the project.
- [x] T002 Ensure `src/todo/models.py` exists for `TodoItem` definition.
- [x] T003 Ensure `src/todo/service.py` exists for todo item management.
- [x] T004 Ensure `src/todo/cli.py` exists for CLI command handling.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T005 Implement the `TodoItem` class in `src/todo/models.py` with `id`, `title`, `description`, and `status` attributes as per `data-model.md`.
- [x] T006 Implement an in-memory storage mechanism (e.g., a list or dictionary) for `TodoItem` objects in `src/todo/service.py`.
- [x] T007 Implement a `get_all_todos()` method in `src/todo/service.py` that returns all current `TodoItem` objects from the in-memory storage.
- [x] T008 Implement an `add_todo()` method in `src/todo/service.py` for populating todo items for testing and future features (for `todo add` command).

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - View All Todos (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to see a list of all my existing todo items, including their IDs, titles, descriptions, and completion status, so I can quickly review my tasks.

**Independent Test**: Add several todo items (some completed, some not) using the `add_todo()` service method, then invoke the `todo view` command, and verify the output matches the expected format (ID, title, description, and completion status), with completed items visually distinguishable and the order maintained as added.

### Implementation for User Story 1

- [x] T009 [US1] Add a `view` command entry point to `src/todo/cli.py` as defined in `contracts/cli.md`.
- [x] T010 [US1] Inside the `view` command in `src/todo/cli.py`, call the `get_all_todos()` method from `src/todo/service.py`.
- [x] T011 [US1] Implement logic in `src/todo/cli.py` to iterate through the retrieved `TodoItem` objects and format each one according to the output structure in `contracts/cli.md` (e.g., `[ ] ID: Title - Description`).
- [x] T012 [US1] Ensure visual distinction for completed items (e.g., prefix `[x]` for completed, `[ ]` for incomplete) in `src/todo/cli.py`.
- [x] T013 [US1] Ensure the output order of todo items in `src/todo/cli.py` matches the order returned by `get_all_todos()` (which should reflect the order they were added).

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - View Empty Todo List (Priority: P1)

**Goal**: As a user, I want the application to handle an empty todo list gracefully, so I understand there are no tasks without the application crashing or displaying errors.

**Independent Test**: Invoke the `todo view` command when no todo items have been added (i.e., `get_all_todos()` returns an empty list), and verify the application does not crash and displays the message "No todo items found.".

### Implementation for User Story 2

- [x] T014 [US2] Modify the `view` command in `src/todo/cli.py` to check if the list returned by `get_all_todos()` is empty.
- [x] T015 [US2] If the list is empty, print "No todo items found." to the console from `src/todo/cli.py`, as specified in `contracts/cli.md`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories or the overall project quality.

- [x] T016 Review all code in `src/todo/cli.py`, `src/todo/models.py`, `src/todo/service.py` for adherence to Python best practices and project conventions.
- [x] T017 Update `src/main.py` (if necessary) to correctly initialize and run the CLI application, ensuring the `todo view` command is accessible.
- [x] T018 Add/update comments and docstrings in `src/todo/cli.py`, `src/todo/models.py`, `src/todo/service.py` for clarity and maintainability.
- [x] T019 Validate the implementation against `quickstart.md` to ensure the steps and examples are still accurate.
- [x] T020 Consider adding basic unit tests for `src/todo/service.py` (e.g., `get_all_todos` with empty and non-empty lists) in `tests/unit/test_service.py` to improve code robustness.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 by checking for an empty list *before* attempting to display items. Functionally, US1's display logic is built upon after US2's empty check.

### Within Each User Story

- Models before services
- Services before endpoints (CLI command logic)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks can run in parallel.
- Foundational tasks T005, T006, T007, T008 can be developed in parallel as they cover different parts of the service and model layer.
- Once Foundational phase completes, User Story 1 and User Story 2 tasks, particularly those operating on different files, can have some parallel execution. For example, `T009` (add view command) can be done while `T005` (implement TodoItem) is in progress, as long as the CLI command's logic doesn't depend on the complete implementation of the service methods. However, for simplicity and clearer dependencies, a sequential approach within a story is recommended.
- Polish tasks (T016, T017, T018, T019) can be done in parallel for different files/aspects. T020 (unit tests) can be done in parallel to other polish tasks.

---

## Parallel Example: User Story 1

```bash
# Models before services:
Task: "Implement the `TodoItem` class in src/todo/models.py" (Foundational)
Task: "Implement an in-memory storage mechanism for `TodoItem` objects in src/todo/service.py" (Foundational)

# Services before CLI logic:
Task: "Implement a `get_all_todos()` method in src/todo/service.py" (Foundational)
Task: "Implement an `add_todo()` method in src/todo/service.py" (Foundational)

# CLI implementation
Task: "Add a `view` command entry point to src/todo/cli.py" (US1)
Task: "Inside the `view` command in src/todo/cli.py, call the `get_all_todos()` method from src/todo/service.py" (US1)
```

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

The "View Todo List" feature itself can be considered the MVP.
1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. **STOP and VALIDATE**: Test User Stories 1 and 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done, User Story 1 and User Story 2 can be developed. Due to the tight integration (US2 being a check before US1's display logic), it might be more efficient for a single developer or close collaboration.
3. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
