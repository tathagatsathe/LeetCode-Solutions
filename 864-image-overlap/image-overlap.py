from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        ones_img1 = []
        ones_img2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones_img1.append((r, c))
                if img2[r][c] == 1:
                    ones_img2.append((r, c))

        if not ones_img1 or not ones_img2:
            return 0
            
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                vector = (r2 - r1, c2 - c1)
                shift_counts[vector] += 1
                
                if shift_counts[vector] > max_overlap:
                    max_overlap = shift_counts[vector]
                    
        return max_overlap