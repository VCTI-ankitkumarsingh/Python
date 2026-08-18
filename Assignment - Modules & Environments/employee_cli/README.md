# Project 2 – Employee CLI Application

This project demonstrates Python modules, a Python package, third-party libraries, virtual environment isolation, and dependency management for a command-line employee information application.

## Libraries Used

Project 2 uses the following third-party libraries:

- **Tabulate** – displays employee information in different CLI table formats.
- **Rich** – creates a styled terminal employee table.

> **Note:** Jinja2 and PrettyTable belong to Project 1 and are not used in this project.

---

## Part 1 – Project 2 Output

The application is executed using:

```bash
python app.py
```

The output contains:

1. An employee table generated using **Tabulate**.
2. The employee information displayed using the `grid` format.
3. The employee information displayed using the `simple` format.
4. A styled employee table generated using **Rich**.

### Sample Output

```text
========================================
 EMPLOYEE CLI APPLICATION
========================================

Employee List - Tabulate
------------------------
+------+--------+--------------+----------+
| id   | name   | department   |   salary |
+======+========+==============+==========+
| E001 | John   | IT           |    50000 |
+------+--------+--------------+----------+
| E002 | Alice  | HR           |    45000 |
+------+--------+--------------+----------+
| E003 | Bob    | Finance      |    55000 |
+------+--------+--------------+----------+

Employee List - Tabulate (simple)
---------------------------------
id    name    department      salary
----  ------  ------------  --------
E001  John    IT               50000
E002  Alice   HR               45000
E003  Bob     Finance          55000

Employee List - Rich
--------------------
           Employee Details           
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┓
┃ ID   ┃ Name  ┃ Department ┃ Salary ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━┩
│ E001 │ John  │ IT         │  50000 │
│ E002 │ Alice │ HR         │  45000 │
│ E003 │ Bob   │ Finance    │  55000 │
└──────┴───────┴────────────┴────────┘
```

The employee information is supplied dynamically to Tabulate and Rich, and the libraries generate the table formatting.

---

## Part 3 – Comparing the Libraries

For this project, the two required libraries have different responsibilities.

| Library | Purpose | Outcome |
|---|---|---|
| Tabulate | CLI table formatting | Employee data displayed in multiple table formats |
| Rich | Rich terminal UI | Styled employee table with title, alignment, and formatting |

### Why Tabulate?

Tabulate is useful when employee information needs to be displayed quickly in different predefined table formats. The project demonstrates the `grid` and `simple` formats.

### Why Rich?

Rich is useful when terminal output needs additional styling and a better visual presentation. The employee table includes a title, column formatting, and alignment.

### Part 3 Outcome

Tabulate is used for **multiple CLI table formats**, while Rich is used for a **styled terminal table**. Together, they satisfy the Employee CLI Application requirements.

---

## Part 4 – Virtual Environment Isolation

A separate virtual environment is used for Project 2:

```text
employee_cli/
└── .venv/
    ├── Tabulate
    └── Rich
```

The environment is created using:

```bash
python -m venv .venv
```

The Project 2 environment is activated using:

```bash
.venv\Scripts\activate
```

The installed packages can be checked using:

```bash
pip list
```

The Project 2 environment contains Tabulate and Rich, while the libraries belonging to Project 1 are not installed in this environment.

### Test 2 Screenshot

**Test 2** contains the results of the Project 2 environment verification.

It shows:

- `tabulate`
- `rich`
- `jinja2` → Package not found
- `prettytable` → Package not found

This confirms that the Project 2 environment contains its required libraries and does not contain the Project 1 libraries.

The screenshot is available in:

```text
Test 2.png
```

### Part 4 Outcome

The Employee CLI application runs inside its own `.venv`, with Tabulate and Rich installed independently of the other project's environment.

---

## Part 5 – Proving the Environments Are Separate

The isolation was verified by checking for packages that belong to the other project.

With the Project 2 environment active:

```bash
pip show jinja2
pip show prettytable
```

The result was:

```text
WARNING: Package(s) not found: jinja2
WARNING: Package(s) not found: prettytable
```

At the same time, `pip list` confirmed that the Project 2 dependencies are installed.

### Part 5 Outcome

The results demonstrate that installing libraries for Project 2 does not automatically make the other project's libraries available in the Project 2 environment.

Therefore, the environments provide dependency isolation between the two projects.

---

## Project Structure

```text
employee_cli/
│
├── .venv/
├── app.py
├── requirements.txt
│
└── employee_system/
    ├── __init__.py
    ├── employee.py
    ├── salary.py
    └── attendance.py
```

## Requirements

The project dependencies are recorded in `requirements.txt`:

```text
tabulate
rich
```

They can be installed using:

```bash
pip install -r requirements.txt
```

---

## Summary

Project 2 demonstrates the complete workflow:

```text
Python Modules
      ↓
Python Package
      ↓
Third-Party Libraries
      ↓
Project-Specific Virtual Environment
      ↓
Tabulate + Rich
      ↓
Employee CLI Application
```

The result is a command-line employee application with multiple table formats through Tabulate and a styled terminal table through Rich, while maintaining an isolated project environment.
