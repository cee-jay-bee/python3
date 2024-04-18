from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for e in self.employees:
            print(e.fname, e.lname)
        print('---------------')

    def pay_employees(self):
        print('Paying Employees')
        for e in self.employees:
            print('Paycheck for:', e.fname, e.lname)
            print(f'Amount ${e.calculate_paycheck():,.2f}')
            print('----------------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('CJ', 'Barnes', 92000)
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee('Theresa', 'Ha', 40, 50)
    my_company.add_employee(employee2)

    employee3 = CommissionEmployee('Mia', 'Barnes', 150000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()