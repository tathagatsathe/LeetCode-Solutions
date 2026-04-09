class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        q = len(queries)
        b = int(n**0.5) if n > 100 else 0
            
        q1 = {}

        for l, r, k, v in queries:
            if k > b:
                for idx in range(l, r+1, k):
                    nums[idx] = (nums[idx] * v) % mod
            else:
                if k not in q1:
                    q1[k] = {}

                offset = l % k

                if offset not in q1[k]:
                    q1[k][offset] = []

                start_idx, end_idx = (l - offset) // k, (r - offset) // k
                q1[k][offset].append((start_idx, end_idx, v))

        for k, offsets in q1.items():
            for offset, l_queries in offsets.items():
                lane_len = (n-1-offset)//k + 1
                diff_arr = [1] * (lane_len + 1)

                for start, end, v in l_queries:
                    v_inv = pow(v, mod-2, mod)
                    diff_arr[start] = (diff_arr[start] * v )%mod
                    diff_arr[end + 1] = (diff_arr[end + 1] * v_inv )%mod
                
                curr = 1
                for i in range(lane_len):
                    curr = (curr * diff_arr[i]) % mod
                    global_idx = i * k + offset
                    nums[global_idx]=(nums[global_idx] * curr) % mod
                    

        ans = 0
        for num in nums:
            ans^=num

        return ans