# Fibonacci Number

## Problem Description

The Fibonacci sequence is defined as follows:

- `fib(0) = 0`
- `fib(1) = 1`
- For `n >= 2`, `fib(n) = fib(n-1) + fib(n-2)`

Given an integer `n`, return the `n`th Fibonacci number.

### Example 1:

**Input:** `n = 2`  
**Output:** `1`  
**Explanation:** The Fibonacci sequence is: 0, 1, 1. Therefore, `fib(2)` is 1.

### Example 2:

**Input:** `n = 3`  
**Output:** `2`  
**Explanation:** The Fibonacci sequence is: 0, 1, 1, 2. Therefore, `fib(3)` is 2.

### Example 3:

**Input:** `n = 4`  
**Output:** `3`  
**Explanation:** The Fibonacci sequence is: 0, 1, 1, 2, 3. Therefore, `fib(4)` is 3.

## Constraints

- `0 <= n <= 30`

---

## Solution

### Python Code:

```python
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr
