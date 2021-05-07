class Employees:
    raise_amount = 2000
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.current_raise_amount = Employees.raise_amount

    def add_salary(self):
        self.salary = self.salary + self.current_raise_amount

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def increase_raise_amount(cls, amount):
        cls.raise_amount = cls.raise_amount + amount

class Manager(Employees):
    def __init__(self, first_name, last_name, salary, employees=None):
        super.__init__(first_name, last_name, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print(f'{self.first_name} already manages {employee.first_name}')

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f'{self.first_name} does not manage {employee.first_name}')

    def print_all_employees(self):
        for employee in self.employees:
            print(employee.get_full_name())

    def print_total_salary(self):
        total_salary = []
        for employee in self.employees:
            total_salary.append(employee.salary)
        print(sum(total_salary))
