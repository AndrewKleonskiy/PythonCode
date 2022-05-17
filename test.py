from bank_account import BankAccount
my_account = BankAccount('Joe',21457288)
my_account.account_number #Доступ к атрибуту класса my_account
my_account.deposit(64) #Вызов метода класса my_account
print(my_account.balance)


from bank_account import BankAccount
from Customer import Customer


customer1 = Customer('Helen Smith','76 The Warren, Blandings, Sussex','1976-02-29')
account1 = BankAccount(customer1,21457288,1000)
print(account1.customer.get_age())
print(account1.customer.address)