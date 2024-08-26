from trie import Trie,TrieNode
from dictread import create_dict
import time

def insertDict(location, trie):
    with open("./dictionaries/russian.txt", "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
        for word in words:
            trie.insert(word.rstrip())
            # print(f"Word is : {word}")

if __name__ == "__main__":
    start = time.time()
    trie = Trie()
    insertDict("./dictionaries/russian.txt",trie)
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")

    start = time.time()
    print(trie.search("абажур"))
    print(trie.search("размер"))
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")