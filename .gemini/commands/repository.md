# Repository Generator

Read the project context from GEMINI.md before generating code.

Generate a production-ready Repository layer for the requested SQLAlchemy model.

Requirements:

* Follow the Repository Pattern.
* Use Flask SQLAlchemy.
* Use the existing `db` instance.
* Use type hints.
* Add Google-style docstrings.
* Keep business logic out of the repository.
* Use SQLAlchemy ORM queries only.
* Raise exceptions instead of printing errors.
* Follow PEP 8.
* Keep methods reusable.
* Return only the complete Python file.

Implement CRUD methods:

* create
* get_by_id
* get_all
* update
* delete

Also generate any additional lookup methods that make sense for the model.

