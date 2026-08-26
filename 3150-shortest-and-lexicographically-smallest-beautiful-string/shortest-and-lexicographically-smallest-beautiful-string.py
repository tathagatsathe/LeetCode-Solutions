class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        left = 0
        right = 0
        n = len(s)
        count_k = 0

        while left < n or right < n:
            if count_k == k:
                if ans == "" or len(s[left:right]) < len(ans) or (len(s[left:right]) == len(ans) and s[left:right] < ans):
                    ans = s[left:right]
                if s[left] == "1":
                    count_k-=1
                left+=1
            elif right < n:
                if s[right] == "1":
                    count_k+=1
                right+=1
            else:
                break

        return ans