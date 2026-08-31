# Assignment Answers: Python Exception Handling and Logging

## 1. What is exception handling?

Exception handling is a way of detecting and managing runtime errors in a program so that the program can respond safely instead of stopping unexpectedly. In this assignment, `try` and `except` are used to handle invalid input and division by zero.

## 2. Why should we use exception handling?

We use exception handling to prevent unexpected errors from crashing the application and to give the user a clear, useful message. Without it, invalid input such as `abc` passed to `int()` can terminate the program with an unhandled `ValueError`.

## 3. What is the difference between `try` and `except`?

The `try` block contains code that may raise an exception. The `except` block catches a specified exception and handles it. For example, the program puts `int(input(...))` inside `try` and catches `ValueError` when the user enters a non-numeric value.

## 4. When is the `else` block executed?

The `else` block is executed only when the associated `try` block completes successfully without raising an exception.

## 5. When is the `finally` block executed?

The `finally` block is executed whether an exception occurs or not. It is useful for actions that should always happen, such as cleanup or displaying a completion message.

## 6. What is logging?

Logging is the practice of recording application events, warnings, errors, and other useful information. It helps developers understand what happened during execution and makes troubleshooting easier, especially when the application is running in production.

## 7. What is the difference between `print()` and logging?

`print()` is mainly used to show immediate information to the user in the console. Logging is designed to record application events in a structured way and can write messages to files while supporting levels such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

## 8. What happens when the logging level is set to `ERROR`?

Messages at `ERROR` and `CRITICAL` levels are recorded. `DEBUG`, `INFO`, and `WARNING` messages are filtered out.

| Log level | Recorded with `level=logging.ERROR`? |
|---|---|
| DEBUG | No |
| INFO | No |
| WARNING | No |
| ERROR | Yes |
| CRITICAL | Yes |

When the level is changed to `DEBUG`, messages at all five levels are allowed to be recorded.

## 9. What happens if we do not handle `ValueError` when converting user input using `int()`?

If the user enters something that is not a valid integer, `int()` raises a `ValueError`. Without an appropriate exception handler, the program stops and displays a traceback instead of asking the user to enter the value again.

## 10. Why should we avoid using a broad exception handler such as `except: pass`?

It can hide real problems and make debugging difficult. It also silently ignores errors, so the program may continue in an incorrect state. The better approach is to catch specific exceptions, such as `ValueError` and `ZeroDivisionError`, and handle them deliberately.

## 11. Why is logging useful in a production application?

Logging provides a history of important application events and failures. Developers can use the logs to diagnose problems, monitor unusual behavior, and understand what happened without relying only on what a user sees on screen.

## 12. What is the purpose of the `finally` block?

The `finally` block contains code that should run regardless of whether an exception happened. In this application it prints `Processing completed.` and records completion in the log.

## Logging Level Experiment

### With `level=logging.ERROR`

Only `ERROR` and `CRITICAL` messages are written to `student_app.log`.

### With `level=logging.DEBUG`

`DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages can be written to `student_app.log`.

Changing the logging level changes the minimum severity of messages that the logger accepts. A lower threshold such as `DEBUG` permits more detailed messages, while a higher threshold such as `ERROR` records only more serious events.

## Program Features Implemented

- Student name, subject count, and marks input.
- `ValueError` handling for invalid numbers and marks.
- Marks validation from 0 to 100.
- Average calculation.
- Result classification: Excellent, Very Good, Pass, Fail.
- `ZeroDivisionError` handling when zero subjects are entered.
- `try`, `except`, `else`, and `finally` usage.
- Logging to `student_app.log`.
- All required logging levels demonstrated.
- Multiple-student processing.
- Separate `calculate_average()` and `get_result()` functions.
- Bonus statistics: highest mark, lowest mark, and average.
- Useful `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages.
