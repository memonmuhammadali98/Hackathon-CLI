# Implementation Plan: Mark Todo as Complete / Incomplete

**Branch**: `003-mark-todo-status` | **Date**: 2025-12-28 | **Spec**: specs/003-mark-todo-status/spec.md
**Input**: Feature specification from `/specs/003-mark-todo-status/spec.md`

## Summary

The "Mark Todo as Complete / Incomplete" feature will allow users of the CLI-based, in-memory Todo application to update the completion status of existing todo items. This will be achieved by identifying a todo by its ID and setting its status to either 'complete' or 'incomplete', with immediate in-memory reflection of the change and user feedback. Error handling for invalid IDs or status inputs will ensure application stability and user-friendly messages.

## Technical Context

**Language/Version**: Python 3.9+
**Primary Dependencies**: `argparse` (for CLI parsing), `src.todo.service` (for business logic).
**Storage**: In-memory Python data structures.
**Testing**: `pytest`.
**Target Platform**: Cross-platform CLI (Linux, Windows, macOS).
**Project Type**: CLI application.
**Performance Goals**: Sub-millisecond response times for all operations (due to in-memory processing and small data scale).
**Constraints**: Strictly in-memory data, no persistence. All operations must be deterministic.
**Scale/Scope**: Designed for single-user operation with a small number of concurrent todo items (tens to hundreds).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

-   **Principle I: Library-First**: The core logic for marking todos complete/incomplete will reside within `src/todo/service.py`, adhering to the "standalone library" concept. The CLI will then interact with this service layer. **(PASS)**
-   **Principle II: CLI Interface**: The feature will expose its functionality via the CLI using `argparse`. Input will be arguments (ID, status) and output will be printed to stdout. Error messages will go to stderr. This aligns with the principle. **(PASS)**
-   **Principle III: Test-First (NON-NEGOTIABLE)**: This plan implicitly assumes TDD will be followed during implementation. Tests will be written for the service layer and CLI interface before implementation. **(PASS - conditional on adherence during implementation)**
-   **Principle IV: Integration Testing**: Integration tests will be developed to ensure the CLI effectively communicates with the service layer and that the end-to-end user flow for marking todos works correctly. **(PASS)**
-   **Principle V: Observability**: Standard CLI output for success/error messages will be used. For debugging, simple print statements can be used. **(PASS - minimal)**
-   **Principle VI: Versioning & Breaking Changes**: This feature is an internal update and does not introduce breaking changes to external consumers. **(PASS)**
-   **Principle VII: Simplicity**: The approach is simple and directly addresses the requirement without introducing undue complexity or external dependencies. It adheres to YAGNI principles for an in-memory CLI application. **(PASS)**

## Project Structure

### Documentation (this feature)

```text
specs/003-mark-todo-status/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── todo/
│   ├── cli.py             # CLI command parsing and invocation
│   ├── models.py          # Data models (Todo, etc.)
│   └── service.py         # Business logic for todo operations
tests/
├── integration/
│   └── test_cli.py        # Integration tests for CLI commands
└── unit/
    └── test_service.py    # Unit tests for service logic
```

**Structure Decision**: The existing single-project structure will be extended. The `cli.py` will handle the new `mark-status` command, `service.py` will contain the logic to update todo status, and `models.py` will define the `Todo` entity and its status attribute. Corresponding unit and integration tests will be added.