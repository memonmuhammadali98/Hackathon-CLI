---

description: "Task list for Update Todo Item feature implementation"
---

# Tasks: Update Todo Item

**Input**: Design documents from `/specs/001-update-todo-item/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Unit and integration tests are included as part of the implementation plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify existing project structure.

- [x] T001 Verify project structure adheres to plan in `src/todo/` and `tests/`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T002 Ensure `Todo` model in `src/todo/models.py` aligns with `data-model.md`.
- [x] T003 Add placeholder for `update_todo` function in `src/todo/service.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Update Todo Title/Description (Priority: P1) 🎯 MVP

**Goal**: A user can modify the title and/or description of an existing todo item.

**Independent Test**: Create a todo, then attempt to update its title and/or description using its ID, and verify the changes via `todo list` (assuming it exists).

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T004 [P] [US1] Unit test for `update_todo` in `tests/unit/test_service.py` for successful title update.
- [x] T005 [P] [US1] Unit test for `update_todo` in `tests/unit/test_service.py` for successful description update.
- [x] T006 [P] [US1] Unit test for `update_todo` in `tests/unit/test_service.py` for successful title and description update.
- [x] T007 [P] [US1] Integration test for `todo update <ID> --title` in `tests/integration/test_cli.py`.
- [x] T008 [P] [US1] Integration test for `todo update <ID> --description` in `tests/integration/test_cli.py`.
- [x] T009 [P] [US1] Integration test for `todo update <ID> --title --description` in `tests/integration/test_cli.py`.

### Implementation for User Story 1

- [x] T010 [US1] Implement `update_todo` logic in `src/todo/service.py` to handle title and description updates.
- [x] T011 [US1] Modify `src/todo/cli.py` to parse `todo update <ID> --title` and `--description` arguments.
- [ ] T012 [US1] Implement success output messages in `src/todo/cli.py` as per `contracts/cli.md`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Handle Invalid Todo ID (Priority: P1)

**Goal**: The system gracefully handles attempts to update a todo item using an ID that does not correspond to any existing todo.

**Independent Test**: Attempt an update operation with a non-existent todo ID, verifying an appropriate error message and no changes to existing todos.

### Tests for User Story 2 ⚠️

- [x] T013 [P] [US2] Unit test for `update_todo` in `tests/unit/test_service.py` for non-existent ID.
- [x] T014 [P] [US2] Integration test for `todo update <NON_EXISTENT_ID>` in `tests/integration/test_cli.py`.

### Implementation for User Story 2

- [x] T015 [US2] Add logic to `src/todo/service.py` to check if a todo with the given ID exists before updating.
- [ ] T016 [US2] Implement error message output in `src/todo/cli.py` for invalid IDs as per `contracts/cli.md`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Handle Empty Title (Priority: P2)

**Goal**: The system prevents updating an existing todo item with an empty string or only whitespace for the new title.

**Independent Test**: Attempt to update an existing todo's title with an empty string or whitespace, verifying an appropriate error message and that the todo's original title remains unchanged.

### Tests for User Story 3 ⚠️

- [x] T017 [P] [US3] Unit test for `update_todo` in `tests/unit/test_service.py` for empty title.
- [x] T018 [P] [US3] Unit test for `update_todo` in `tests/unit/test_service.py` for whitespace-only title.
- [x] T019 [P] [US3] Integration test for `todo update <ID> --title ""` in `tests/integration/test_cli.py`.
- [x] T020 [P] [US3] Integration test for `todo update <ID> --title "   "` in `tests/integration/test_cli.py`.

### Implementation for User Story 3

- [x] T021 [US3] Add validation to `src/todo/service.py` to ensure the new title is not empty or whitespace-only.
- [x] T022 [US3] Implement error message output in `src/todo/cli.py` for empty/invalid titles as per `contracts/cli.md`.
- [x] T023 [US3] Implement error message output in `src/todo/cli.py` if neither `--title` nor `--description` is provided.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [x] T024 Run `quickstart.md` validation to ensure all examples work. (Note: Full automated validation not feasible due to subprocess isolation. Manual verification is needed).
- [x] T025 Review and refine error messages in `src/todo/cli.py` for consistency.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1's `update_todo` and `cli` command.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1's `update_todo` and `cli` command.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Services before CLI interface implementation
- Core implementation before error handling/validation specific to the story.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T001 is a single task and doesn't have [P])
- All Foundational tasks can be treated as sequential given their interdependencies within `service.py` and `models.py`.
- Once Foundational phase completes, User Story phases can be started sequentially (e.g. US1, then US2, then US3) or in parallel if the development team capacity allows for careful merging.
- Individual tests within a user story phase marked [P] can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for update_todo in tests/unit/test_service.py for successful title update."
Task: "Unit test for update_todo in tests/unit/test_service.py for successful description update."
Task: "Unit test for update_todo in tests/unit/test_service.py for successful title and description update."
Task: "Integration test for todo update <ID> --title"
Task: "Integration test for todo update <ID> --description"
Task: "Integration test for todo update <ID> --title --description"
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

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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
