#1

# class student:
#     school = "Elizade"

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course


# student1 = student("Timothy", 19, "Mathematics")
# student2 = student("Sharon", 20, "Chemistry")
# student3 = student("Faraday", 18, "Physics")

# print(student3.course)


#2

# class bank_account:
#     def __init__(self, account_holder, account_number, balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance


#     def deposit_money(self):
#         deposit = ""
#         while not deposit.isdigit():
#             deposit = input("How much would you like to deposit: ")
#         else:
#             self.balance += int(deposit)
#             print(f"You just deposited: {deposit}\nYour balance is: {self.balance}")

#     def withdraw_money(self):
#         withdraw = ""
#         while not withdraw.isdigit() or int(withdraw) > self.balance:
#             withdraw = input("Enter a valid amount: ")
                
        
#         self.balance -= int(withdraw)
#         print(f"You just withdrew: {withdraw}\nYour balance is: {self.balance}")

#     def display_balance(self):
#         print(self.balance)

# bank_account1 = bank_account("Temilade", 12345, 22000)
# bank_account2 = bank_account("Fredrick", 83245, 9700)
# bank_account3 = bank_account("Rachel", 55621, 8200)

# users = [bank_account1, bank_account2, bank_account3]


# def main():
#     user_found = False
#     user_identity = input("Welcome to Trust bank, what is your ID: ")
#     for user in users:
#         if int(user_identity) == user.account_number:
#             user_choice = input("What would you like to do today: \n1.Deposit\n2.Withdraw\n3.Check Balance\n")
#             user_found = True
#             match user_choice:
#                 case "1":
#                     user.deposit_money()
#                 case "2":
#                     user.withdraw_money()
#                 case "3":
#                     user.display_balance()
#     if not user_found:
#         print("This account does not exist ")


# main()



#3
# Shop_Items = []

# class InventoryItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         return self.price * self.quantity

#     def display_info(self):
#         print(f"Item: {self.name}")
#         print(f"Price: ${self.price:.2f}")
#         print(f"Quantity: {self.quantity}")
#         print(f"Total Value: ${self.total_value():.2f}")

#     def add_stock(self):
#         stock_name = input("Enter the name of the item to add stock: ")
#         if stock_name == self.name:
#             print("This stock exist!")
#             stock_quantity = ""
#             while not stock_quantity.isdigit():
#                  stock_quantity = input("How much of this stock do you want to add: ")
#             self.quantity += int(stock_quantity)
#         else:
#             print("This stock doesn't exist!")
#             stock_quantity = ""
#             while not stock_quantity.isdigit():
#                     stock_quantity = input("How much of this stock do you want to add: ")
#             stock_price = input("How much do you want to sell this: ")
#             stock_name = InventoryItem(stock_name, int(stock_price), int(stock_quantity))
#             Shop_Items.append(stock_name)


#     def remove_stock(self):
#         remove_stock = input("Enter the stock you want to remove: ")
#         if remove_stock == self.name:
#              Shop_Items.remove(self)


# Ketchup = InventoryItem("Ketchup", 3200, 14)
# Mustard = InventoryItem("Mustard", 4400, 8)
# Cupcakes = InventoryItem("Cupcakes", 2100, 19)
# Icecream = InventoryItem("Icecream", 8000, 12)
# Fanta = InventoryItem("Fanta", 500, 42)

# Shop_Items = [Ketchup, Mustard, Cupcakes, Icecream, Fanta]



# def main():
#      user_input = input("Welcome to the store. What would you like to do: \n1.Calculate total price\n2.Add stock\n3.Remove stock\n4.Display stock Information\n")
#      match user_input:
#             case "1":
#                 Decision = input("Enter your item: ")
#                 for user in Shop_Items:
#                     if Decision.lower() ==  user.name.lower(): 
#                         user.total_value()

#             case "2":
#                 Decision = input("Enter your item: ")
#                 for user in Shop_Items:
#                     if Decision.lower()  == user.name.lower():
#                         user.add_stock()

