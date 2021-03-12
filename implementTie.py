class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.trie
        for char in word:
            
            if char not in  curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.end = True
        return 

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.trie
        for char in word:
            
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.end:
            return True
        return False
           

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.trie
        for char in prefix:
          
            if char in  curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True
class Node:
    def __init__(self,char = None):
        self.children = {}
        self.end = False
        self.value = char
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)