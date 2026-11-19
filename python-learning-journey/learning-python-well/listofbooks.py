import os

folder1 = os.listdir("C:/Users/USER/Desktop/GoodBooks")

for file in folder1:
    if file.endswith("pdf"):
        print(file)