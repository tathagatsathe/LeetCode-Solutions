import bisect, math 

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(side * side for x, y, side in squares)
        target_area = total_area / 2
        
        low = min(y for x, y, side in squares)
        high = max(y + side for x, y, side in squares)
        

        for _ in range(100):
            mid = (low + high) / 2
            
            current_area = 0
            for x, y, side in squares:
                if y < mid:
                    height_below = min(y + side, mid) - y
                    current_area += max(0, height_below) * side
            
            if current_area < target_area:
                low = mid
            else:
                high = mid
                
        return low


