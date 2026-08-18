# Python Training - Modules, Packages, Libraries & Virtual Environments

This folder contains two independent Python projects built using the same employee-related modules and package structure:

- **Project 1 - HR Report Generator**
  - Jinja2
  - PrettyTable
- **Project 2 - Employee CLI Application**
  - Tabulate
  - Rich

Each project has its own virtual environment so that its dependencies remain isolated.


# Documentation

## 1. What is a Module?

A **module** is a Python file containing Python code that can be imported and reused in another Python program.

In this project:

```text
employee.py
salary.py
attendance.py
```

are modules.

For example:

```python
from employee_system.employee import get_all_employees
```

Here, `employee.py` is the module that provides `get_all_employees()`.

---

## 2. What is a Package?

A **package** is a directory used to organize related Python modules together.

In this project:

```text
employee_system/
├── __init__.py
├── employee.py
├── salary.py
└── attendance.py
```

`employee_system` is the package, while `employee.py`, `salary.py`, and `attendance.py` are the modules inside it.

The modules can be imported using:

```python
from employee_system.employee import get_all_employees
from employee_system.salary import calculate_salary
```

Therefore:

```text
employee.py          → Module
employee_system/     → Package
```

---

## 3. What is a Virtual Environment?

A **virtual environment** is an isolated Python environment created for a particular project.

It allows a project to have its own installed packages and dependencies without affecting other projects on the same machine.

A virtual environment is created using:

```bash
python -m venv .venv
```

It can then be activated using:

```bash
.venv\Scripts\activate
```

---

## 4. Why Are Two Virtual Environments Used?

Two virtual environments are used because the assignment contains **two independent projects** with different third-party libraries.

### Project 1

```text
hr_report_generator/.venv/
├── Jinja2
└── PrettyTable
```

### Project 2

```text
employee_cli/.venv/
├── Tabulate
└── Rich
```

The separate environments provide dependency isolation.

For example, installing Rich in the Project 2 environment does not automatically make Rich available in the Project 1 environment.

Likewise, installing Jinja2 and PrettyTable in Project 1 does not automatically make them available in Project 2.

This makes each project independent and prevents dependency conflicts.

---

## 5. What is Jinja2 Used For?

**Jinja2** is used for **template-based text/report generation**.

In the HR Report Generator, the employee report is stored as a template:

```text
templates/employee_report.txt
```

The template contains placeholders such as:

```text
Employee ID : {{ employee.id }}
Name : {{ employee.name }}
Department : {{ employee.department }}
Salary : {{ employee.salary }}
```

The Python application supplies the employee data, and Jinja2 generates the final report dynamically.

Therefore:

```text
Jinja2 → Dynamic employee report generation
```

---

## 6. What is PrettyTable Used For?

**PrettyTable** is used to create a **formatted ASCII table**.

In the HR Report Generator, employee records are added dynamically to a PrettyTable object.

The library generates the table borders, columns, and alignment automatically.

Therefore:

```text
PrettyTable → Formatted employee table
```

It is suitable when a clean ASCII box-style table is required.

---

## 7. What is Tabulate Used For?

**Tabulate** is used to display data in **different predefined CLI table formats**.

The Employee CLI Application demonstrates formats such as:

```python
tablefmt="grid"
```

and:

```python
tablefmt="simple"
```

This allows the same employee data to be displayed in different layouts.

Therefore:

```text
Tabulate → Multiple CLI table formats
```

---

## 8. What is Rich Used For?

**Rich** is used to create a **styled terminal interface and formatted terminal output**.

In the Employee CLI Application, Rich is used to create an employee table with features such as:

- Table title
- Column formatting
- Alignment
- Terminal styling

Therefore:

```text
Rich → Styled terminal employee table
```

---

## 9. What is `requirements.txt`?

`requirements.txt` is a file used to record the Python packages required by a project.

For example, Project 1 records its dependencies in:

```text
hr_report_generator/requirements.txt
```

and Project 2 records its dependencies in:

```text
employee_cli/requirements.txt
```

Dependencies can be installed from the file using:

```bash
pip install -r requirements.txt
```

This makes it easier to recreate the required project environment.

The assignment uses:

```bash
pip freeze > requirements.txt
```

to record the installed dependencies.

---

## 10. Why Should Package Versions Be Specified?

Package versions should be specified so that the project can use **consistent and reproducible dependencies**.

For example:

```text
prettytable==3.16.0
```

specifies the exact PrettyTable version required by the project.

Without a version specification, a different version might be installed later, which could potentially change behavior or cause compatibility problems.

Specifying versions helps ensure that:

```text
Development Environment
        ↓
Testing Environment
        ↓
Recreated Environment
```

use compatible dependency versions.

This is especially important when a project has been tested with a specific package version.


# Why Use Separate Virtual Environments Instead of Installing All Four Libraries Globally?

Even though both projects are on the same machine, separate virtual environments are used because each project has its own dependencies.

Project 1 .venv
├── Jinja2
└── PrettyTable


Project 2 .venv
├── Tabulate
└── Rich

Using separate virtual environments provides:

**Dependency isolation**: Packages installed for one project do not automatically become available in the other project.
**Version control**: Each project can use the package versions it requires.
**Avoids dependency conflicts**: Changes or upgrades in one project do not affect the other project.
**Reproducibility**: Each project can recreate its required environment using its own requirements.txt.
**Cleaner global Python environment**: Project-specific libraries do not need to be installed globally.

For example, if Project 1 requires a specific version of PrettyTable, changing the dependencies of Project 2 will not affect Project 1.

Instead of installing everything globally:

Global Python
├── Jinja2
├── PrettyTable
├── Tabulate
└── Rich

The projects maintain separate environments:

Project 1 .venv
├── Jinja2
└── PrettyTable


Project 2 .venv
├── Tabulate
└── Rich

Therefore, separate virtual environments make the two projects independent, reproducible, and protected from dependency conflicts, even when both projects are running on the same machine.


# Overall Learning Outcome

The project demonstrates the relationship between Python applications, modules, packages, third-party libraries, virtual environments, and dependency management.

```text
Python Application
        ↓
      Modules
        ↓
      Package
        ↓
Third-Party Libraries
        ↓
Project-Specific Virtual Environment
        ↓
requirements.txt
```

The two projects use the same employee-related modules and package structure while maintaining separate external dependencies.

This demonstrates why project-specific virtual environments are preferable to installing all libraries globally on the machine.
