class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = len(nums[0])
        nums.sort()
        temp = "0"*s

        while temp in nums:
            decimal = int(temp,2)
            decimal+=1
            binary = str(bin(decimal)[2:])
            temp = (s - len(binary))*"0" + binary

        return temp
