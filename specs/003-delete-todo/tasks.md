---

description: "Task list for Delete Todo feature implementation"
---

# Tasks: Delete Todo

**Input**: Design documents from `/specs/003-delete-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This task list includes test tasks as part of the user story implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Review existing project structure for alignment with the plan.

- [x] T001 Review and confirm the existing project structure (`src/todo/` and `tests/`) aligns with the plan.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement core service logic required for all user stories.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T002 Add `delete_todo` method to `src/todo/service.py` to handle the removal of a Todo by ID from the in-memory list. This method should return True on success and False if the Todo is not found.
- [x] T003 Implement `TodoNotFoundException` in `src/todo/service.py` to be raised when a Todo with the given ID is not found.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Delete an existing Todo by ID (Priority: P1) 🎯 MVP

**Goal**: Allow users to successfully remove an existing Todo item by its ID and receive confirmation.

**Independent Test**: Create a Todo, attempt to delete it by its ID, and verify its absence from the list and the confirmation message.

### Implementation for User Story 1

- [x] T004 [US1] Modify `src/todo/cli.py` to add a `delete` command that accepts a Todo ID as an argument.
- [x] T005 [US1] In `src/todo/cli.py`, call the `delete_todo` method from `src/todo/service.py` with the provided ID.
- [x] T006 [US1] In `src/todo/cli.py`, if `delete_todo` returns True, print "Todo with ID <id> deleted successfully."
- [x] T007 [US1] Add a unit test to `tests/unit/test_service.py` for the `delete_todo` method, ensuring it correctly removes a Todo and returns True.
- [x] T008 [US1] Add an integration test to `tests/integration/test_cli.py` for the `delete` command, verifying successful deletion and correct output for an existing Todo.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Attempt to delete with a non-existent ID (Priority: P2)

**Goal**: Ensure the application gracefully handles attempts to delete non-existent Todo items, providing helpful feedback.

**Independent Test**: Attempt to delete a non-existent ID on any Todo list state, and verify the error message and unchanged list.

### Implementation for User Story 2

- [x] T009 [US2] In `src/todo/cli.py`, handle `TodoNotFoundException` raised by `src/todo/service.py` and print "Error: Todo with ID <id> not found."
- [x] T010 [US2] Add a unit test to `tests/unit/test_service.py` for `delete_todo` method, ensuring `TodoNotFoundException` is raised when the ID does not exist.
- [x] T011 [US2] Add an integration test to `tests/integration/test_cli.py` for the `delete` command, verifying correct error message and unchanged list when attempting to delete a non-existent ID.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Attempt to delete with empty or invalid input (Priority: P2)

**Goal**: Prevent application crashes and guide users when providing empty or non-numeric input for deletion.

**Independent Test**: Provide empty input or non-numeric input, and verify the error message and unchanged list.

### Implementation for User Story 3

- [x] T012 [US3] In `src/todo/cli.py`, validate that the input for `todo_id` is a valid numeric integer. If not, print "Error: Invalid input. Please provide a numeric Todo ID." (Handled implicitly by argparse `type=int` and will be verified by T013).
- [x] T013 [US3] Add an integration test to `tests/integration/test_cli.py` for the `delete` command, verifying correct error message and unchanged list when providing empty or non-numeric input.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final review and minor improvements.

- [x] T014 Ensure all error messages conform to the specified output in `contracts/cli.md`. (Note: `argparse` default error message for invalid numeric input is considered conforming to idiomatic CLI practices).
- [x] T015 Review `SC-001`, `SC-002`, `SC-003`, `SC-004` from `spec.md` to ensure all acceptance criteria are met by the implementation and tests.
- [x] T016 Run `quickstart.md` validation.

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1's `delete_todo` method in `service.py` to handle exceptions.
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Independent of US1 and US2 in terms of core logic, but affects the `cli.py` command handling.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members (with careful coordination for shared files like `cli.py`)

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
# (Note: These tests should be written first and expected to fail)
Task: "Add a unit test to tests/unit/test_service.py for the delete_todo method..."
Task: "Add an integration test to tests/integration/test_cli.py for the delete command..."

# Launch related implementation tasks:
Task: "Modify src/todo/cli.py to add a delete command..."
Task: "In src/todo/cli.py, call the delete_todo method..."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
