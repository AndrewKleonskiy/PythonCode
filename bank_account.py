#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BankAccount:
    """An abstract base class representing a bank account"""
    """Абстрактный базовый класс, представляющий банковский счет"""
    currency = '$'
    
    def __init__(self,customer,account_number,balance = 0):
    #"""Initialize the BankAccount class with a cuustomer, account number and opening balance (which defaults to 0.) """
    #"""Иницилизация класса BankAccount значениями имени клиента, номера счета и баланса при открытии счета (по умолчанию 0)"""
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        if amount >0:
            self.balance  += amount
        else:
            print('Invalid deposit amount:',amount)
    def withdraw(self,amount):
        
        if amount > 0:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount',amount)    
    def check_balance(self):
        print('The balance of account number {:d} is {:s}{:.2f}'.format(self.account_number,self.currency, self.balance))





