from trie import Trie,TrieNode
from dictread import create_dict
import time


def insertDict(location, trie):
    with open(location, "r", encoding="cp1251", newline="") as file:
        words = file.readlines()
        print(words[:10])
        for word in words:
            trie.insert(word.rstrip())
            # print(f"Word is : {word}")


def insertDict2(location, trie):
    with open(location, "r", encoding="cp1251", newline="") as file:
        words = []
        for line in file:
            line = line.rstrip('\r\n')
            if line:
                # print(line)
                try:
                    slovo,tolk = line.split(",", 1)
                # tolk = tolk.split(". ", 1)
                    words.append(slovo)
                except ValueError:
                    continue
        # for word in words[:10]:
        #     slovo,tolk = word.split(",", 1)
        #     mest, tolk = tolk.split(". ", 1)
        #     print(slovo)
        #     print(tolk)
        print(words[:10])

        # for word in words:
        #     trie.insert(word.rstrip())

if __name__ == "__main__":
    start = time.time()
    trie = Trie()
    # insertDict("./dictionaries/russian.txt",trie)
    insertDict2("./dictionaries/rudict.txt",trie)
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")

    start = time.time()
    print(trie.search("абажур"))
    print(trie.search("размер"))
    end = time.time()
    total_time = end - start
    print(f"Your programm executed in  {total_time} seconds")