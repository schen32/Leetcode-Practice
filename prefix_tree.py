class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        nextLetters = self.root.children
        for letter in word:

            found = False
            for l in nextLetters:
                if l.val == letter:
                    if letter == word[-1]:
                        l.end = True

                    found = True
                    nextLetters = l.children
                    break
            
            if found:
                continue

            node = TreeNode(letter)
            nextLetters.append(node)
            nextLetters = node.children

    def search(self, word: str) -> bool:
        children = self.root.children
        for letter in word:

            found = False
            for child in children:
                if child.val == letter:
                    found = True
                    children = child.children
                    break
            
            if not found:
                return False
        if children:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        children = self.root.children
        for letter in prefix:
            found = False
            for child in children:
                if child.val == letter:
                    found = True
                    children = child.children
                    break
            
            if not found:
                return False
        return True

tree = PrefixTree()
print(tree.insert("apple"))
print(tree.search("apple"))
print(tree.search("app"))
print(tree.startsWith("app"))
print(tree.insert("app"))
print(tree.search("app"))