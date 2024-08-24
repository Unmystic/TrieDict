# This is a test file for determining the ability to read big dictionary

with open("./dictionaries/russian.txt", "r", encoding="cp1251") as file:
    words = file.readlines()
    for word in words:
        print(f"Word is : {word}")