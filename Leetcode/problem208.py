# Leetcode problem 208: Implement Trie (Prefix Tree)
# Difficulty: Medium
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.bool = False
        self.arr = [None]*26
        self.val = ""

class Trie:
    def __init__(self):
        self.start = Node()
        self.pointer = None

    def insert(self, word: str) -> None:
        i = 0
        node_pointer = self.start
        while(i < len(word)):      # traverse the tree until common prefix
            ascii_char = ord(word[i]) - ord('a')
            if(node_pointer.arr[ascii_char] is None):
                break
            node_pointer = node_pointer.arr[ascii_char]
            if(i == len(word)-1):
                node_pointer.bool = True
                break
            i+=1
        
        while(i < len(word)):
            ascii_char = ord(word[i]) - ord('a')
            new_node = Node()
            new_node.val = word[i]
            node_pointer.arr[ascii_char] = new_node
            node_pointer = node_pointer.arr[ascii_char]
            if(i == len(word)-1):
                node_pointer.bool = True
                break
            i+=1
  
        

    def search(self, word: str) -> bool:
        ptr = self.start
        for i in range(len(word)):
            ascii_char = ord(word[i]) - ord('a')
            if(ptr.arr[ascii_char] is not None):
                ptr = ptr.arr[ascii_char]
            else:
                return False
        else:
            return True if(ptr.bool) else False
        
            
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.start
        if(self.start is None):
            return False
        for i in range(len(prefix)):
            ascii_char = ord(prefix[i]) - ord('a')
            if(ptr.arr[ascii_char] is not None):
                ptr = ptr.arr[ascii_char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Time complexity :
# insert: O(m) - where m is the length of the word being inserted.
# search: O(m) - where m is the length of the word being searched.
# startsWith: O(m) - where m is the length of the prefix being searched.