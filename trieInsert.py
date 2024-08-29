from trie import Trie,TrieNode
from dictread import create_dict
import time
import logging



def insertDict(location, trie):
    with open(location, "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
        for word in words:
            trie.insert(word.rstrip())
            # print(f"Word is : {word}")


# Insertion words from smaller dictionary but with definitions 
def insertDict2(location, trie):
    with open(location, "r", encoding="cp1251", newline="") as file:
        # Creating dict with definitions for every word
        words = []
        wordDict ={}

        # Data from txt file is not clean, so we use filtering and formating of lines
        for line in file:
            line = line.rstrip('\r\n')
            if line:
                try:
                    slovo,tolk = line.split(",", 1)
                    _,tolk = tolk.split(". ", 1)
                    slovo = slovo.title()
                    words.append(slovo)
                    wordDict[slovo] = tolk
                except ValueError:
                    continue
        # print(words[:10])
        # print(len(words), len(wordDict))
        # print(wordDict["Аббат"])

        for word in words:
            trie.insert(word.rstrip())

if __name__ == "__main__":
    start = time.time()
    trie = Trie()
    # insertDict("./dictionaries/russian.txt",trie)
    insertDict2("./dictionaries/rudict.txt",trie)
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")

    start = time.time()
    print(trie.search("Абажур"))
    print(trie.search("Размер"))
    print(trie.autocomplete("Аббат"))
    print(trie.autocomplete("Аб"))
    print(trie.autocomplete("Тре"))
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")