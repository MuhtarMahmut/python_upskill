class Person:
    def __init__(self, name: str = "Unknown", age: int = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):

    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")


class Tester(Employee):

    def work(self):
        print(f"{self.name} is testing the application")


class Developer(Employee):

    def work(self):
        print(f"{self.name} is developing the application")


employee1 = Tester("Sara", 30, "Quality Assurance", 100_000)
employee2 = Developer("Said", 40, "Python Developer", 120_000)

print(employee1)
print(employee2)

employee1.work()
employee2.work()