import sys
import datetime


class Employee:

    hike_amount = 1.05

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = pay
        self._email = first + '.' + last + '@someone.com'

    def fullname(self):
        return '{} {}'.format(self._first, self._last)

    def apply_hike(self):
        try:
            return int(self._pay * self.hike_amount)
        except TypeError:
            print("Pay should be in correct type {}".format(type(self._pay)), file=sys.stderr)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self._first, self._last, self._pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self._email)

    @classmethod
    def set_hike_amount(cls, amount):
        cls.hike_amount = amount

    @classmethod
    def create_employee_from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self._programming_language = programming_language


# print(help(Developer))
print(Employee.is_workday(datetime.date(2019, 7, 10)))

dev1 = Developer('Eric', 'Evans', 1000000, 'Domain Driven Design')
print(dev1.fullname())
print(dev1._programming_language)

# emp1 = Employee('Bob', 'Marley', 90000)
emp1 = Employee.create_employee_from_string('Bob-Marley-90000')
emp2 = Employee('John', 'Lenon', 90000)

# print(emp1.__dict__)
#
# emp1.hike_amount = 1.08
#
# print(emp1.__dict__)

Employee.set_hike_amount(1.07)

# emp1.hike_amount = 1.09
print(emp1.apply_hike())
print(emp1.fullname())

print(emp2.apply_hike())
# __str__ special method invoking :::
print(emp2)
# print(Employee.hike_amount)
# print(emp1.hike_amount)
# print(emp2.hike_amount)
