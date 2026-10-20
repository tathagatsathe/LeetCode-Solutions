class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        nums_sorted = sorted(nums)
        factors = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)

        total_sum = 0

        for k in factors:
            is_sortable = True

            for i in range(0, n, k):
                chunk = nums[i:i+k]
                target_chunk = nums_sorted[i:i+k]
                drops = 0
                drop_idx = -1

                for j in range(k):
                    if chunk[j] > chunk[(j+1)%k]:
                        drops+=1
                        drop_idx = j

                if drops > 1:
                    is_sortable = False
                    break

                if drops == 0:
                    aligned_chunk = chunk
                else:
                    aligned_chunk = chunk[drop_idx+1:] + chunk[:drop_idx+1]
                
                if aligned_chunk != target_chunk:
                    is_sortable = False
                    break
                
            if is_sortable:
                total_sum += k
                
        return total_sum