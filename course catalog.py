# course_catalog.py

# Base class
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"{self.course_code} - {self.course_name} ({self.credit_hours} Credit Hours)"


# Subclass for Core Courses
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        status = "Required" if self.required_for_major else "Not Required"
        return super().display_info() + f" | Major Requirement: {status}"


# Subclass for Elective Courses
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        return super().display_info() + f" | Elective Type: {self.elective_type}"


# Example usage
if __name__ == "__main__":
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
    elective_course = ElectiveCourse("HIST201", "World History", 2, "Liberal Arts")

    print(core_course.display_info())
    print(elective_course.display_info())

# employee.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

# main.py

from employee import Employee  # Importing Employee class from employee module

# Creating an Employee object
emp = Employee("John Doe", 50000)

# Display employee details
print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: {emp.get_salary()}")

