import requests
from bs4 import BeautifulSoup
import json
import time

# url = "https://en.wikipedia.org/wiki/Theory_of_relativity"
# headers = {"user-agent" : "mylearningbot/1.0"}

# response = requests.get(url, headers=headers)

# soup  = BeautifulSoup(response.text, "html.parser")

# paragraphs = soup.find_all("p")


# for paragraph in paragraphs:
#     combined_string = "".join(paragraph.text) 


# print(combined_string[0:500])





#2

# if response.status_code == 200:
#     print(response.status_code)
#     print("website is reachable")
# else:
#     print("website is currently unreachable")



# 3

# url = "https://jsonplaceholder.typicode.com/users"
# headers = {"user-agent" : "mylearningbot/1.0"}

# response = requests.get(url, headers=headers)

# py_dict = json.loads(response.text)

# print(py_dict)


4,#5,#6
# def search():
#     try:
#         Decision = ""
#         while Decision != "3":
#             Decision = input("\n1.Search \n2.Get details \n3.Exit")
#             match Decision:
#                 case "1":
#                     user_search = input("Enter a topic you want to search about ").strip(" ")     
#                     url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&titles={user_search}"
#                     headers = {"user-agent" : "mylearningbot/1.0"}
#                     response = requests.get(url, headers=headers)           
#                     print(response.text)
                

#                 case "2":
#                     user_search = input("Enter a topic you want to Get details about ").strip(" ")     
#                     url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&titles={user_search}"
#                     headers = {"user-agent" : "mylearningbot/1.0"}
#                     response = requests.get(url, headers=headers)   
#                     print(response.status_code)
#                     print(response.headers["content-type"])



#     except requests.exceptions.ConnectTimeout as e:
#         print(f"The request timed out: {e}")

#     except requests.exceptions.ConnectionError as e:
#         print(f"A connection error occured: {e}")

#     except requests.exceptions.HTTPError as e:
#         print(f"HTTP error occured: {e}")


# start_time = time.perf_counter()

# search()


# end_time = time.perf_counter()

# exec_time = end_time - start_time

# print(f"The function took {exec_time:.4f}s to run")





#7

# url = "https://jsonplaceholder.typicode.com/posts"

# pay_load = {"name": "John the Doe", "email": "Thefirstname@example.com"}
# response = requests.post(url, json= pay_load)

# print(response.status_code)




#8

# url = "https://en.wikipedia.org/w/api.php?"
# url = "https://httpbin.org/post"

# user_search = input("Enter search: ").strip(" ")
# parameters = [
#     ("action","query"),
#     ("prop", "extract"),
#     ("explaintext", "1"),
#     ("format", "json"),
#     ("titles", user_search)
# ]
# headers = {"user-agent": "mybot/1.0"}
# pay_load = {"name": "John the Doe", "email": "Thefirstname@example.com"}
# try:
#     # response = requests.get(url, timeout=5.0, params=parameters, headers= headers)
#     response = requests.post(url,json= pay_load, timeout= 10.0, params= parameters, headers= headers)
    
#     print(response.status_code)

# except requests.exceptions.ConnectTimeout as e:
#     print("The connection Timed out")


#9

# def search():
#     try:
#         Decision = ""
#         while Decision != "2":
#             Decision = input("\n1.Search \n2.Exit")
#             match Decision:
#                 case "1":
#                     user_search = input("Enter a topic you want to search about ").strip(" ")     
#                     url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&titles={user_search}"
#                     headers = {"user-agent" : "mylearningbot/1.0"}
#                     response = requests.get(url, headers=headers)
#                     response.raise_for_status()
#                     data = response.json()
#                     data["query"]["pages"]["123"]["extract"]
                




#     except requests.exceptions.ConnectTimeout as e:
#         print(f"The request timed out: {e}")

#     except requests.exceptions.ConnectionError as e:
#         print(f"A connection error occured: {e}")

#     except requests.exceptions.HTTPError as e:
#         print(e)

#     except requests.exceptions.InvalidURL as e:
#         print("Invalid Url")

#     except requests.exceptions.RequestException as e:
#         print("Invalid Request")

#     except requests.exceptions.JSONDecodeError as e:
#         print("Invalid JSON response")

#     except KeyError as e:
#         print("The key you are looking for does not exist in the response.")

#     except requests.RequestException as e:
#         print("There was an error")



#10
# page = 1
# url = "https://rickandmortyapi.com/api/character"
# response = requests.get(url, params= {"page":page})
# data = response.json()


# user_request = input("How many resutls do you want: ")
# integer_request = int(user_request)
# search_data = []
# if integer_request > (data["info"]["count"]):
#     print("Request greater than available information")
# else:
#     while True: 
#         response = requests.get(url, params= {"page":page})
#         data = response.json()
#         needed_number = integer_request - len(search_data)
#         for element in data["results"][0:(len(data["results"]))]:
#             if data["results"].index(element) < needed_number:
#                 search_data.append(element)
#         if len(search_data) == integer_request:
#             print("Complete!")
#             break
        
#         page += 1
            


# print(search_data)



#11
url = "https://en.wikipedia.org/w/api.php"

try:
    user_search = input("Enter search: ").strip(" ")
    parameters = [
        ("action","query"),
        ("prop", "extract"),
        ("explaintext", "1"),
        ("format", "json"),
        ("titles", user_search)
    ]
    response = requests.get(url, params=parameters, timeout=5.0)
    response.raise_for_status()
    data = response.json()

    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    title = page.get("title", user_search)
    extract = page.get("extract", "No article extract found.")

    with open("output.txt", "w", encoding="utf-8") as file1:
        file1.write(f"{title}\n\n{extract}")



except requests.exceptions.ConnectTimeout as e:
    print(f"The request timed out: {e}")

except requests.exceptions.ConnectionError as e:
    print(f"A connection error occured: {e}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occured: {e}")

except requests.exceptions.InvalidURL as e:
    print(f"Invalid URL: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request exception: {e}")

except requests.exceptions.JSONDecodeError as e:
    print(f"Invalid JSON response: {e}")

except KeyError as e:
    print(f"The key you are looking for does not exist in the response: {e}")

except FileNotFoundError as e:
    print(f"File not found: {e}")

except IOError as e:    
    print(f"An I/O error occurred: {e}")
