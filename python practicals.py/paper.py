class Employee:
    def __init__(self, eno=None, name=None):
        self.eno = eno
        self.name = name
        self.employees = []

    def addemp(self, eno, name):
        self.employees.append({'eno': eno, 'name': name})

    def displayemp(self):
        for employee in self.employees:
            print(f"Number: {employee['eno']}, Name: {employee['name']}")


e = Employee()  # Corrected instantiation
e.addemp(101, 'rohit')
e.addemp(201, 'rohan')
e.displayemp()
