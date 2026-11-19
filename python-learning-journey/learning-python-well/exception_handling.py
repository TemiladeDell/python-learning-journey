#1

# try:
#     first_number = input("Enter a number: ")
#     second_number = input("Enter another number: ")

#     print(int(first_number) / int(second_number))

# except ValueError:
#     print("Enter valid numbers")


#2

# try:
#     first_number = input("Enter a number: ")
#     second_number = input("Enter another number: ")

#     print(int(first_number) / int(second_number))

# except ValueError:
#     print("Enter valid numbers")

# except  ZeroDivisionError:
#     print("Cannot divide by zero")


#3


# try:
#     age = input("Enter your age: ")
#     hours_slept = input("How many hours do you sleep per night? ")
#     height = input("what is your height? ")
#     if int(age) < 0 or int(hours_slept) < 0 or int(height) < 0:
#         raise ValueError("Age cannot be negative")

# except ValueError as e:
#     print(e)
    

#4

# name = input("Enter the name of the file you want to open: ")

# try:
#     file1 = open(name, "r")
#     print(file1.read())

# except FileExistsError:
#     print("This file does not exist")

# except FileNotFoundError:
#     print("This file wasn't found")

# except OSError:
#     print("This is an invalid file name")



#5

# class InvalidPasswordError(ValueError):
#     '''Raised when user types an invalid password'''

# class EmptyInputError(ValueError):
#     '''Raised when a user enters nothing'''

# class MalformedDataError(ValueError):
#     '''When the data is not in correct format'''

# class UsernameNull(ValueError):
#     '''Raised when the username doesn't exist'''


# user_name = input("Enter your username: ")
# password = input("Enter your password: ")




# try:
#     with open("users.txt", "r") as file1:
#         user_found = False
#         if len(user_name) <  1 or len(password) < 1:
#             raise EmptyInputError("One or more boxes are empty")
        
#         real_file = file1.read()
#         for record in real_file.split("\n"):
#             parts = record.strip().split(":")
#             if len(parts) != 2:
#                 raise MalformedDataError("The data does not exist in correct format")

#             else:
#                 location = record.find(":")
#                 name = record[0:location]
#                 if user_name.lower()  == name.lower():
#                     user_found = True
#                     position = record.find(":") + 1
#                     unlock = record[position:]
#                     if unlock.lower() != password.lower():
#                         raise InvalidPasswordError("The password entered is incorrect")
                
            

#         if user_found == False:
#             raise UsernameNull("User does not exist")
        
        



# except FileNotFoundError:
#     print("File not found")

# except OSError:
#     print("Incorrect file name")

# except UsernameNull as e:
#     print(e)

# except MalformedDataError as e:
#     print(e)

# except InvalidPasswordError as e:
#     print(e)

# except EmptyInputError as e:
#     print(e)


#6
# class WithdrawGreater(ValueError):
#     '''Raised when withdraw amount greater than user balance'''

# class NegativeNumberEntry(ValueError):
#     '''Raised when user enters a negative number'''


# class BankAccount:
#     def __init__(self, name, account_id, balance):
#         self.name = name
#         self.account_id = account_id
#         self.balance = balance


#     def deposit(self):

#         try:
#             deposit_amount = input("Enter how much you want to deposit: ")
#             self.balance += int(deposit_amount)
#         except ValueError:
#             print("Invalid option entered")




#     def withdraw(self):
#         try:
#             withdraw_amount = input("Enter how much you want to withdraw: ")
#             amount = int(withdraw_amount)
#             if amount < 0:
#                     raise NegativeNumberEntry("You cannot enter a negative number")
#             if amount > self.balance:
#                 raise WithdrawGreater("The amount entered is greater than balance")

       
            
#             self.balance -= amount
#         except WithdrawGreater as e:
#             print(e)
#         except NegativeNumberEntry as e:
#             print(e)
#         except ValueError:
#             print("Invalid characters entered")

#     def check_balance(self):
#         return f"Balance: {self.balance}"



# Joseph = BankAccount("Joseph", 215546, 45000)
# Samuel = BankAccount("Samuel", 223345, 18000)
# Sharon = BankAccount("Sharon", 553322, 18000000)

# accounts = [Joseph, Samuel, Sharon]


# def main():
#     confirm_user = input("Please enter your name to continue banking with us: ")
#     for account in accounts:
#         if confirm_user.lower() == account.name.lower():
#             Decision = input("Welcome to Trust bank: \n1.Deposit \n2.Withdraw \n3.Check Balance \n\n")
#             match Decision:
#                 case "1":
#                     account.deposit()
#                 case "2":
#                     account.withdraw()

#                 case "3":
#                     account.check_balance()



# main()




#7

# class WithdrawGreater(ValueError):
#     '''Raised when withdraw amount greater than user balance'''

# class NegativeNumberEntry(ValueError):
#     '''Raised when user enters a negative number'''


# class BankAccount:
#     def __init__(self, name, account_id, balance):
#         self.name = name
#         self.account_id = account_id
#         self.balance = balance


#     def deposit(self):

#         try:
#             deposit_amount = input("Enter how much you want to deposit: ")
#             self.balance += int(deposit_amount)
#         except ValueError:
#             print("Invalid option entered")




#     def withdraw(self):
#         try:

#             withdraw_amount = input("Enter how much you want to withdraw: ")
#             amount = int(withdraw_amount)
#             if amount < 0:
#                     raise NegativeNumberEntry("You cannot enter a negative number")
#             if amount > self.balance:
#                 raise WithdrawGreater("The amount entered is greater than balance")

       
            
#             self.balance -= amount
#         except WithdrawGreater as e:
#             print(e)
#         except NegativeNumberEntry as e:
#             print(e)
#         except ValueError:
#             print("Invalid characters entered")

#     def check_balance(self):
#         return f"Balance: {self.balance}"



# Joseph = BankAccount("Joseph", 215546, 45000)
# Samuel = BankAccount("Samuel", 223345, 18000)
# Sharon = BankAccount("Sharon", 553322, 18000000)

# accounts = [Joseph, Samuel, Sharon]


# def main():
#         confirm_user = input("Please enter your name to continue banking with us: ")
#         for account in accounts:
#             if confirm_user.lower() == account.name.lower():
#                 Decision = ""   
#                 while Decision != "4":
#                         Decision = input("Welcome to Trust bank: \n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Exit \n\n")
#                         match Decision:
#                             case "1":
#                                 account.deposit()
#                             case "2":
#                                 account.withdraw()

#                             case "3":
#                                 print(account.check_balance())
#                             case _:
#                                     print("Invalid option entered. Please try again.")


# main()




#8

# class IncompleteDataError(ValueError):
#     '''Raised when data is missing'''


# file1 = open("students.txt", "r")
# students = file1.read()
# for record in students.split("\n"):
#     try:
#         digits = []
#         if len(record.strip().split("|")) != 4:
#             raise IncompleteDataError("A record in the data is incomplete")
        
#         for element in record.strip().split("|"):
#             if element.isdigit():
#                 digits.append(element)
#         if len(digits) != 2:
#             raise IncompleteDataError("A record in the data is malformed")

#     except IncompleteDataError as e:
#         print(e)
#     continue




#9


