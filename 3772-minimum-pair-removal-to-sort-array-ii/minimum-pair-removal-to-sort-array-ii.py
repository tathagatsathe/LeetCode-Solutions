import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        h = []
        deleted = set()
        n = len(nums)
        pair_sums = [0]*n
        adjacents = [[i-1, i+1] for i in range(n)]
        inversions = 0
        for i in range(n-1):
            heapq.heappush(h, (nums[i]+nums[i+1], i))
            pair_sums[i] = nums[i]+nums[i+1]
            if nums[i+1] < nums[i]:
                inversions+=1
            if i == 0:
                adjacents[i] = [-1, 1]
            else:
                adjacents[i] = [i-1, i+1]
        
        # print('inversions: ',inversions)
        deleted = [False]*n
        ans = 0
        while inversions and h:
            # print('______________________________________________________')
            sum_, idx = heapq.heappop(h)
            prev, nxt = adjacents[idx]
            # print('nums: ',nums)
            # print('adjacents: ',adjacents)
            # print('pair_sums: ',pair_sums)
            if sum_ != pair_sums[idx] or deleted[idx] == True:
                continue
            if nxt < n:
                if nums[idx] > nums[nxt]:
                    # print('nxt')
                    inversions-=1
                next_ = adjacents[nxt][1]
                if next_ < n:
                    if nums[nxt] <= nums[next_] and sum_ > nums[next_]:
                        # print('next_')
                        inversions+=1
                    if nums[nxt]>nums[next_] and sum_<=nums[next_]:
                        inversions-=1
            
            if prev >=0:
                if nums[prev]>nums[idx] and sum_>=nums[prev]:
                    # print('prev')
                    inversions-=1
                if nums[idx]>=nums[prev] and sum_<nums[prev]:
                    inversions+=1

            
            
            
            nums[idx] = sum_
            # print('idx: ',idx, prev, nxt, ' inversions: ',inversions, ' sum_: ',sum_, ' ans: ', ans)

            if nxt<n:
                ans+=1
                if prev>=0:
                    heapq.heappush(h, (sum_ + nums[prev], prev))
                    pair_sums[prev] = sum_ + nums[prev]
                next_ = adjacents[nxt][1]
                deleted[nxt] = True
                if next_<n:
                    heapq.heappush(h, (sum_ + nums[next_], idx))
                    pair_sums[idx] = sum_ + nums[next_]
                    adjacents[next_] = [idx, adjacents[next_][1]]
                adjacents[idx] = [prev, next_]
                
        
        return ans
