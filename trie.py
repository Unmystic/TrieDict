class TrieNode(object):
    def __init__(self) -> None:
        self.children = {}
        self.wordEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.wordEnd = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.wordEnd
    
    def search2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i, c in enumerate(word):
            if c == ".":
                if not curr.children:
                    return False
                for rel in curr.children:
                    x = Trie()
                    x.root = curr.children[rel]
                    if x.search2(word[i+1:]):
                        return True
                return False
            elif c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.wordEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("a")
    trie.insert("a")
    print(trie.search2("."))
    print(trie.search2("a"))
    print(trie.search2("aa"))
    print(trie.search2("a"))
    print(trie.search2(".a"))
    print(trie.search2("a."))
    print(trie.search2(".at"))
    trie.insert("bat")
    print(trie.search2(".at"))
