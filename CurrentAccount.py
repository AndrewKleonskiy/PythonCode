from bank_account import BankAccount

class CurrentAccount(BankAccount):
    """
    A class representing a current (checking) account
    """
    #""" Класс, представляющий  текущий(чековый) счет"""
    def __init__(self,customer,account_number,annual_free,transaction_limit,balance = 0):
        """
        Инициализация текущего счета
        """
        self.annual_fee = annual_free
        self.transaction_limit = transaction_limit
        super().__init__(customer,account_number,balance)

    def withdraw(self,amount):

        """
        Снятие денежной суммы, если на счете имеется достаточно средств и снимаемая сумма меньше лимита, установленного для одной транзакции
        """
        if amount <= 0:
            print('Invalid withdrawal amount:', amount)
        if amount > self.balance:
            print ("Insuffcient funds")
            return
        if amount > self.transaction_limit:
            print('{0:s}{1:.2f} exceeds the single transaction limit of'
                  '{0:s}{2:.2f}'.format(self.currency,amount,self.transaction_limit))
            return
        self.balance -= amount

    def apply_annual_fee(self):
        """
        Удержание ежегодной оплаты с баланса счета
        """
        self.balance = max(0., self.balance - self.annual_fee)


my_current = CurrentAccount('Alison Wicks',78300991, 20.,200.)
my_current.withdraw(220)

my_current.deposit(750)
my_current.check_balance()

my_current.withdraw(220)