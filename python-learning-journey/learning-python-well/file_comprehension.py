import math

#1
# square_numbers = []
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     square_numbers.append(number**2)

# print(square_numbers)


#2

# numbers = [3, 8, 11, 14, 17, 20, 25, 30]
# even_numbers = []
# for number in numbers:
#     if (number % 2) == 0:
#         even_numbers.append(number)

# print(even_numbers)


#3

# names = ["temi", "john", "sarah", "david"]
# capitalized_names = []
# for name in names:
#     capitalized_names.append(name.capitalize())

# print(capitalized_names)



#4
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_evens = []
# for number in numbers:
#     if (number % 2) == 0:
#         squared_evens.append(number ** 2)

# print(squared_evens)



#5
# names = ["  Temi ", " John", "Sarah  ", "  David  ", ""]
# cleaned_names = []
# for name in names:
#     if len(name.strip(" ")) < 1:
#         pass
#     else:
#         cleaned_names.append(name.strip(" "))

# print(cleaned_names)


#6

# students = [
#     {"name": "Temi", "age": 22},
#     {"name": "John", "age": 17},
#     {"name": "Sarah", "age": 25},
#     {"name": "David", "age": 16}
# ]
# legal_students = []

# for student in students:
#     if student["age"] >= 18:
#         legal_students.append(student["name"])

# print(legal_students)



#7
# names = ["Temi", "John", "Sarah", "David"]
# ages = [22, 21, 24, 20]
# name_dict = {}
# postion = 0
# for name in names:
#     name_dict.update({name : ages[postion]})
#     postion +=1 
# print(name_dict)



#8
# products = [
#     {"name": "Laptop", "price": 500000},
#     {"name": "Mouse", "price": 15000},
#     {"name": "Keyboard", "price": 30000},
#     {"name": "Monitor", "price": 120000}
# ]
# expensive_products = []

# for product in products:
#     if product["price"] > 30000:
#         expensive_products.append(product["name"])


# print(expensive_products)


#9
# words = ["python", "robot", "artificial", "intelligence", "AI"]

# for word in words:
#     print(f"{word}: {len(word)}")


#10

# words = ["python", "ai", "python", "robot", "ai", "python"]
# frequency = {}
# count = 1
# for word in words:
#     frequency.update({word : words.count(word)})
 

# print(frequency)


#11

# scores = {
#     "Temi": 85,
#     "John": 72,
#     "Sarah": 91,
#     "David": 64
# }
# grades = {}
# for record in scores:
#     if scores[record] > 90:
#         grades.update({record: "A"})
#     if scores[record] > 80 and scores[record] < 90:
#         grades.update({record : "B"})
#     if scores[record] > 70 and scores[record] < 80:
#         grades.update({record : "C"})
#     if scores[record] > 60 and scores[record] < 70:
#         grades.update({record : "D"})
#     if scores[record] < 60:
#         grades.update({record : "F"})


# print(grades)



#12


# departments = {
#     "Computer Science": ["Python", "AI", "Algorithms"],
#     "Mechanical Engineering": ["Thermodynamics", "CAD"],
#     "Electrical Engineering": ["Circuits", "Control Systems"]
# }

# subcourses = []
# for course in departments:
#     subcourse = departments[course]
#     for element in subcourse:
#         subcourses.append(element)

# print(subcourses)




#13

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# scaled_matrix = [[val * 2 for val in row] for row in matrix]

# greaterthanfive = [[val for val in row if val > 5] for row in matrix]


# print(scaled_matrix)

# print(greaterthanfive)



#14
# users = [
#     {"name": " Temi ", "age": 22, "active": True},
#     {"name": " John", "age": None, "active": True},
#     {"name": "Sarah ", "age": 25, "active": False},
#     {"name": " ", "age": 19, "active": True},
#     {"name": "David", "age": 17, "active": True}
# ]
# cleaned_user = []

# for user in users:
#     user = user.update({"name" : user["name"].strip(" "), "age": user["age"], "active" : user["active"]})


# for element in users:
#     if len(element["name"]) > 1 and element["age"] != None:
#         cleaned_user.append(element)

# print(cleaned_user)


#15


# users = {
#     1: "Temi",
#     2: "John",
#     3: "Sarah",
#     4: "David"
# }

# scores = {
#     1: 87,
#     2: 65,
#     3: 94
# }


# user_list = []
# scores_list = []
# combined = {}

# for score in scores:
#     scores_list.append(scores[score])


# for user in users:
#     user_list.append(users[user])




# while len(user_list) != len(scores_list):
#     if len(user_list) > len(scores_list):
#         user_list.pop(-1)
#     else:
#         scores_list.pop(-1)


# count = 0 
# for user in user_list:
#    combined.update({user: scores_list[count]})
#    count += 1

# print(combined)




#16

# products = [
#     {"name": "Laptop", "price": 500000, "stock": 4},
#     {"name": "Mouse", "price": 15000, "stock": 0},
#     {"name": "Monitor", "price": 120000, "stock": 7},
#     {"name": "Keyboard", "price": 30000, "stock": 2},
#     {"name": "Phone", "price": 350000, "stock": 0}
# ]

# actual_products = []
# for product in products:
#     if product["stock"] >= 1 and product["price"] > 20000:
#         actual_products.append(product)


# print(actual_products)
# prices = []
# names = []
# for stock in actual_products:
#     prices.append(stock["price"] * stock["stock"])
#     names.append(stock["name"])


# print(names)
# print(prices)
# new_dict = {}
# count = 0
# for item in names:
#     new_dict.update({item : prices[count]})
#     count += 1

# print(new_dict)
