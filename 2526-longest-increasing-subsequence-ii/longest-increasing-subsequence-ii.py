class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        size = n + 1
        tree = [0]*2*size

        def update(num, longest_lis):
            num+=size
            if tree[num] < longest_lis:
                tree[num] = longest_lis
                while num > 1:
                    tree[num>>1] = max(tree[num], tree[num^1])
                    num>>=1

        def query(l, r):
            res = 0
            l+=size
            r+=size
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l+=1
                if r & 1:
                    r-=1
                    res = max(res, tree[r])
                l>>=1
                r>>=1
            
            return res

        res = 0 
        for num in nums:
            lower_bound = max(num-k,0)
            longest_lis = query(lower_bound, num)
            update(num, longest_lis+1)

        return query(0, size)