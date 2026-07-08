class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mod = 10**9 + 7
        ans = []

        pref_sum = [0]*(n+1)
        pref_cnt = [0]*(n+1)
        pref_val = [0]*(n+1)
        pow10 = [1]*(n+1)


        for i in range(1, n+1):
            pref_sum[i] = (pref_sum[i-1] + int(s[i-1])) % mod
            if s[i-1] != "0":
                pref_val[i] = (pref_val[i-1] * 10 + int(s[i-1])) % mod
                pref_cnt[i] = pref_cnt[i-1] + 1
            else:
                pref_val[i] = pref_val[i-1]
                pref_cnt[i] = pref_cnt[i-1]
                
            pow10[i] = (pow10[i-1] * 10) % mod

        for x, y in queries:
            count = pref_cnt[y + 1] - pref_cnt[x]
            concat_number, sum_of_digits = (pref_val[y+1] - pref_val[x] * pow10[count]) % mod, pref_sum[y+1] - pref_sum[x]
            ans.append(concat_number*sum_of_digits % mod)

        return ans
