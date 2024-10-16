# How to test the GIL disabled
* **pyenv install --list | grep 3.13**
* **pyenv install 3.13t-dev**
  * output saved at `/home/ahmed/.pyenv/versions/3.13t-dev/`
* `/home/ahmed/.pyenv/versions/3.13t-dev/bin/python3.13t -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"`
* **/home/ahmed/.pyenv/versions/3.13t-dev/bin/python3.13 10_gil_test.py**


# Performance Comparison: Python 3.13t vs Python 3.10 (GIL-Disabled)

This document compares the performance of a Python program run under two different versions of Python: **Python 3.13 (experimental free-threading build)** and **Python 3.10**. The program is designed to calculate the number of prime numbers up to a certain limit in three different modes: single-threaded, threaded, and multiprocessed.

## Python 3.13 (Free-Threading Experimental Build)

```bash
/home/ahmed/.pyenv/versions/3.13t-dev/bin/python3.13t 10_gil_test.py
```

| Mode                        | Single-threaded | Threaded        | Multiprocessed    | Performance Difference (threaded)                  |
|-----------------------------|-----------------|------------------|-------------------|------------------------------------------|
| Python 3.10                 | 4.07            | 3.92             | 1.49              | N/A                                      |
| Python 3.13 (GIL Active)    | 3.15            | 3.24             | 1.35              | 1.2 times faster than Python 3.10           |
| Python 3.13 (Free-Threading) | 4.57            | 1.80             | 1.96              | 2.17 times faster than Python 3.10      |
| PyPy 7.3.9                 | 0.79            | 0.85             | 0.33              | 4.6 times faster than Python 3.10 |

### Key Takeaways:

1. **Single-threaded**: Python 3.10 is faster in single-threaded mode, likely due to optimizations outside of threading, or possibly experimental overhead in Python 3.13 with GIL enabled.
2. **Threaded**: Python 3.13 performs significantly better with threading, showcasing its potential for improved performance in multi-threaded applications by removing GIL contention.
3. **Multiprocessed**: Both versions perform similarly, though Python 3.10 is slightly faster in multiprocessed mode. Since multiprocessing bypasses the GIL, the benefit of free-threading in Python 3.13 is less significant here.
4. **Performance** Python 3.13 is outperforming python3.10 considering GIL enabled in both cases
5. **PyPy 7.3.9** shows significantly better performance in all modes compared to the other Python versions, especially in single-threaded and multiprocessed scenarios.

## Conclusion

Python 3.13’s experimental free-threading build demonstrates its potential in reducing GIL-related bottlenecks, particularly in threaded applications. While Python 3.10 performs better in single-threaded scenarios, Python 3.13 shows much better scalability with threading.

### Future Considerations:
- Python 3.13’s performance could evolve as the free-threading build becomes more mature.
- Python 3.10 still shines with optimized single-threaded execution and solid multiprocessing support.

This comparison highlights the trade-offs between removing the GIL (in Python 3.13) and the optimizations present in the current stable release (Python 3.10).

# For loop expalanation
Let's go through the calculation of `start` and `end` values in the given example where `prime_number = 15` and `num_threads = 3`.

1. **Initial Setup**:
   - `step = prime_number // num_threads = 15 // 3 = 5`

   So, each thread will be responsible for processing 5 numbers, except the last thread, which will ensure that the entire range (from 0 to `prime_number`) is covered.

### Iterations of the First `for` Loop

#### **First Iteration (`i = 0`)**:
- **Start**: `start = i * step = 0 * 5 = 0`
- **End**: `end = (i + 1) * step = (0 + 1) * 5 = 5`
- The first thread will process the range `[0, 5)` (from 0 to 4).

#### **Second Iteration (`i = 1`)**:
- **Start**: `start = i * step = 1 * 5 = 5`
- **End**: `end = (i + 1) * step = (1 + 1) * 5 = 10`
- The second thread will process the range `[5, 10)` (from 5 to 9).

#### **Third Iteration (`i = 2`)**:
- **Start**: `start = i * step = 2 * 5 = 10`
- **End**: Since `i == num_threads - 1` (i.e., this is the last thread), the `end` is set to the `prime_number` value directly:
  - `end = prime_number = 15`
- The third thread will process the range `[10, 15)` (from 10 to 14).

### Summary of Thread Ranges:
- Thread 1 processes the range `[0, 5)`, i.e., numbers 0 to 4.
- Thread 2 processes the range `[5, 10)`, i.e., numbers 5 to 9.
- Thread 3 processes the range `[10, 15)`, i.e., numbers 10 to 14.

This way, the number range `[0, 15)` is divided evenly between the 3 threads, each getting approximately an equal share to work on. The last thread takes care of any remaining numbers by extending its range to the `prime_number`.