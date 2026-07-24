class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        pairs = {u ^ v for u in unique_nums for v in unique_nums}
        
        triplets = {p ^ u for p in pairs for u in unique_nums}
        
        return len(triplets)