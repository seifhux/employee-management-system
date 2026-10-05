import json
all_employees = [] 
FILE_NAME = "employees.json"


class Employee:
    def __init__(self, id, name, age, dept, type, phone, email, bonus, deduction):
        self.id = id
        self.name = name
        self.age = age
        self.dept = dept
        self.phone = phone
        self.email = email
        self.type = type
        self.bonus = bonus
        self.deduction = deduction
        
    def display_info(self):
        print(f"""            ========================================                    
            ID: {self.id}
            Name: {self.name}
            Age: {self.age}
            Department: {self.dept}
            Type: {self.type}
            Phone: {self.phone}
            Email: {self.email}""")

    def add_bonus(self, bonus):
        self.bonus += bonus
        print(f"{bonus} EGP bonus added.")
        print(f"Total Bonus: {self.bonus} EGP")

    def add_deduction(self, deduction):
        self.deduction += deduction
        print(f"{deduction} EGP deduction added.")
        print(f"Total deduction: {self.deduction} EGP")               


class Full_Time_Employee(Employee):
    def __init__(self, id, name, age, dept, phone, email, bonus, deduction, basic_salary, present_days, absent_days, late_days, final_salary):
        super().__init__(id, name, age, dept, "Full-Time", phone, email, bonus, deduction)
        self.basic_salary = basic_salary
        self.present_days = present_days
        self.absent_days = absent_days
        self.late_days = late_days
        self.final_salary = final_salary

    def display_rate(self):
        print(f"Current Salary: {self.basic_salary}")

    def update_rate(self, new_rate):
        self.basic_salary = new_rate
        print(f"Salary Updated to {new_rate}")

    def mark_present(self):
        self.present_days += 1

    def mark_absent(self):
        self.absent_days += 1

    def record_late(self):
        self.late_days += 1

    def attendance_report(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Present Days: {self.present_days}
            Absent Days: {self.absent_days}
            Late Days: {self.late_days}""")

    def calculate_salary(self):
        absent_deduction = self.absent_days * 200
        late_days_deduction = self.late_days * 50
        self.final_salary = self.basic_salary + self.bonus - self.deduction - absent_deduction - late_days_deduction
        return self.final_salary
        
    def show_salary_details(self):
        print(f"""
            ========================================
                        SALARY BREAKDOWN
            ========================================
            Name: {self.name}
            Type: {self.type}
            ========================================
            Basic Salary: {self.basic_salary} EGP
            Bonus: {self.bonus} EGP
            Manual Deduction: {self.deduction} EGP
            Absent Days: {self.absent_days}
            Absence Deduction: {self.absent_days * 200} EGP
            Late Days: {self.late_days}
            Late Deduction: {self.late_days * 50} EGP
            Final Salary: {self.final_salary} EGP
            """)

    def payroll_details(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Final Salary: {self.final_salary}""")
                
                 
class Part_Time_Employee(Employee):
    def __init__(self, id, name, age, dept, phone, email, bonus, deduction, hourly_rate, working_hrs, present_days, absent_days, late_days, final_salary):
        super().__init__(id, name, age, dept, "Part-Time", phone, email, bonus, deduction)
        self.hourly_rate = hourly_rate
        self.working_hrs = working_hrs
        self.present_days = present_days
        self.absent_days = absent_days
        self.late_days = late_days
        self.final_salary = final_salary
  
    def display_rate(self):
        print(f"Current Hourly rate: {self.hourly_rate}")

    def update_rate(self, new_rate):
        self.hourly_rate = new_rate  
        print(f"Hourly Rate Updated to {new_rate}")

    def mark_present(self):
        self.present_days += 1
    
    def mark_absent(self):
        self.absent_days += 1
    
    def record_late(self):
        self.late_days += 1    

    def add_working_hours(self, hours):
        self.working_hrs += hours
        print(f"{hours} hours added.")
        print(f"Total working hours: {self.working_hrs}")

    def attendance_report(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Working Hours: {self.working_hrs}
            Present Days: {self.present_days}
            Absent Days: {self.absent_days}
            Late Days: {self.late_days}""")

    def calculate_salary(self):
        absent_deduction = self.absent_days * 200
        late_days_deduction = self.late_days * 50
        basic_salary = self.hourly_rate * self.working_hrs
        self.final_salary =  basic_salary + self.bonus - self.deduction - absent_deduction - late_days_deduction
        return self.final_salary

    def show_salary_details(self):
        print(f"""
            ========================================
                        SALARY BREAKDOWN
            ========================================
            Name: {self.name}
            Type: {self.type}
            ========================================
            Basic Salary: {self.basic_salary} EGP
            Bonus: {self.bonus} EGP
            Manual Deduction: {self.deduction} EGP
            Absent Days: {self.absent_days}
            Absence Deduction: {self.absent_days * 200} EGP
            Late Days: {self.late_days}
            Late Deduction: {self.late_days * 50} EGP
            Final Salary: {self.final_salary} EGP
            """)           

    def payroll_details(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Final Salary: {self.final_salary}""")

