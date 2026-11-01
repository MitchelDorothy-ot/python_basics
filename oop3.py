# bank acc == owner, acc no, balance, history 1988-08-28
from datetime import date, datetime
from time import strptime


class Client:
    def __init__(self, names, kra_pin, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    # ctrl+alt+l to align
    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year -  birth_date.year
        return age


class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount:int):
        self.balance += amount

    def withdraw(self, amount:int):
        if amount > self.balance:
            print("You don't have enough money to withdraw")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("-----------------")


Jane = Client('Jane Doe','A001', '1999-01-16', 'F')
Ahmed = Client('Ahmed Ali', 'A0005','2005-10-26','M')

acc1 = BankAccount(Jane,111111,70_000)
acc2 = BankAccount(Ahmed,394798,80_745)
acc3 = BankAccount(Ahmed,113456,70_000_678)

acc1.deposit(10_000)
acc1.deposit(3_000)

acc1.print_details()
acc1.withdraw(10_000)
acc1.print_details()

print("Jane's Age", Jane.calc_age())
print("Ahmed's Age", Ahmed.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(Jane.names, Jane.calc_age())
print(acc2.owner.calc_age())


# dob = '18-01-2005' #d.m.Y(4-digits)
#
# today = date.today()
# # print(f"{today.year}-{today.month}-{today.day}")
# # covert string to date
# birth_date = datetime.strptime(dob,"%d.%m.%Y")
#
# age = today.year - birth_date.year
# print(age)