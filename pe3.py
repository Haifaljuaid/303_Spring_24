import datetime
import string

def encode(input_text, shift):
    def shift_letter(letter, shift_amount):
        # Convert letter to lowercase and work only with lowercase alphabet
        if letter.isalpha():
            letter = letter.lower()  # Ensure the letter is lowercase
            alphabet = string.ascii_lowercase  # Use lowercase alphabet for shifting
            
            shifted_index = (alphabet.index(letter) + shift_amount) % 26
            shifted_letter = alphabet[shifted_index]
            return shifted_letter
        else:
            return letter

    if not input_text:
        return (list(string.ascii_lowercase), "")  # Handle empty string case

    # Encode the input text, ensuring the entire operation is lowercase
    encoded_text = ''.join([shift_letter(char, shift) for char in input_text])

    return (None, encoded_text)

def decode(encoded_text, shift):
    # Decode by inverting the shift amount
    return encode(encoded_text, -shift)[1]




def decode(encoded_text, shift):
    return encode(encoded_text, -shift)[1]

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise ValueError("Creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Negative deposit amounts are not allowed.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds for withdrawal.")
            return
        self.balance -= amount

    def view_balance(self):
        print(f"Current balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (datetime.date.today() - self.creation_date).days < 180:
            print("Withdrawals are only permitted after the account has been in existence for 180 days.")
            return
        if self.balance - amount < 0:
            print("Overdrafts are not permitted.")
            return
        super().withdraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= (amount + 30)  # Adjusting to include the withdrawal amount in overdraft scenario
            print("Overdraft incurred. A $30 fee has been applied.")
        else:
            super().withdraw(amount)