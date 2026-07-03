class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        ans = 0
        currLen = 0
        lastIndex = -1

        for i, char in enumerate(s):
            if char in hashmap:
                lastIndex = max(lastIndex, hashmap[char])
            ans = max(ans, i - lastIndex)
            hashmap[char] = i

        return ans