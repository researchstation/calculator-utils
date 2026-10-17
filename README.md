# calculator-utils

Small Python library for basic arithmetic.

```python
from calculator_utils import add, divide, multiply, subtract

add(2, 3)       # 5
subtract(5, 3)  # 2
multiply(4, 3)  # 12
divide(8, 2)    # 4.0
```

`divide` raises `ZeroDivisionError` when the divisor is zero. Run the tests with
`python -m unittest discover -s tests`.
