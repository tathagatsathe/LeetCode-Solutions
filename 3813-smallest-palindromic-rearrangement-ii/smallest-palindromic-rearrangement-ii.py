import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        
        middle = ""
        H = [0] * 26
        left_half_len = 0
        
        for i in range(26):
            char = chr(i + ord('a'))
            if counts[char] % 2 != 0:
                middle += char
            H[i] = counts[char] // 2
            left_half_len += H[i]
            
        CAP = 10**6 + 1
        
        def get_perms(freq: list) -> int:
            p = 1
            total = 0
            for count in freq:
                if count > 0:
                    total += count
                    p *= math.comb(total, count)
                    if p >= CAP:
                        return CAP
            return p
            
        total_perms = get_perms(H)
        if k > total_perms:
            return ""
            
        left_half = []
        current_k = k
        
        for _ in range(left_half_len):
            for c in range(26):
                if H[c] > 0:
                    H[c] -= 1
                    p = get_perms(H)
                    
                    if current_k <= p:
                        left_half.append(chr(c + ord('a')))
                        break
                    else:
                        current_k -= p
                        H[c] += 1
                        
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]
