# Advanced Python Assignment

## Employee Data Processing Pipeline

This project demonstrates the five advanced Python concepts required by the assignment:

| Concept | Implementation |
|---|---|
| Iterator | `EmployeeIterator` |
| Generator | `employee_generator()` and `filter_by_department()` |
| Closure | `create_salary_filter()` |
| Decorator | `@log_execution` |
| Context Manager | `ReportFile` |

## How to Run

Run:

```bash
python main.py
```

Then enter values such as:

```text
Enter department: IT
Enter minimum salary: 60000
```

The program creates `employee_report.txt`.

For the example input, the selected employees are:

```text
103 - David - IT - 65000
105 - Alex - IT - 75000
```

## Six Conceptual Questions

### 1. Iterator

**What is the difference between `iter(employees)` and `next(iterator)`?**

`iter(employees)` obtains an iterator from an iterable object. It prepares an object that can return elements one at a time.

`next(iterator)` actually requests the next element from that iterator. When there are no more elements, it raises `StopIteration`.

In this assignment, `EmployeeIterator.__iter__()` returns the iterator itself and `EmployeeIterator.__next__()` returns the next employee.

### 2. Generator

**Why is `yield` preferred over returning a complete list when processing a very large dataset?**

`yield` produces values lazily, one at a time. It does not need to create and store the entire result list in memory.

This makes generators more memory-efficient and suitable for processing very large datasets or streams of data.

### 3. Generator vs Iterator

**Is a generator an iterator? Explain why.**

Yes. A generator is a special type of iterator.

A generator function uses `yield`. Calling the function returns a generator object, which implements the iterator protocol and can be used with `next()` and `for` loops. It keeps track of its execution state between yielded values.

### 4. Closure

**Why does `check()` still know the value of `min_salary` after `create_salary_filter()` has finished?**

`check()` is an inner function that references `min_salary` from the enclosing function.

When `create_salary_filter()` returns `check`, the returned function keeps access to the referenced variable from its enclosing scope. This preserved environment is called a closure.

For example:

```python
high_salary = create_salary_filter(60000)

high_salary(employees[0])  # False
high_salary(employees[2])  # True
```

The returned function remembers that `min_salary` is `60000`.

### 5. Decorator

**What does `@log_execution` approximately mean in Python?**

The syntax:

```python
@log_execution
def generate_report():
    ...
```

is approximately equivalent to:

```python
def generate_report():
    ...

generate_report = log_execution(generate_report)
```

The decorator receives the original function and returns a wrapped version with additional behavior.

In this assignment, the decorator prints a `[START]` message before the function runs and an `[END]` message after it finishes.

### 6. Context Manager

**Why is `with ReportFile("report.txt") as report:` better than manually opening and closing the file?**

A context manager handles setup and cleanup automatically.

`__enter__()` opens the file and returns the file object. After the `with` block finishes, `__exit__()` closes the file, including when an exception occurs inside the block.

This reduces the chance of forgetting to close the file and makes resource management cleaner and safer.

## Flow of the Program

```text
Employee List
     |
     v
Generator
employee_generator()
     |
     v
Department Generator
filter_by_department()
     |
     v
Closure
create_salary_filter()
     |
     v
Salary Filter
     |
     v
Context Manager
ReportFile
     |
     v
Write employee_report.txt

Decorator
@log_execution
wraps report generation and salary calculation
```
