class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if not char in node.children:
                    return False
                return dfs(index + 1, node.children[char])                    
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)