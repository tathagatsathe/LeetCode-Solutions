class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest_odd = None
        
        for i, val in enumerate(nums1):
            if val % 2 and (smallest_odd == None or val < smallest_odd):
                smallest_odd = val

        for i, val in enumerate(nums1):
            if val % 2 == 0 and (smallest_odd != None and val <= smallest_odd):
                return False

        return True
