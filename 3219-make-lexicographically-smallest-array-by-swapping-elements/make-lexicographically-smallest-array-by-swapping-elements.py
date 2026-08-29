class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        result = [0] * n

        group_indices = []
        group_values = []
        prev_val = None

        for idx in order:
            val = nums[idx]
            if prev_val is not None and val - prev_val > limit:
                for gi, gv in zip(sorted(group_indices), sorted(group_values)):
                    result[gi] = gv
                group_indices, group_values = [], []
            group_indices.append(idx)
            group_values.append(val)
            prev_val = val

        if group_indices:
            for gi, gv in zip(sorted(group_indices), sorted(group_values)):
                result[gi] = gv

        return result