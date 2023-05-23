import json
class Account:
    def __init__(self, balance,user,password):
        self.balance = balance
        self.username = user
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getBalance(self):
        return self.balance

    def deposit(self, amt, acc):
        self.balance += int(amt)
        print('You have successfully deposited $', amt, 'in your bank account')
        cash = self.balance
        acc[self.username].balance = cash


    def withdraw(self, amt, acc):
        if self.balance > int(amt):
            self.balance -= int(amt)
            cash = self.balance
            acc[self.username].balance = cash
            print('You have successfully widthdrawed $', amt, 'in your bank account')
        else:
            print('ERROR not enough money in acc')
