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
    
    # simple search with no allowed sym substitutions
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
    
    # Implementation of autocomplete feature
    def searchNode(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr
    
    def autocomplete(self,word):
        node = self.searchNode(word)
        if not node:
            return []
        suggestions = []
        self.findWords(node,word,suggestions)
        return suggestions
    
    def findWords(self,node,word,suggestions):
        if len(suggestions) > 5:
            return
        if node.wordEnd:
            suggestions.append(word)
        for char, next_node in node.children.items():
            self.findWords(next_node, word + char, suggestions)

    # def _search_node(self, prefix):
    #     node = self.root
    #     for char in prefix:
    #         if char not in node.children:
    #             return None
    #         node = node.children[char]
    #     return node

    # def autocomplete(self, prefix):
    #     node = self._search_node(prefix)
    #     if not node:
    #         return []

    #     suggestions = []
    #     self._find_words(node, prefix, suggestions)
    #     return suggestions

    # def _find_words(self, node, prefix, suggestions):
    #     if node.is_end_of_word:
    #         suggestions.append(prefix)

    #     for char, next_node in node.children.items():
    #         self._find_words(next_node, prefix + char, suggestions)

    
    # More complex search with 1 allowed substitution
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
