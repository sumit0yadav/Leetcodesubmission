class Node:
    def __init__(self):
        self.child={}
        self.isword=False

class WordDictionary:

    def __init__(self):
        self.root=Node()
        
        

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.child:
                node.child[char]=Node()
            node=node.child[char]
        node.isword=True
        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.isword
            char=word[i]
            if char=='.':
                for child in node.child.values():
                    if dfs(child,i+1):
                        return True
                return False
            else:
                if char in node.child:
                    return dfs(node.child[char],i+1)
                else:
                    return False
        return dfs(self.root,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)