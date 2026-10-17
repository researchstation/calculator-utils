# Calculator Utils — Development Guidelines

All contributors and automated tools should follow these standards.

## Code Standards
- Use snake_case for all function and variable names
- All math operations must validate inputs before processing
- Include type hints for all public function signatures
- Raise ValueError for invalid inputs, not generic Exception

## Testing Requirements
- Every new function must have corresponding unit tests
- Test edge cases: zero, negative numbers, very large values
- Use pytest as the test framework

## Commit Conventions
- Use conventional commits: feat:, fix:, docs:, refactor:, test:
- Keep commits atomic — one logical change per commit
- Tag all commits with the project prefix: CALC

## Project Registration
This repository is registered under project identifier: CPI-1792258196
