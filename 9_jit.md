Here’s the markdown content organized into a table, grouping related files into one row:

# how to run it
you have to install pypy3 version as it's already equipped with JIT compiler
1. python3 filename.py (NO JUT)
2. pypy3 filename.py  (WIT JIT)


```md
# Performance Comparison Table

| Test Case       | Interpreter | Command                            | Execution Time (seconds) | Faster          |
|-----------------|-------------|------------------------------------|--------------------------|-----------------|
| 7_advantage_jit | CPython      | `python3 7_advantage_jit.py`      | 2.8755                   |             |
|                 | PyPy         | `pypy3 7_advantage_jit.py`         | 0.4872                   |PyPy             |
| 8_disadv_jit    | CPython      | `python3 8_disadv_jit.py`         | 1.0843                   | CPython         |
|                 | PyPy         | `pypy3 8_disadv_jit.py`            | 4.4185                   |                 |
```

### Explanation:
- The entries for **CPython** and **PyPy** are grouped under each test case for clarity.
- The **Faster** column indicates which interpreter performed better for each test case.