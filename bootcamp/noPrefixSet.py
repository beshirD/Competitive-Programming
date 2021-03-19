class Node:
    def __init__(self,char = None):
        self.children = {}
        self.end = False
        self.value = char
class Trie:

    def __init__(self):
       
        self.trie = Node()

    def insert(self, word: str) -> None:
        
        curr_node = self.trie
        for char in word:
            if curr_node.end: 
                return False
            if char not in  curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        if bool(curr_node.children) or curr_node.end:
            return False
        curr_node.end = True
        
        return True
        
def noPrefix(words):
    trie = Trie()
    for word in words:
        if not trie.insert(word):
            print("BAD SET")
            print(word)
            break
    else:
        print("GOOD SET")