class FreeLancer(Employee):
    def __init__(self, id, name, age, dept, phone, email, bonus, deduction, project_rate, projects_completed, final_salary):
        super().__init__(id, name, age, dept, "Freelancer", phone, email, bonus, deduction)
        self.project_rate = project_rate
        self.projects_completed = projects_completed
        self.final_salary = final_salary  

    def display_rate(self):
        print(f"Current Project Rate: {self.project_rate}")    

    def update_rate(self, new_rate):
        self.project_rate = new_rate
        print(f"Project Rate Updated to {new_rate}")

    def add_projects(self, projects):
        self.projects_completed += projects
        print(f"{projects} Projects Added.")
        print(f"Total Projects Completed: {self.projects_completed}")

    def attendance_report(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Projects Completed: {self.projects_completed}""") 

    def calculate_salary(self):
        basic_salary = self.projects_completed * self.project_rate
        self.final_salary =  basic_salary + self.bonus - self.deduction 
        return self.final_salary

    def show_salary_details(self):
        print(f"""
            ========================================
                        SALARY BREAKDOWN
            ========================================
            Name: {self.name}
            Type: {self.type}
            ========================================
            Basic Salary: {self.basic_salary} EGP
            Bonus: {self.bonus} EGP
            Manual Deduction: {self.deduction} EGP
            Absent Days: {self.absent_days}
            Absence Deduction: {self.absent_days * 200} EGP
            Late Days: {self.late_days}
            Late Deduction: {self.late_days * 50} EGP
            Final Salary: {self.final_salary} EGP
            """)             
              
    def payroll_details(self):
        print(f"""            ID: {self.id}
            Name: {self.name}
            Type: {self.type}
            Final Salary: {self.final_salary}""")



def add_employee():
    type = int(input("""
        Enter employee type 
        1. Full-Time
        2. Part-Time 
        3. Freelancer
        """))

    while True:
        try:
            id = int(input("Enter Employee ID: "))

            if id <= 0:
                print("Error: Employee ID must be greater than zero.")
                continue

            if search_by_id(id) is not None:
                print("Error: Employee ID already exists.")
                continue

            break

        except ValueError:
            print("Error: Employee ID must be a number.")

    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    dept = input("Enter employee department: ")
    phone = input("Enter employee phone number: ")
    email = input("Enter employee email: ")

    if type == 1:
        basic_salary = float(input("Enter employee basic salary: "))

        employee = Full_Time_Employee(id, name, age, dept, phone, email, 0, 0, basic_salary, 0, 0, 0, basic_salary)

    elif type == 2:
        hourly_rate = float(input("Enter employee hourly rate: "))
        working_hrs = int(input("Enter employee working hours: "))

        employee = Part_Time_Employee(id, name, age, dept, phone, email, 0, 0, hourly_rate, working_hrs, 0, 0, 0, 0.0)

    elif type == 3:
        project_rate = float(input("Enter employee project rate: "))
        projects_completed = int(input("Enter employee completed projects: "))

        employee = FreeLancer(id, name, age, dept, phone, email, 0, 0, project_rate, projects_completed, 0.0)

    else:
        print("Invalid employee type. Please try again.")
        return    

    all_employees.append(employee)                
    print("Employee added.")
    save_data()


def display_employees():    
    print(f"""
            ========================================
                       Total Employees: {len(all_employees)}""")    

    for employee in all_employees:
        employee.display_info()


def search_by_id(id):
    for employee in all_employees:
        if employee.id == id:
            return employee
    return None


def search_by_name(name):
    employees_to_display = []

    for employee in all_employees:
        if employee.name == name:
            employees_to_display.append(employee)

    if not employees_to_display:
        print(f"No employees named {name} found.")
             
    else:
        for employee in employees_to_display:
            employee.display_info()


def search_by_department(dept):
    employees_to_display = []

    for employee in all_employees:
        if employee.dept == dept:
            employees_to_display.append(employee)
    
    if not employees_to_display:
        print(f"No employees found in {dept}.")
                 
    else:
        for employee in employees_to_display:
            employee.display_info()


def search_by_type(type):
    if type == 1:
        type = "Full-Time"
    elif type == 2:
        type = "Part-Time"
    elif type == 3:
        type = "Freelancer"   

    employees_to_display = []         
    for employee in all_employees:
        if employee.type == type:
            employees_to_display.append(employee)
        
    if not employees_to_display:
        print(f"No {type} employees found.")
                     
    else:
        for employee in employees_to_display:
            employee.display_info()


def update_employee():
    id = int(input("Enter employee ID: "))
    emp = search_by_id(id)
    
    if emp is None:
        print("Employee not found.")
        return
            
    print("""
        Select field to update:
        1. Name
        2. Age
        3. Department
        4. Phone
        5. Email
        6. Salary / Rate
        0. Cancel
        """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Current name: {emp.name}")
        new_name = input("Enter new name: ")
        emp.name = new_name
        print(f"Name updated to {new_name}.")
        
    elif choice == 2:
        print(f"Current age: {emp.age}")
        new_age = int(input("Enter new age: "))
        emp.age = new_age
        print(f"Age updated to {new_age}")
                   
    elif choice == 3:
        print(f"Current department: {emp.dept}")
        new_dept = input("Enter new department: ")
        emp.dept = new_dept
        print(f"Department updated to {new_dept}.")
                
    elif choice == 4:
        print(f"Current phone: {emp.phone}")
        new_phone = input("Enter new phone: ")
        emp.phone = new_phone
        print(f"Phone updated to {new_phone}")
            
    elif choice == 5:
        print(f"Current email: {emp.email}")
        new_email = input("Enter new email: ")
        emp.email = new_email
        print(f"Email updated to {new_email}")
                
    elif choice == 6:
        emp.display_rate()
        new_rate = float(input("Enter new rate: "))
        emp.update_rate(new_rate)
                 
    elif choice == 0:
        return

    save_data()                                                      


def delete_employee():
    id = int(input("Enter employee ID: "))
    employee = search_by_id(id)

    if employee is None:
        print("ID not found.")  
        return      

    choice = input(f"Are you sure you want to delete employee #{id}? (y/n)\n").lower()
    if choice == "y":
        all_employees.remove(employee)
        print(f"Employee #{id} deleted.")
        save_data()

    elif choice == "n":
        print(f"Employee #{id} preserved.")

    else:
        print("Invalid choice.")

            
def add_bonus():
    id = int(input("Enter employee ID: "))
    emp = search_by_id(id)
        
    if emp is None:
        print("Employee not found.")
        return

    bonus = float(input("Enter bonus value: "))
    emp.add_bonus(bonus)
    save_data()


def add_deduction():
    id = int(input("Enter employee ID: "))
    emp = search_by_id(id)
        
    if emp is None:
        print("Employee not found.")
        return

    deduction = float(input("Enter deduction value: "))
    emp.add_deduction(deduction)
    save_data()


def display_salary():
    id = int(input("Enter employee ID: "))
    emp = search_by_id(id)
        
    if emp is None:
        print("Employee not found.")
        return

    salary = emp.calculate_salary()
    print(f"Final Salary: {salary}")
    save_data()


def salary_details():
    id = int(input("Enter employee ID: "))
    emp = search_by_id(id)
            
    if emp is None:
        print("Employee not found.")
        return
    
    emp.show_salary_details()


def payroll_report():
    if not all_employees:
        print("No employees found.")
        return

    total_payroll = 0.0
    highest_paid = None
    lowest_paid = None

    print(""" 
        ========================================
                    PAYROLL REPORT
        ========================================""")
    
    for employee in all_employees:    
        employee.calculate_salary()
        employee.payroll_details()
        print("        ========================================")
        total_payroll += employee.final_salary
        
        if highest_paid is None or employee.final_salary >= highest_paid.final_salary:
            highest_paid = employee
        
        if lowest_paid is None or employee.final_salary <= lowest_paid.final_salary:
            lowest_paid = employee
        
    average_salary = total_payroll / len(all_employees)
    print(f"        Total Payroll: {total_payroll} EGP")
    print(f"        Average Salary: {average_salary:.2f} EGP")
    print("        ========================================")
    print(f"        Highest Paid Employee: {highest_paid.name} - {highest_paid.final_salary} EGP")
    print(f"        Lowest Paid Employee: {lowest_paid.name} - {lowest_paid.final_salary} EGP\n")        


def stats_report():
    total_employees = len(all_employees)
    total_full_time = sum(1 for employee in all_employees if employee.type == "Full-Time")
    total_part_time = sum(1 for employee in all_employees if employee.type == "Part-Time")
    total_freelancers = sum(1 for employee in all_employees if employee.type == "Freelancer")

    print(f""" 
        ========================================
                   EMPLOYEE STATISTICS
        ========================================
        Total Employees: {total_employees}
        Full-Time Employees: {total_full_time}
        Part-Time Employees: {total_part_time}
        Freelancers: {total_freelancers}
        ========================================""")

    all_depts = {}
    for employee in all_employees:
        specific_dept = employee.dept
        all_depts[specific_dept] = all_depts.get(specific_dept, 0) + 1

    print(f"""                      DEPARTMENTS
        ========================================""")
    for dept, count in all_depts.items():
        print(f"        {dept}: {count}")


# ---- FILE HANDLING FUNCTIONS ----
def employee_to_dict(employee):
    data = employee.__dict__.copy()
    data["class_type"] = employee.__class__.__name__
    return data

def save_data():
    data = []

    for employee in all_employees:
        data.append(employee_to_dict(employee))

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Employee data saved successfully.")

def load_data():
    global all_employees

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        all_employees = []
        for employee_data in data:
            if employee_data["class_type"] == "Full_Time_Employee":
                employee = Full_Time_Employee(
                    employee_data["id"],
                    employee_data["name"],
                    employee_data["age"],
                    employee_data["dept"],
                    employee_data["phone"],
                    employee_data["email"],
                    employee_data["bonus"],
                    employee_data["deduction"],
                    employee_data["basic_salary"],
                    employee_data["present_days"],
                    employee_data["absent_days"],
                    employee_data["late_days"],
                    employee_data["final_salary"]
                )

            elif employee_data["class_type"] == "Part_Time_Employee":
                employee = Part_Time_Employee(
                    employee_data["id"],
                    employee_data["name"],
                    employee_data["age"],
                    employee_data["dept"],
                    employee_data["phone"],
                    employee_data["email"],
                    employee_data["bonus"],
                    employee_data["deduction"],
                    employee_data["hourly_rate"],
                    employee_data["working_hrs"],
                    employee_data["present_days"],
                    employee_data["absent_days"],
                    employee_data["late_days"],
                    employee_data["final_salary"]
                )

            elif employee_data["class_type"] == "FreeLancer":
                employee = FreeLancer(
                    employee_data["id"],
                    employee_data["name"],
                    employee_data["age"],
                    employee_data["dept"],
                    employee_data["phone"],
                    employee_data["email"],
                    employee_data["bonus"],
                    employee_data["deduction"],
                    employee_data["project_rate"],
                    employee_data["projects_completed"],
                    employee_data["final_salary"]
                )

            else:
                continue

            all_employees.append(employee)
        print("Employee data loaded successfully.")

    except FileNotFoundError:
        all_employees = []
        print("No saved employee data found. Starting with empty list.")

    except json.JSONDecodeError:
        all_employees = []
        print("Employee data file is empty or corrupted. Starting with empty list.")   

         
# ---- MENUS ---- 
def main_menu():
    while True:
        print("""
        ========================================
               EMPLOYEE MANAGEMENT SYSTEM
        ========================================
        1. Add Employee
        2. Display All Employees
        3. Search Employee
        4. Update Employee
        5. Delete Employee
        6. Attendance Management
        7. Add Bonus
        8. Add Deduction
        9. Calculate Employee Salary
        10. Salary Details
        11. Payroll Report
        12. Employee Statistics
        13. Save Data
        0. Exit
        ========================================""")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_employee()

        elif choice == 2:
            display_employees()

        elif choice == 3:
            search_menu()

        elif choice == 4:
            update_employee()

        elif choice == 5:
            delete_employee()

        elif choice == 6:   
            attendance_management_menu()

        elif choice == 7:
            add_bonus()

        elif choice == 8:
            add_deduction()    

        elif choice == 9:
            display_salary()

        elif choice == 10:
            salary_details()

        elif choice == 11:
            payroll_report()

        elif choice == 12:
            stats_report()

        elif choice == 13:
            save_data()

        elif choice == 0:
            break     

        else:
            print("Invalid choice. Please try again.")


def search_menu():
    while True:
        print("""
        ========================================
                      SEARCH MENU
        ========================================
        1. Search by ID
        2. Search by Name
        3. Search by Department
        4. Search by Employee Type
        0. Back
        ========================================""")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            id = int(input("Enter employee ID to search: "))
            employee = search_by_id(id)

            if employee:
                employee.display_info()
            else:
                print("Employee not found.")

        elif choice == 2:
            name = input("Enter employee name to search: ")
            search_by_name(name)

        elif choice == 3:
            dept = input("Enter department to search for: ")
            search_by_department(dept)

        elif choice == 4:
            type = int(input("Enter employee type to search: \n1. Full-Time\n2. Part-Time\n3. Freelancer\n"))
            search_by_type(type)

        elif choice == 0:
            break

        else:
            print("Invalid choice. Please try again.")


def attendance_management_menu():
    while True:
        print("""
        ========================================
               ATTENDANCE MANAGEMENT MENU
        ========================================        
        1. Mark Present
        2. Mark Absent
        3. Record Late Day
        4. Add Working Hours
        5. Add Completed Project
        6. Display Attendance Report
        0. Back  
        ========================================""")
        choice = int(input("Enter your choice: "))

        # Mark Present
        if choice == 1:
            id = int(input("Enter employee ID: "))
            employee = search_by_id(id)

            if employee is None:
                print("Employee not found.")

            elif not isinstance(employee, (Full_Time_Employee, Part_Time_Employee)):
                print("ID must be a full-time or part-time employee.")
                
            else:
                employee.mark_present()
                print("Presence recorded.")
                print(f"Total Present Days: {employee.present_days}")
                save_data()

        # Mark Absent
        elif choice == 2:
            id = int(input("Enter employee ID: "))
            employee = search_by_id(id)

            if employee is None:
                print("Employee not found.")

            elif not isinstance(employee, (Full_Time_Employee, Part_Time_Employee)):
                print("ID must be a full-time or part-time employee.")

            else:
                employee.mark_absent()
                print("Absence recorded.")
                print(f"Total Absent Days: {employee.absent_days}")
                save_data()

        # Record Late Arrival
        elif choice == 3:
            id = int(input("Enter employee ID: "))
            employee = search_by_id(id)

            if employee is None:
                print("Employee not found.")

            elif not isinstance(employee, (Full_Time_Employee, Part_Time_Employee)):
                print("ID must be a full-time or part-time employee.")

            else:
                employee.record_late()
                print("Late arrival recorded.")
                print(f"Total Late Days: {employee.late_days}")
                save_data()

        # Add Working Hours
        elif choice == 4:
            id = int(input("Enter employee ID: "))
            employee = search_by_id(id)

            if employee is None:
                print("Employee not found.")

            elif not isinstance(employee, Part_Time_Employee):
                print("ID must be a part-time employee.") 

            else:
                print(f"Current working hours: {employee.working_hrs}") 
                hours = int(input("How many hours do you want to add? "))
                employee.add_working_hours(hours)
                save_data()          

        # Add Completed Project
        elif choice == 5:
            id = int(input("Enter employee ID: "))
            employee = search_by_id(id)
            
            if employee is None:
                print("Employee not found.")
            
            elif not isinstance(employee, FreeLancer):
                print("ID must be a freelancer.") 
            
            else:
                print(f"Current Completed Projects: {employee.projects_completed}") 
                projects = int(input("How many projects do you want to add? "))
                employee.add_projects(projects)
                save_data()

        # Display Attendance Report    
        elif choice == 6:
            print("""
            ========================================
                        ATTENDANCE REPORT""")
            for employee in all_employees:
                print("            ========================================")
                employee.attendance_report()

        elif choice == 0:
            break
        
        else:
            print("Invalid choice. Please try again.")


# Main Program
load_data()
main_menu()
print("System closing...")