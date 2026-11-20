import json
from operator import index

#1

# person_details = {
#     "name": "John Doe",
#     "Age": 34,
#     "Country": "Almeria",
#     "favorite programming language": "Python"
#     }

# y = json.dumps(person_details)

# print(person_details)
# print(y)


#2

# x = '{"name": "Temilade", "age": 22, "language": "Python"}'

# y= json.loads(x)

# print(y)


#3

# x = {
#     "name" : "John Doe",
#     "skills": ["cooking", "Programming"],
#     "Languages": ["Python", "English", "Yoruba"],
#     "Foods" :["Eba", "Rice", "Chicken"]
#     }

# y = json.dumps(x)

# print(y)


#4 

# user = {
#     "name": "John",
#     "Age": 34,
#     "Country": "Almeria"
# }

# user_json =json.dumps(user)

# file1 = open("user.json", "a")
# file1.write(user_json)
# file1.close()


#5 and #6

# file1 = open("user.json", "r")
# actual_file = file1.readline()
# y = json.loads(actual_file)
# y["Age"] = 45
# file1.close()


# file1 = open("user.json", "w")
# x = json.dumps(y) 
# print(x)
# file1.write(x)
# file1.close()


#7
# file1 = open("user.json", "r")
# actual_file = file1.readline()
# x = json.loads(actual_file)

# x["email"] = "xxxxxxxxx@gmail.com"
# x["skills"] = ["Programming", "Engineering", "Cooking"]


# y = json.dumps(x)
# file1.close()
# file1 = open("user.json", "w")
# file1.write(y)
# file1.close()


#8

# file1 = open("test_file.json", "r")

# py_dict = json.load(file1)

# for key in py_dict:
#     print(key["name"])
# file1.close()


#9

# file1 = open("test_file.json", "r")

# py_dict = json.load(file1)

# user_input = input("Enter username: ")

# for key in py_dict:
#     name = key["name"]
#     if name.lower() == user_input.lower():
#         print(key["age"])
#     else:
#         print("user not found")



#10

# file1 = open("user.json", "r")
# x = json.load(file1)
# username = input("Enter your username: ")
# for user in x:
#     if username.lower() == user["name"].lower():
#         print("user found")
#         new_email = input("What would you like to change your email to: ")
#         new_age = int(input("What would you like to change your age to: "))
#         user["email"] = new_email
#         user["Age"] = new_age


# file1.close()
# y = json.dumps(x)
# file1 = open("user.json", "w")
# file1.write(y)
# file1.close()


#11 #12 #13 #14
# def student_database(file_url):
#     file1 = open(file_url, "r")
#     py_dict = json.load(file1)
#     student_data = {}
#     Decision = ""
#     while Decision != "6":
#         Decision = input("What would you like to do today?\1. Add a student\n2. View all students\n3. Search all students taking a course\n4. Calculate Students Average\n5. Delete a student\n6. Exit\n")
#         match Decision:
#             case "1":
#                 student_name = input("Enter name: ")
#                 student_age = input("Enter age")
#                 student_course1 = input("Enter first course: ")
#                 student_course2 = input("Enter second course: ")
#                 student_course3 = input("Enter third course: ")
#                 student_grade1 = int(input("Enter grade for course 1: "))
#                 student_grade2 = int(input("Enter grade for course 2: "))
#                 student_grade3 = int(input("Enter grade for course 3: "))


#                 student_data = {"name" : student_name, "age" : student_age, "courses" : {student_course1: student_grade1, student_course2: student_grade2, student_course3: student_grade3}}
#                 py_dict.append(student_data)
#                 y = json.dumps(py_dict)
#                 file1 = open(file_url, "w")
#                 file1.write(y)
#                 print(py_dict)
#                 file1.close()

#             case "2":
#                 if len(py_dict) < 1:
#                     print("There are no students in database")
#                 else:
#                     print(py_dict)

#             case "3":
#                 course_search = input("Enter a course: ")
#                 for profile in py_dict:
#                     for element  in profile["courses"].keys():
#                         if course_search.lower() == element.lower():
#                             print(profile)
#             case "4":
#                 avg_scores = []
#                 for student in py_dict: 
#                     scores = []
#                     for value in student["courses"].values():
#                         scores.append(value)
#                     one_average = sum(scores)/len(scores)
#                     avg_scores.append(one_average)
#                 if len(avg_scores) >= 1:
#                     print(max(avg_scores))
#                 else:
#                     print("no students in database")
                

#             case "5":
#                 student_found = False
#                 remove_student = input("Enter a student you want to remove: ")
#                 for member in py_dict:
#                     if remove_student.lower() == member["name"].lower():
#                         position = py_dict.index(member)
#                         student_found = True
#                 if not student_found:
#                     print("Student not found")
#                 else:
#                     py_dict.pop(position)
#                     y = json.dumps(py_dict)
#                     file1 = open(file_url, "w")
#                     file1.write(y)
#                     file1.close()
#             case "6":
#                 break

#     file1.close()


# student_database("student_data.json")


#15

