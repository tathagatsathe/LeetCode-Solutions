class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False
        self.index = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, index):
        curr = self.root
        for c in key:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.index = index
        curr.isLeaf = True

    def searchPrefix(self, key):
        curr = self.root
        prev = curr
        for c in key:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                return curr.index
            prev = curr
            curr = curr.children[idx]

        return curr.index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ans = []

        trie = Trie()
        
        wordsContainer = [(len(word), idx, word[::-1]) for idx, word in enumerate(wordsContainer)]
        wordsContainer.sort(reverse=True)

        min_idx = wordsContainer[-1][1]

        for _, idx, word in wordsContainer:
            trie.insert(word, idx)

        for query in wordsQuery:
            l = trie.searchPrefix(query[::-1])
            if l == None:
                ans.append(min_idx)
                continue
            ans.append(l)

        return ans


