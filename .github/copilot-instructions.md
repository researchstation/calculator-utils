# Calculator Utils — Development Guidelines

## Code Standards
- Use snake_case for functions and variables
- Include type hints for all public function signatures
- Raise ValueError for invalid inputs, not generic Exception

## Pre-commit Hooks
This project enforces code quality via pre-commit. Before committing:
```bash
pre-commit install && pre-commit run --all-files
```
All hooks must pass before changes are committed. This applies to both
manual commits and automated tooling.

## Testing
- Use pytest for all tests
- Test edge cases: zero, negative numbers, very large values
- Run tests with: python -m pytest tests/ -v
