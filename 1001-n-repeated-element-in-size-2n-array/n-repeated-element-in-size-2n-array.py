class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        unique_nos = set()

        for num in nums:
            if num in unique_nos:
                return num
            unique_nos.add(num)


        return -1