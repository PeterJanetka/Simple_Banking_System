"""
this needs rework,
i did manage to delete all my progress in step 4
so didnt want to waste time with this project anymore, and move forward
comments are missing, functions nonexistent, work with objects will remove some db transactions.
"""
from random import randrange, seed
import sqlite3
seed()
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER,number TEXT,pin TEXT,balance INTEGER DEFAULT 0);')
conn.commit()
IIN = 400000
account_logged_in = 0


class Account:
    def __init__(self):
        self.number = str(randrange(0, 999999999)).zfill(9)
        self.card = str(IIN) + str(self.number) + str(str(str(str(IIN) + str(self.number)) + str(10 - (sum(number - 9 if number > 9 else number
              for number in (int(number) * 2
              for number in (int(number)
              for number in (str(IIN) + str(self.number))[0::2]))) + sum(int(number)
              for number in (str(IIN) + str(self.number))[1::2])) % 10)[-1])[-1])
        self.pin = str(randrange(0, 9999)).zfill(4)
        self.balance = 0
        cur.execute("INSERT INTO card (id, number, pin, balance) VALUES(?, ?, ?, ?)", (self.number, self.card, self.pin, self.balance))
        conn.commit()


def check_card_valid(card):
    if str(card) == card[0: -1] + str(checksum(card[0: -1])):
        return True
    else:
        return False


def checksum(card):
    return (10 - (sum(number - 9 if number > 9 else number for number in (int(number) * 2 for number in (int(number) for number in str(card)[0::2]))) + sum(int(number) for number in str(card)[1::2])) % 10)


while True:
    while account_logged_in == 0:
        main_menu_input = input('1. Create an account\n'
                                '2. Log into account\n'
                                '0. Exit\n', )
        print('')
        if main_menu_input == "1":
            new = Account()
            print('Your card has been created\n'
                  'Your card number:\n'
                  f'{new.card}\n'
                  'Your card PIN:\n'
                  f'{new.pin}\n')

        if main_menu_input == "2":
            user_card = input('Enter your card number:\n', )
            user_pin = input('Enter your PIN:\n', )
            print('')
            cur.execute("SELECT * FROM card WHERE number = ? AND pin = ?", (user_card, user_pin))
            db_fetch = cur.fetchone()
            try:
                if int(db_fetch[1]) == int(user_card) and int(db_fetch[2]) == int(user_pin):
                    account_logged_in = db_fetch[0]
                    print('You have successfully logged in!\n')

            except TypeError:
                print('Wrong card number or PIN!\n')
        if main_menu_input == "0":
            print("Bye!")
            exit()

    while account_logged_in != 0:

        logged_in_input = input('1. Balance\n'
                                '2. Add income\n'
                                '3. Do transfer\n'
                                '4. Close account\n'
                                '5. Log out\n'
                                '0. Exit\n', )
        print('')
        if logged_in_input == "1":
            cur.execute("SELECT * FROM card WHERE id = ? ;", (account_logged_in,))
            db_fetch_logged_in_account = cur.fetchone()
            print("Balance: ", db_fetch_logged_in_account[3])
            print('')
        if logged_in_input == "2":
            cur.execute("SELECT * FROM card WHERE id = ? ;", (account_logged_in,))
            balance = cur.fetchone()
            add = int(balance[3]) + int(input('Enter income:\n', ))
            cur.execute("UPDATE card SET balance = ? WHERE id  = ? ;",
                        (add, account_logged_in,))
            conn.commit()
            print("Income was added!\n")
        if logged_in_input == "3":
            transfer_number = input('Transfer\nEnter card number:\n', )
            cur.execute("SELECT * FROM card WHERE number = ? ;", (transfer_number,))
            db_fetch_recipient = cur.fetchone()
            cur.execute("SELECT * FROM card WHERE id = ? ;", (account_logged_in,))
            db_fetch_logged_in_account = cur.fetchone()
            try:
                if transfer_number != db_fetch_logged_in_account[1]:
                    if not check_card_valid(transfer_number):
                        print('Probably you made a mistake in the card number.\n'
                              ' Please try again!\n'
                              '')
                    if transfer_number == db_fetch_recipient[1]:
                        transfer_amount = input('Enter how much money you want to transfer:\n', )
                        if int(transfer_amount) > int(db_fetch_logged_in_account[3]):
                            print('Not enough money!\n')
                        if int(transfer_amount) <= int(db_fetch_logged_in_account[3]):
                            cur.execute("SELECT * FROM card WHERE id = ? ;", (account_logged_in,))
                            db_fetch_logged_in_account = cur.fetchone()

                            balance_logged_in = (int(db_fetch_logged_in_account[3]) - int(transfer_amount))
                            cur.execute("UPDATE card SET balance = ? WHERE id  = ? ;",
                                        (balance_logged_in, account_logged_in))
                            conn.commit()
                            cur.execute("SELECT * FROM card WHERE number = ? ;", (transfer_number,))
                            db_fetch_recipient = cur.fetchone()
                            balance_recipient = (int(db_fetch_recipient[3]) + int(transfer_amount))
                            cur.execute("UPDATE card SET balance = ? WHERE number  = ? ;",
                                        (balance_recipient, transfer_number))
                            conn.commit()
                            print('Success!\n')
                else:
                    print("You can't transfer money to the same account!\n")
            except TypeError:
                print('Such a card does not exist.\n')

        if logged_in_input == "4":
            cur.execute("DELETE FROM card WHERE id = ?;", (account_logged_in,))
            conn.commit()
            account_logged_in = 0
            print("The account has been closed!\n")
        if logged_in_input == "5":
            account_logged_in = 0
            print('You have successfully logged out!\n')

        if logged_in_input == "0":
            print('Bye')

            exit()
