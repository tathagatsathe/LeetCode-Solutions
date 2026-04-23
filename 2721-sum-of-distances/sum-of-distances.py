from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        index_map = defaultdict(list)
        sum_map = defaultdict(list)
        arr = []

        for i in range(n):
            index_map[nums[i]].append(i)

        sum_map = { val: sum(indices) for val, indices in index_map.items()}

        count_map = defaultdict(int)
        sum_ = defaultdict(int)

        for i, num in enumerate(nums):
            left_part = i*count_map[num] - sum_[num]

            right_sum = sum_map[num] - (sum_[num] + i)
            right_count = len(index_map[num]) - count_map[num] - 1

            right_part = right_sum - right_count*i

            arr.append(left_part + right_part)

            count_map[nums[i]]+=1
            sum_[num]+=i

        return arr