#             case "3":
#                 Decision = input("Enter your item: ")
#                 for user in Shop_Items:
#                     if Decision.lower() == user.name.lower():
#                         user.remove_stock()

#             case "4":
#                 Decision = input("Enter your item: ")
#                 for user in Shop_Items:
#                     if Decision.lower() == user.name.lower():
#                         user.display_info()



#4

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#         pass

#     def area(self):
#         pi = 22/7
#         return pi * self.radius**2

#     def diameter(self):
#         return self.radius * 2

#     def circumference(self):
#         pi = 22/7
#         return 2 * pi * self.radius


# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimimeter(self):
#         return (2*self.length + 2*self.width)


# circle1 = circle(7)
# circle2 = circle(18)
# rectangle1 = rectangle(6, 9)
# rectangle2 = rectangle(3, 8)


# area_of_circle1 = circle1.area()
# area_of_circle2 = circle2.area()
# area_of_rectangle1 = rectangle1.area()
# area_of_rectangle2 = rectangle2.area()

# list_of_shapes = [area_of_rectangle1, area_of_rectangle2, area_of_circle1, area_of_circle2]


# print(max(list_of_shapes))


#5

# class library:
#     def __init__(self, name):
#         self.name = name

#     def add_books(self):
#         new_book_name = input("Enter the name the book you want to add: ")
#         new_book_author = input("Enter the name of the author of this book: ")
#         new_book_year = input("Enter the year this book was published: ")
#         book_available = True
#         book_borrower = []

# library_book = []

# class library:
#     def __init__(self):
#        pass

#     class books:
#         def __init__(self, title, author, year, book_available):
#             self.title = title
#             self.author = author
#             self.year = year
#             self.book_available = book_available
    

#         def add_books():
#             book_title = input("Enter the name of the book: ")
#             book_author = input("Enter the author of the book: ")
#             book_year = input("Enter the year of publishing: ")
#             book_available = True

#             book_name = library.books(book_title, book_author, book_year, book_available)
#             library_books.append(book_name)


#         def display_info(self):
#             print(f"Title of Book: {self.title}\nAuthor of Book: {self.author}\nYear published: {self.year}")

#         def remove_books():
#             book_remove = input("Enter the book you want to remove: ")
#             for book in library_books:
#                 if book_remove.lower() == book.title.lower():
#                     library_books.remove(book)




#     class members:
#         def __init__(self, name, age, contact):
#             self.name = name
#             self.age = age
#             self.contact = contact

#         def add_member():
#             member_name = input("Enter your name: ")
#             member_age = input("Enter your age: ")
#             member_contact = input("Enter your email address: ")

#             member_name = library.members(member_name, member_age, member_contact)
#             library_members.append(member_name)

#         def display_info(self):
#             print(f"name: {self.name}\nAge of member: {self.age}\nEmail Address: {self.contact}")



# library_member1 = library.members("Temilade", 22, "Temiladedell@gmail.com")
# library_member2 = library.members("Sharon", 25, "sharonAkinyimika@gmail.com")
# library_member3 = library.members("Joy", 22, "JoyOgundare1@gmail.com")

# library_book1 = library.books("Uncharted", "Simon Fredrick", 2007, True)
# library_book2 = library.books("Pluto", "Himawari Uzumaki", 2014, True)
# library_book3 = library.books("Naruto", "Kishimoto", 2003, True)
# library_book4 = library.books("AOT", "Eren Yeager", 2013, True)

# library_members = [library_member1, library_member2, library_member3]
# library_books =[library_book1, library_book2, library_book3, library_book4]
# borrower_list = []


# def main():
#     Decision = input("Welcome to the Library. Choose an option \n1.Read Book\n2.Return Book\n3.Borrow Book\n4.Become member\n5.Display borrowed books\n6.Add book\n7.Remove book\n\nChoose an Option: ")
#     match Decision:
#         case "1":
#             book_found =False
#             book_chosen = input("Enter the name of the book you wish to read: ")
#             for book in library_books:
#                 if book_chosen.lower() == book.title.lower():
#                     if book.book_available == True:
#                         print("This book is available to read")
#                         book_found = True
#                     else:
#                         print("This book is not available to read")
#                         book_found = True


