class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        n = len(strs)
        idx_count = 0
        ans = []

        for i in range(n):
            freq = [0]*26
            for c in strs[i]:
                freq[ord(c) - ord('a')]+=1
            
            freq_serialized = ",".join([str(x) for x in freq])
            if freq_serialized not in dictionary:
                dictionary[freq_serialized] = idx_count
                idx_count+=1
                ans.append([strs[i]])
            else:
                ans[dictionary[freq_serialized]].append(strs[i])

        return ans