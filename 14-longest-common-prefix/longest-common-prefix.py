class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word):
        res = ""
        curr = self.root
        for char in word:
            if curr.is_end_of_word:
                return res
            if char not in curr.children:
                curr.is_end_of_word = True
                return res
            curr = curr.children[char]
            res = res + char
        return res
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie = Trie()
        strs.sort(key = lambda x: len(x))
        trie.insert(strs[0])

        if len(strs) == 1:
            return strs[0]

        ans = ""
        for st in strs[1:]:
            ans = trie.search(st)

        return ans
        