class Node:
    def __init__(self,char = None):
        self.children = {}
        self.end = False
        self.value = char
    
class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        sentence = sentence.split()
        trie = Node()
        # insert to prefixes in dictionry to trie
        for word in dictionary:
            curr_node = trie
            for char in word:
                index = ord(char) - ord("a")
                if char not in curr_node.children:
                    curr_node.children[char] = Node(char)
                curr_node = curr_node.children[char]
                
            curr_node.end = True
        # check if word in sentence have prefix in trie and 
        # replace if word have prefix
        for i in range(len(sentence)):
            word = sentence[i]
            curr_node = trie
            prefix = []
            for char in word:
                if char not in curr_node.children:
                    break
                else:
                    
                    curr_node = curr_node.children[char]
                    prefix.append(curr_node.value)
                
                    if curr_node.end:
                        sentence[i] = ''.join(prefix)
                        break
        return ' '.join(sentence)      
                    