#             if book_found == False:
#                 print("This book doesn't exist")

#         case "2":
#             found_book = False
#             borrower_found = False
#             borrower_name = input("Enter your name: ")
#             book_chosen = input("Enter the name of the book you want to return: ")
#             for book in library_books:
#                 if book_chosen.lower() == book.title.lower():
#                     if book.book_available == False:
#                         print("book successfully returned")
#                         book.book_available = True
#                         found_book = True
#                         for name in borrower_list:
#                             if borrower_name.lower() == name.lower():
#                                 position = borrower_list.index(name)
#                                 borrower_list.pop(position)
#                                 borrower_found = True
#                         if not borrower_found:
#                             print("not in borrower list")
#                     else:
#                         print("This book is available")
#                         found_book = True
                        
        
                            
                      
#             if found_book == False:
#                 print("This book doesn't belong here")


#         case "3":
#             member_found = False
#             book_found = False
#             book_chosen = input("Enter the name of the book you want to borrow: ")
#             borrower_name = input("Enter your name: ")
#             for member in library_members:
#                 if borrower_name.lower() == member.name.lower():
#                     member_found = True

#             if member_found == False:
#                 become_member = input("Become a member to borrow a book: \n1.Yes\n2.no\n: ")
#                 if become_member == "1":
#                     library.members.add_member()
#                 elif become_member == "2":
#                     print("Okay come again")
#             elif member_found == True:
#                 for book in library_books:
#                     if book_chosen.lower() == book.title.lower():
#                         if book.book_available == False:
#                             print("This book is unavailable")
#                             book_found = True

#                         elif book.book_available == True:
#                             print("This book is available") 
#                             borrower_list.append(borrower_name)
#                             book.book_available = False
#                             book_found =True
#                 if book_found == False:
#                     print("This book wasn't found")


#         case "4":
#             library.members.add_member()


#         case "5":
#             for book in library_books:
#                 if book.book_available == False:
#                     book.display_info()

#         case "6":
#             library.books.add_books()

#         case "7":
#             library.books.remove_books()




# main()



#6

# shoppingcart = []

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


#     def display_info(self):
#         print(f"Product Name: {self.name}\nPrice: {self.price}\n")


# class shopping_cart:
#     def __init__(self):
#         pass

#     def add_products():
#         product_found = False
#         for element in products:
#             print(f'Product: {element}, Price: {products[element]["price"]}')
            
#         select_product = input("What Product will you like to buy: ")
#         for element in products.keys():
#             if select_product.lower() == element.lower():
#                 product_found =True
#                 quantity = products[element]["quantity"]
#                 price = products[element]["price"]
#                 print(f"we currently have {quantity } in stock")
#                 cart = input("How many will you like to add to cart: ")
#                 while int(cart) > quantity:
#                     cart = input("Amount entered greater than stock: ")

#         selection = f"{select_product} : {int(cart) * price}"

#         add_to_cart = input("Would you like to add this selection to cart: \n1.Yes\n2.No\n")
#         match add_to_cart:
#             case "1":
#                 shoppingcart.append(selection)
#             case "2":
#                 customer_decision = input("Would you like to select another product: \n1.Yes\n2.No\n")
#                 match customer_decision:
#                     case "1":
#                         shopping_cart.add_products()
#                     case "2":
#                         print("Thank you for shopping with us")
                                    

#         if product_found == False:
#             print("This product does not exist")

            

        

        

#     def remove_product():
#         count = 0
#         product_found = False
#         for item in shoppingcart:
#             print(f"{count}.{item}")
#             count += 1
#         remove_item = input("Which Item would you like to remove")
#         for selected in shoppingcart:
#             if remove_item.lower() in selected.lower():
#                 product_found = True
#                 position = shoppingcart.index(selected)
                
#         if product_found == True:
#             shoppingcart.pop(position)

