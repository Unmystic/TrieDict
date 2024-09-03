# TrieDict
## Simple python Trie adaptation with example of dictionary loadout.

Trie is a variation of tree datastructure, that well suited for quick comparison purposes, such as Autocomplete.
In its base form it consist of tree class and its constructor - node class. Per <code>trie.py</code> :
```
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
```

Trie file includes all fuctionality methods for default trie operations: search and insertion. Core of autocomplete fuctionality also in  Trie class methods.

File `dictread.py` describes simple File open interaction. Used only for test purposes. 

`trieInsert.py` implements two different examples of dictionaries insertion. Raw data used in examples required cleanup, so there different stages of filtration  + try/except.
For more proffessional uses input dictionaries must be better prepared, but for the examplery use it is enough.

Final script file `autoc.py` creates GUI realization of Autocomplete usin flet framework. Design is simple, but functional.

## Prerequisits

For CLI Trie uses Python is enough. For GUI version must install flet + its platform dependecies, consult  [official flet site](https://flet.dev/docs/getting-started/)
