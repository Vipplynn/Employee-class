class Employee:
    def __init__(self, name, ID, department, title):
        self.name = name
        self.ID = ID
        self.department = department
        self.title = title
    def set_name(self,name):
        self.name = name
    def set_ID(self, ID):
        self.ID = ID
    def set_department(self,department):
        self.department = department
    def set_title(self,title):
        self.title = title

    def get_name(self):
        return self.name
    def get_ID(self):
        return self.ID
    def get_department(self):
        return self.department
    def get_title(self):
        return self.title

def main():
    emp1 = Employee('name', 'id', 'department', 'title')
    emp2 = Employee('name', 'id', 'department', 'title')
    emp3 = Employee('name', 'id', 'department', 'title')

    emp1.set_name('Susan Meyers')
    emp1.set_ID('47899')
    emp1.set_department('Accounting')
    emp1.set_title('Vice President')

    emp2.set_name('Mark Jones')
    emp2.set_ID('39119')
    emp2.set_department('IT')
    emp2.set_title('Programmer')

    emp3.set_name('Joy Rogers')
    emp3.set_ID('81774')
    emp3.set_department('Manufacturing')
    emp3.set_title('Engineer')


    print(f"{emp1.get_name()} | {emp1.get_ID()} | {emp1.get_department()} | {emp1.get_title()}")
    print(f"{emp2.get_name()} | {emp2.get_ID()} | {emp2.get_department()} | {emp2.get_title()}")
    print(f"{emp3.get_name()} | {emp3.get_ID()} | {emp3.get_department()} | {emp3.get_title()}")


main()