#         if product_found == False:
#             print("This Item is not in the cart")

        


#     def total_cost():
#         numbers = []
#         string_sol = " ".join(shoppingcart)
#         for word in string_sol.split(" "):
#             if word.isdigit():
#                 numbers.append(int(word))

#         print(f"The total is: {sum(numbers)}")


#     def display_contents():
#          for element in shoppingcart:
#             print(element)


# products = {
#     "Laptop": {"quantity": 5, "price": 750000},
#     "Phone": {"quantity": 12, "price": 450000},
#     "Headphones": {"quantity": 20, "price": 35000},
#     "Keyboard": {"quantity": 15, "price": 25000},
#     "Mouse": {"quantity": 25, "price": 15000},
#     "Monitor": {"quantity": 8, "price": 180000},
#     "USB Cable": {"quantity": 30, "price": 5000},
#     "Power Bank": {"quantity": 10, "price": 40000},
#     "Tablet": {"quantity": 7, "price": 300000},
#     "Webcam": {"quantity": 9, "price": 55000},
#     "Printer": {"quantity": 4, "price": 220000},
#     "Speaker": {"quantity": 11, "price": 60000},
#     "Flash Drive": {"quantity": 18, "price": 12000},
#     "Router": {"quantity": 6, "price": 85000},
#     "Smartwatch": {"quantity": 13, "price": 95000}
# }


# def main():
#     Decision = input("Welcome to the Every store:\n\n What would you like to do: \n1.Add products to shopping cart\n2.Remove products from shopping cart\n3.Calculate toal price\n4.Display contents of shopping cart:\n\n")
#     match Decision:
#         case "1":
#             shopping_cart.add_products()

#         case "2":
#             shopping_cart.remove_product()

#         case "3":
#             shopping_cart.total_cost()

#         case "4":
#            shopping_cart.display_contents()



# main()


#7

# class employee:
#     def __init__(self, name, identification, employee_type):
#         self.name = name
#         self.identification = identification
#         self.employee_type = employee_type
#         self.employees = []
        
    

#     def add_employee(self):
#         new_employee = f"{self.name} {self.identification} {self.employee_type}"
#         self.employees.append(new_employee)

#     def display_info(self):
#          return f"{self.name}\n{self.identification}\n{self.employee_type}"
         
        
# class part_time_employee(employee):
#     def __init__(self, name, identification, employee_type, hourly_rate, hours_worked):
#         super().__init__(name, identification, employee_type)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
    
#     def salary(self):
#         base_salary  = self.hours_worked * self.hourly_rate
#         return base_salary

#     def display_salary(self):
#         return f"{self.hourly_rate}\n{self.hours_worked}"



# class full_time_employee(employee):
#     def __init__(self, name, identification, employee_type, negotiated_salary):
#         super().__init__(name, identification, employee_type)
#         self.negotiated_salary = negotiated_salary

#     def salary(self):
#         return self.negotiated_salary

    


    


# class contractor(employee):
#     def __init__(self, name, identification, employee_type, pay_per_job, jobs_completed):
#         super().__init__(name, identification, employee_type)
#         self.pay_per_job = pay_per_job
#         self.jobs_completed = jobs_completed

#     def salary(self):
#         wage  = self.pay_per_job * self.jobs_completed
#         return wage

#     def display_salary(self):
#             return f"{self.pay_per_job}\n{self.jobs_completed}"
    


# James = full_time_employee("James Winchester", "F-012201", "full-time employee", 52000)
# Samuel = part_time_employee("Samuel Winchester", "P-332210", "part-time employee", 24, 80)
# Kendrick = contractor("Kendrick Winchester", "C-001234", "contractor", 600, 23)

# print(James.display_info())




#8



# class player:
#     def __init__(self, name, health, attack_power, agility,  alive):
#         self.name = name
#         self.health = health
#         self.attack_power = attack_power
#         self.agility = agility
#         self.is_alive = alive
#         players = []



#     def receive_damage():
#         return "you receive damage"

#     def create_player(self):
#         player_name = input("Enter the name of your character: ")
#         pass




