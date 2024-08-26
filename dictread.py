# This is a test file for determining the ability to read big dictionary
import time
from pprint import pprint
def create_dict(location):
    library = []
    with open("./dictionaries/russian.txt", "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
        for word in words:
            library.append(word)
            # print(f"Word is : {word}")
        print(len(library))
        # print(library)

if __name__ == "__main__":
    start = time.time()
    create_dict("./dictionaries/russian.txt")
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")