# def user_account(file_url):
#     with open(file_url, "r") as file1:
#         user_found = False
#         py_dict =  json.load(file1)
#         user = input("Enter your account name:")
#         for account in py_dict:
#             if user.lower() == account["Account"]["name"].lower():
#                 user_found = True
#                 Decision = ""
#                 while Decision != "5":
#                     Decision = input("What would you like to do today?\n1.Deposit\n2.Withdraw\n3.View balance\n4.View transaction history\n5.Exit")
#                     match Decision:
#                         case "1":
#                             deposit = ""
#                             while not deposit.isdigit():
#                                 deposit = input("How much would you like to deposit?: ")
#                             if deposit.isdigit():
#                                 account["Balance"] += int(deposit)
#                                 d_transaction = (f"Amount Deposited: {deposit}. Available Balance: {account["Balance"]}")
#                                 account["Transactions"].append(d_transaction)
#                                 file1 = open(file_url, "w")
#                                 y = json.dumps(py_dict)
#                                 file1.write(y)
#                                 file1.close()


#                         case "2":
#                             withdraw = ""
#                             while not withdraw.isdigit():
#                                     withdraw = input("Enter a valid amount: ")
#                             while  withdraw.isdigit() and int(withdraw) > account["Balance"]: 
#                                     withdraw = input("Amount greater than balance: ")
#                             if withdraw.isdigit() and int(withdraw) <= account["Balance"]:
#                                     withdraw = int(withdraw)
#                                     account["Balance"] -= int(withdraw)
#                                     w_transaction= (f"Amount withdrwawn: {withdraw}. Available Balance: {account["Balance"]}")
#                                     account["Transactions"].append(w_transaction)
#                                     file1 = open(file_url, "w")
#                                     y = json.dumps(py_dict)
#                                     file1.write(y)
#                                     file1.close()
                                

#                         case "3":
#                             print(f"Available balance: {account["Balance"]}")

#                         case "4":
#                             for transaction in account["Transactions"]:
#                                 print(transaction)

#                         case "5":
#                             print("Exiting Bank")
#         if not user_found:
#              print("user does not exist")



# user_account("transactions.json")



#16
# def log_analyzer(file_url):
#     error_count = 0
#     info_count = 0
#     warning_count = 0
#     with open(file_url, "r") as file1:
#         py_dict = json.load(file1)
#         for log in py_dict:
#             if log["level"] == "ERROR":
#                 error_count += 1
#             if log["level"] == "INFO":
#                 info_count += 1
#             if log["level"] == "WARNING":
#                 warning_count += 1

#         print(f"INFO:{info_count}\nERROR: {error_count}\nWARNING: {warning_count}")

#         error_locator = input("Enter word to search for error message: ")
#         for word in py_dict:
#             if error_locator.lower() in word["message"].lower():
#                 print(word)


# log_analyzer("log.json")
        

#16

# def library(file_url):
#     with open(file_url, "r") as file1:
#         py_dict = json.load(file1)
#         Decision = ""
#         while Decision != "8" :
#             found_book = False
#             Decision = input("What would you like to do?\n1.Add book\n2.Remove book\n3.Search book\n4.Borrow book\n5.Return book\n6.List available books\n7.List borrowed books\n8.Exit\n")
#             match Decision:
#                 case "1":
#                     book_title = input("Enter book title: ")
#                     book_author= input("Enter book author: ")
#                     book_year =  input("Enter book year: ")
#                     book_genre = input("Enter book genre: ")
            
#                     book_data = {"Title": book_title, "Author": book_author, "Year": book_year, "Genre": book_genre, "Available": True, "Borrower": []}
#                     py_dict.append(book_data)
#                     y = json.dumps(py_dict)
#                     file1 = open(file_url, "w")
#                     file1.write(y)
#                     file1.close()


#                 case "2":
#                     remove_book = input("Enter name of book you want to remove: ")
#                     for book in py_dict:
#                         if remove_book.lower() == book["Title"].lower():
#                             position = py_dict.index(book)
#                             py_dict.pop(position)
#                             found_book = True
#                             y = json.dumps(py_dict)
#                             file1 = open(file_url, "w")
#                             file1.write(y)
#                             file1.close()

#                     if not found_book:
#                         print("book does not exist")

#                 case "3":
#                     search_book = input("Enter the title of the book: ")
#                     for book in py_dict:
#                         if search_book.lower() == book["Title"].lower() and book["Available"] == True:
#                             print("book found")
#                             found_book = True
                        

#                     if not found_book: 
#                         print("Book is not available")

#                 case "4":
#                     found_book = False
#                     borrow_book = input("Which book will you like to borrow: ")
#                     for book in py_dict:
#                         if borrow_book.lower() == book["Title"].lower():
#                             if book["Available"] ==  True:
#                                 found_book = True
#                                 name_entry = input("Enter your name: ")
#                                 book["Borrower"].append(name_entry)
#                                 book["Available"] = False
#                                 y = json.dumps(py_dict)
#                                 file1 = open(file_url, "w")
#                                 file1.write(y)
#                                 file1.close()


#                     if not found_book:
#                         print("book not available")

#                 case "5":
#                     found_book = False
#                     return_book = input("Enter book to return: ")
#                     for book in py_dict:
#                         if return_book.lower() == book["Title"].lower():
#                             print("This book has been returned")
#                             book["Borrower"].clear()
#                             book["Available"] = True
#                             found_book = True
#                             y = json.dumps(py_dict)
#                             file1 = open(file_url, "w")
#                             file1.write(y)
#                             file1.close()


#                     if not found_book:
#                         print("This book wasn't borrowed from the libarary")

#                 case "6":
#                     for book in py_dict:
#                         print(book["Title"])

#                 case "7":
#                     for book in py_dict:
#                         if len(book["Borrower"]) > 0:
#                             print(book["Title"])

#                 case "8":
#                     print("Thank you")



# library("books.json")
