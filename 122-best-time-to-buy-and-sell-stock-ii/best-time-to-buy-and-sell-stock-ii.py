class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        mx = prices[0]

        for price in prices:
            if(price<mn or price<=mx):
                mn = price
                mx = price
            elif(price>=mx):
                mx = price
                ans+=(mx-mn)
                mn = price
           

        return ans
        