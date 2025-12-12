import bisect

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        forward = [0]*n
        backward = [0]*n

        forward[0] = 1
        l = [nums[0]]
        for i in range(1, n):
            idx = bisect.bisect_left(l, nums[i])
            if idx == len(l):
                l.append(nums[i])
            else:
                l[idx] = nums[i]
            forward[i] = len(l)

        l = [nums[-1]]
        backward[n-1] = 1
        for i in range(n-2,-1,-1):
            idx = bisect.bisect_left(l, nums[i])
            if idx == len(l):
                l.append(nums[i])
            else:
                l[idx] = nums[i]
            backward[i] = len(l)

        # print(forward)
        # print(backward)
        ans = n
        for i in range(1, n-1):
            if forward[i] == 1 or backward[i] == 1:
                continue
            f = (i+1 - forward[i]) + (n - i - backward[i])        
            # print(i, nums[i], f)
            if f < ans:
                ans = f

        return ans
