from account import Account

import json


class Bank:
    def __init__(self):
        self.accounts = {}
        with open("data.json") as json_file:
            data = json.load(json_file)
            for key in data:
                self.accounts[key] = Account(data[key]["balance"],data[key]["username"],data[key]["password"])

    def update_DB(self):
        data = self.accounts
        dataJSON= {}
        for key in data:
            dataJSON[key] = {"username": data[key].getUsername(), "password": data[key].getPassword(),"balance": data[key].getBalance()}
        with open("data.json", "w") as json_file:
            json.dump(dataJSON, json_file)


    def addAcc(self, accObj):
        if accObj.getUsername() not in self.accounts:
            self.accounts[accObj.getUsername()] = accObj
            self.update_DB()
        else:
            print('ERROR dulicate acoounts')

    def loggedIn(self, accObj):
        while True:
            print('your current balance is:', accObj.getBalance())
            a = input('Would you like to deposit(1), withdraw(2), or logout(3)? ')
            if a == "1":
                amt = input('how much do you want to deposit? ')
                accObj.deposit(amt, self.accounts)
                self.update_DB()
            elif a == "2":
                amt = input('how much do you want to withdraw? ')
                accObj.withdraw(amt, self.accounts)
                self.update_DB()
            elif a == "3":
                self.run()

    def run(self):
        while True:
            print('welcome to the bank')
            a = input('would you like to login(press 1) or sign up(press 2)? ')
            if a == "1":
                user = input('What is your username? ')
                password = input('What is your password? ')

                if user in self.accounts:
                    if self.accounts[user].getPassword() == password:
                        self.loggedIn(self.accounts[user])
                else:
                    print('ERROR incorrect username')
            elif a == "2":
                user = input('what would you like your username to be? ')
                password = input('what would you like your password to be? ')
                accObj = Account(0, user, password)
                self.addAcc(accObj)
                pass
            else:
                print('Error')
                pass