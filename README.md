# Employee Management & Payroll System

A command-line application written in **Python** for managing employees, tracking attendance, and calculating salaries. Built with **object-oriented programming** (inheritance and polymorphism), with all data saved to a JSON file so nothing is lost between runs.

## Features

- **Employee management (CRUD):** add, view, update, and delete employee records
- **Three employee types**, each with its own salary logic:
  - **Full-Time:** basic salary
  - **Part-Time:** hourly rate
  - **Freelancer:** project rate
- **Attendance tracking:** mark employees as present, absent, or late
- **Bonuses & deductions:** add extra pay or subtract from it per employee
- **Automatic salary calculation:** includes penalties for absences and late arrivals
- **Reports:** payroll summary and overall statistics
- **Data persistence:** everything is stored in `employees.json`

## OOP Design

```
Employee (base class)
├── Full_Time_Employee   → salary = basic salary (+ bonuses − deductions/penalties)
├── Part_Time_Employee   → salary = hours worked × hourly rate (+ bonuses − deductions/penalties)
└── FreeLancer           → salary = project rate (+ bonuses − deductions/penalties)
```

The base `Employee` class holds the shared data and behavior. Each subclass overrides the salary calculation, so the rest of the program can call the same method on any employee and get the right result (polymorphism).

## Project Structure

```
.
├── main.py          # Program entry point, classes, and menu logic
├── employees.json   # Saved employee data
└── README.md
```

## Getting Started

### Requirements
- Python 3.x (no external libraries needed)

### Run it

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python main.py
```

Follow the on-screen menu to manage employees, record attendance, and generate payroll reports.

## What I Practiced

- Designing class hierarchies with inheritance and polymorphism
- Reading and writing structured data with JSON
- Building a menu-driven CLI application
- Handling business rules like penalties, bonuses, and deductions

## Future Improvements

- Add a database (e.g., SQL Server) in place of JSON
- Export payroll reports to Excel or PDF
- Add a GUI or web interface
- Add input validation and unit tests

## Author

**Seif Aboelazaim**
Computer Science & AI student, Cairo University (FCAI)
[LinkedIn](https://linkedin.com/in/seifaboelazaim) · seifhuss74@gmail.com
