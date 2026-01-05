# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
All development must follow strict Spec-Driven Development methodology: Specifications written → Tasks derived → Tests written → Implementation follows; No manual coding without spec and task traceability; Every change must be traceable to a spec and task ID.

### II. Console/CLI Interface Only
The application must provide a console-based CLI interface only: Text in/out protocol: stdin/args → stdout, errors → stderr; Support human-readable console output with clear formatting; No GUI, web interface, or external API endpoints.

### III. In-Memory Storage (No Persistence)
All data storage must be in-memory only: No file persistence, no database connections, no external storage; Data loss on program termination is acceptable for this phase; State management must be explicit and deterministic.

### IV. Python 3.13+ Standard
All code must use Python 3.13+ features and standards: Leverage latest Python syntax and libraries; Follow PEP 8 style guidelines; Use type hints for all public interfaces; No external dependencies beyond standard library.

### V. Clean Architecture and Separation of Concerns
Maintain clear architectural boundaries: Separation between business logic, data access, and presentation layers; Dependency inversion where appropriate; Single responsibility principle for all modules and functions; Explicit state management with pure functions where possible.

### VI. Testability and Deterministic Behavior

All functions must be testable and produce deterministic outputs: Pure functions preferred for business logic; Clear input/output contracts; Predictable behavior regardless of execution environment; Comprehensive unit test coverage required.

## Constraints and Requirements

- Language: Python 3.13+
- Interface: Console/CLI only
- Storage: In-memory only (no files, no database)
- Development style: Strict Spec-Driven Development
- No manual coding allowed (must follow spec and tasks)
- Clean architecture and separation of concerns
- Each task must be traceable to a spec and task ID

## Prohibited Elements

- External databases
- Web frameworks
- AI features
- File persistence
- Manual coding without spec/task traceability
- External dependencies beyond Python standard library
- GUI or web interfaces

## Development Workflow

- Strict adherence to Spec-Driven Development cycle
- Specifications must be complete before task creation
- Tasks must be traceable to specific spec requirements
- Implementation must follow task definitions precisely
- All changes require spec → task → implementation traceability
- Code reviews must verify constitution compliance

## Governance

This constitution supersedes all other development practices for the Evolution of Todo project. All development activities must comply with these principles. Amendments require explicit documentation, approval from project stakeholders, and a migration plan for existing code. All pull requests and code reviews must verify compliance with these principles. Code that violates these principles must be refactored to achieve compliance.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28

## Phase 2 Addendum: Full-Stack Web Application

### Phase 2 Constraints

- Full-stack web application
- Frontend: Next.js
- Backend: FastAPI (Python)
- Database: PostgreSQL (Neon)
- REST API communication
- No AI features in this phase

### Phase 2 Principles

- Phase 1 functionality must remain intact
- API-first design
- Clear separation between frontend and backend
- Secure, minimal, and scalable architecture

### Phase 2 Governance

All Phase 2 development activities must comply with both the original constitution and these Phase 2 addendum principles. Phase 1 CLI functionality must be preserved and not broken by Phase 2 changes. The architecture must maintain clear separation between frontend and backend components while ensuring secure communication through well-defined REST APIs.

**Phase 2 Version**: 2.0.0 | **Phase 2 Ratified**: 2025-12-29 | **Phase 2 Last Amended**: 2025-12-29