# class warrior(player):
#     def __init__(self, name, health, attack_power, alive):
#         super().__init__(name, health, attack_power, alive)

#     def attack():
#         return "You attack with your axe"


# class Mage(player):
#     def __init__(self, name, health, attack_power, alive):
#         super().__init__(name, health, attack_power, alive)

#     def attack():
#         return "you attack with a fire spell"

# class Archer(player):
#     def __init__(self, name, health, attack_power, alive):
#         super().__init__(name, health, attack_power, alive)

#     def attack():
#         return "you attack with your arrow "


# class game(player):
#     def play(self):
#         player_decision = input("1.Enter Dungeon\n2.Fight another player\n3.Exit")
#         match player_decision:
#             case "1":
#                 zombie_health = 75
#                 first_zombie = input(f"You come accross the first zombie(health: {zombie_health}), he has a bow and arrow and his about to fire. What do you do? \n1.Attack \n2.Dodge \n3.Run")
#                 if self.agility > 50:
#                     if self.attack_power > zombie_health:
#                         if first_zombie == "1":
#                             print("You successfully reach the zombie on time and kill the zombie ")

#                         elif first_zombie == "2":
#                             print("you successfully dodge the zombie's attack")
#                             next_decision = input("The zombie is trying to load another arrow. What do you do? want to do? \n1.Attack \n2.Flee into the dungeon \n3.exit Dungeon")
#                             if next_decision == "1":
#                                 print("You successfully kill the zombie")
#                             elif next_decision == "2":
#                                 print("you escape the zombie, but you might deal with it later")

#                             elif next_decision == "3":
#                                 print("You flee the dungeon")

#                         elif first_zombie == "3":
#                             print("you run for your life and you are able to escape")
#                             self.play()

#                     elif self.attack_power < zombie_health:
#                         if first_zombie == "1":
#                             after_death = input("you arent able to kill the zombie on the first strike and he kills you: \n1.Restart \n2.Exit")
#                             if after_death == "1":
#                                 self.play()
#                             elif after_death == "2":
#                                 print("Thank you for playing")
#                         elif first_zombie == "2":
#                             print("You safely dodge the zombie strike and kill the zombie")
#                         elif first_zombie == "3":
#                             print("You flee the dungeon and the game ends")
#                             self.play()
#                 elif self.agility < 50:
#                     if self.attack_power > zombie_health:
#                         if first_zombie == "1":
#                             print("You cannot reach the zombie ontime and the zombie kills you")

#                         elif first_zombie == "2":
#                             print("you barely dodge the zombie's attack")
#                             next_decision = input("The zombie is trying to load another arrow. What do you do? want to do? \n1.Attack \n2.Flee into the dungeon \n3.exit Dungeon")
#                             if next_decision == "1":
#                                 print("You successfully kill the zombie")
#                             elif next_decision == "2":
#                                 print("while escaping, the zombie shoots you and you die")

#                             elif next_decision == "3":
#                                 print("You barely flee the dungeon")

#                         elif first_zombie == "3":
#                             print("you run for your life and you are able to escape")
#                             self.play()

#                     elif self.attack_power < zombie_health:
#                         if first_zombie == "1":
#                             after_death = input("you arent able to kill the zombie on the first strike and he kills you: \n1.Restart \n2.Exit")
#                             if after_death == "1":
#                                 self.play()
#                             elif after_death == "2":
#                                 print("Thank you for playing")
#                         elif first_zombie == "2":
#                             print("You cannot dodge the zombie strike and the zombie kills you")
#                         elif first_zombie == "3":
#                             print("You flee the dungeon and the game ends")
#                             self.play()

#             case "2":
#                 antagonist = input("Which ")



# def main():
#     Decision  = input("Welcome to Knight and Dragons! \n1. Select character \n2. Exit\n")
#     match Decision:
#         case "1":
#             select_character = input("Choose \n1.Mage\n2.Warrior\n3.Archer")
#             match select_character:
#                 case "1":
#                     print("You have selected a mage")
                    