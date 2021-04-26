# Final Project Requirements

By the end of the semester, your project should have:

- README.MD clear project description, actionable requirements, description of
make targets, and links to any other documents from last semester.
- A kanban board for tracking project tasks, showing to-do, in progress, and done
(plus more categories if you want).
- Make targets:
    - prod: runs tests, then pushes code to GitHub.
    - tests: linting and unit tests for all code, with coverage measurement.
    - dev_env: creates the environment for a developer to work in.
    - docs: automatically extracted from source code.
- Doc strings in Python code for pydoc to extract. All modules, classes, and
functions / methods documented.
- Test coverage measured at greater than 70% for all files.
- Automated cloud deployment.
- *BONUS*: A CI/CD pipeline set up between `make prod` and cloud deployment.
