import sqlite3
import subprocess

# con = sqlite3.connect('my_example.db')

# cur = con.cursor()

# # cur.execute("Create table movie(title, year, score)")

# # cur.execute("""insert into movie values 
# #                 ('Iron man', '2008', '9.4'),
# #                 ('Wreck-it-ralph', '2012', '8.8')
# # """)

# # con.commit()
# # data = [
# #     ('Inception','2011','9.2'),
# #     ('Interstellar','2016','9.8'),
# #     ('Cars','2008','8.6')
# # ]

# # cur.executemany("Insert into movie values (?, ?, ?)", data)
# # con.commit()

# res = cur.execute("select * from movie")
# print(res.fetchall())


conn = sqlite3.connect('test.db')

cur = conn.cursor()

# cur.execute("create table Students(Name, Age, Course, Score)")

# cur.execute("""
#             Insert into Students values

#             ('Temilade', '22', 'Physics', '98'),
#             ('Blessing', '22', 'Mathematics', '100'),
#             ('Emmanuel', '21', 'JavaScript', '99'),
#             ('Samuel', '19', 'Geography', '86'),
#             ('Tammy', '20', 'Biology', '84'),
#             ('Korede', '18', 'Chemistry', '73'),
#             ('Garfield', '24', 'English', '96'),
#             ('Tommiwa', '17', 'Government', '82'),
#             ('Timilehin', '19', 'Economics', '91'),
#             ('Kenny', '21', 'Literature', '93')
# """)

# conn.commit()

# 1 all columns
# exec = cur.execute("select * from Students")
# print(exec.fetchall())

#2 one named column
# exec = cur.execute("select name from Students")

#3 Showing table data
# exec = cur.execute("Pragma table_info(Students)")

# 4 adding a column
# exec = cur.execute("Alter table Students add column matric_no text")

# 5 Removing a column
# exec = cur.execute("Alter table Students Drop column matric_no ")


# exec = cur.execute("select * from Students where cast(Age as integer) > 20")
# exec = cur.execute("select * from Students where Course = 'Physics'")

# exec = cur.execute("select * from Students where cast(Score as integer) > 90")

exec = cur.execute("select * from Students where cast(Score as integer) > 90 and cast(Age as integer) < 20")
print(exec.fetchall())


# fetching one row
# print(exec.fetchone())

try:
    user_input = input("Enter your name: ")
    res = cur.execute("select * from Students where name = ?", (user_input,))
    data = res.fetchall()
    print(data)


    if len(data) > 0:
        change_course = input("What would you like to change your course to: ")
        cur.execute("update students set course = ? where Name = ?",(change_course, user_input))
    else:
        raise sqlite3.DatabaseError("No record found")

    conn.commit()

except sqlite3.DatabaseError as e:
    print(e)

except sqlite3.Error as e:
    print("An error occured")
