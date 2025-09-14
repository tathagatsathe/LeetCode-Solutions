import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def xSum(nums):
            heap = []
            d = [0]*51
            for num in nums:
                d[num]+=1

            for i in range(len(d)):
                heapq.heappush(heap, (-d[i], -i))
            m = 0
            ans = 0
            while m<x:
                nb, occ = heapq.heappop(heap)
                ans+=(nb*occ)
                m+=1

            return ans

        i = 0
        ans = []
        while(i+k<=len(nums)):
            ans.append(xSum(nums[i:i+k]))
            i+=1

        return ans

        

