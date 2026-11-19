# file1 = open("notes.txt", "w")
# file1.write("Python\nMachine Learning\nRobotics\nArtificial Intelligence")
# file1.close()

# file1 = open("notes.txt", "r")
# print(file1.read())
# file1.close()

# file1 = open("notes.txt", "a")
# file1.write("\nComputer Vision")
# file1.close()

# file1 = open("notes.txt", "r")
# lines = len(file1.read().split("\n"))
# print(lines)
# file1.close()

# file1 = open("notes.txt", "r")
# words = len(file1.read().split())
# print(words)
# file1.close()

# file1 = open("notes.txt", "r")
# wordSearch = input("Enter a word to search: ")
# if wordSearch.lower() in file1.read().lower():
#     print("Word found")
# else:
#     print("Word not found")

# diaryEntry = ''
# for i in  range(int(1E10)):
#     diaryEntry = input("Enter your diary entry: ")
#     if diaryEntry.lower() == "close":
#         print("Exiting diary.")
#         break
        
#     else:
#         file1 = open("diary.txt", "a")
#         file1.write(diaryEntry + "\n")
#         print("Entry saved")
#         file1.close()


# def create_user():
#     list_of_users = []
#     print("Welcome to the user registration system")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     file1 = open("users.txt", "a")
#     file2 = open("users.txt", "r")
#     for usr in file2:
#         username_check = usr.split(":")[0]
#         list_of_users.append(username_check)

#     if username not in list_of_users:
#         file1.write(f"{username}:{password}\n")
#         print("User created successfully")
            
#     else:
#         print("this name is unavailable")
#         return
#     file1.close()
#     file2.close()



# def check_user():
#     data = {}
#     file1 = open("users.txt", "r")
#     for element in file1.read().split("\n"):
#         if element:
#             username, password = element.split(":")
#             data[username] = password
#     print("Welcome to the user login system")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username in data and data[username] == password:
#         print("Login successful")
#     else:
#         print("Invalid username or password")

    

# create_user()
# check_user()

# file1= open("text.txt", "r")
# longest_line = []
# for element in file1:
#     longest_line.append(len(element))
# if len(element) == max(longest_line):
#     print(element)
# file1.close()


# file1 = open("source.txt", "r")
# file2 = open("backup.txt", "a")
# copy = []
# for element in file1:
#     copy.append(element)
# print(copy)
# file2.writelines(copy)
# file1.close()
# file2.close()


# def file_statistics(file_url):
#     file1 = open(file_url, "r")
#     line_length = file1.readlines()
#     print(len(line_length))
#     file1.close()

#     file1 = open(file_url, "r")
#     word_count = []
#     for word in file1.read().split(" "):
#         word_count.append(word)
#     print(word_count)
#     file1.close()

#     file1 = open(file_url, "r")
#     char_count = []
#     for element in file1.read():
#         char_count.append(element)
#     print(len(char_count))
#     file1.close()


# file_statistics("source.txt")

# def find_word(file_url):
#     file1 = open(file_url, "r")
    
#     user_input = input("Enter a word: ")
#     sentences  = file1.read().lower().split("\n")
#     for sentence in sentences:
#         if user_input.lower() in sentence.lower():
#             print(sentence)
#     file1.close()
        


# find_word("word_search.txt")


# def log_file(file_url):   
#     file1 = open(file_url, "r")
#     logs = file1.read().split("\n")
#     info_count= []
#     error_count = []
#     warning_count = []
#     for log in logs:
#         if "INFO" in log:
#             info_count.append(log)
#         if "ERROR" in log:
#             error_count.append(log)
#         if "WARNING" in log:
#             warning_count.append(log)


#     print(f"INFO: {len(info_count)}")
#     print(f"ERROR: {len(error_count)}")
#     print(f"WARNING: {len(warning_count)}")
#     file1.close()

        


# log_file("server.log")


# def unique_lines(file_url):
#     file1 = open(file_url, "r")
#     file2 = open("unique_names.txt", "a")
#     lines = file1.read().split("\n")
#     unique = list(dict.fromkeys(lines))
#     for word in unique:
#         file2.write(word + "\n")




# unique_lines("names.txt")



# def replace_text(file_url):
#     file1 = open(file_url, "r")
#     file2 = open("replaced_file.txt", "w")

#     word = input("Enter a word to replace: ")
#     replacer = input("Enter a word to replace with: ")

#     sentences = file1.read().split("\n")

#     for sentence in sentences:
#         if word.lower() in sentence.lower():
#             file2.write(f"{sentence.replace(word, replacer)}\n")
#     file1.close()
#     file2.close()


# replace_text("message.txt")



# def transactions(file_url):
#     file1 = open(file_url, "r")
#     sentences = file1.read().split("\n")
#     starting_balance = 10000
#     final_balance = 0
#     deposit_list = []
#     wihdraw_list = []
#     actual_deposit = []
#     actual_withdraw = []



#     for sentence in sentences:
#         if "deposit" in sentence.lower():
#             deposit_list.append(sentence)
#         if "withdraw" in sentence.lower():
#             wihdraw_list.append(sentence)


    
#     deposit_amount = " ".join(deposit_list)
#     for number in deposit_amount.split(" "):
#         if number.isdigit():
#             actual_deposit.append(int(number))


#     withdraw_amount = " ".join(wihdraw_list)
#     for figure in withdraw_amount.split(" "):
#         if figure.isdigit():
#             actual_withdraw.append(int(figure))

#     withdraw = sum(actual_withdraw)
#     deposit = sum(actual_deposit)

#     print(f"Starting balance: {starting_balance}")
#     print(f"Final balance: {starting_balance + deposit - withdraw}")

    

    




# transactions("transactions.txt")



# def most_frequent_word(file_url):
#     counter = {}
#     file1 = open(file_url, "r")
#     sentences = file1.read().lower().split("\n")
#     word_list = []
#     for sentence in sentences:
#         word_list.append(sentence)

#     the_string = " ".join(word_list)
#     the_string_no_punctuation = the_string.split(".")
#     one_string =  " ".join(the_string_no_punctuation)



#     for element in one_string.split(" "):
#         if element in counter:
#             counter[element] += 1
#         else:
#             counter[element] = 1

#     max_number = max(counter, key=counter.get)
#     print(f"Frequent word: {max_number} - {counter[max_number]}")


# most_frequent_word("message.txt")