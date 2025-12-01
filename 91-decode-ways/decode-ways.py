class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def decodings(s):
            # print('s: ',s)
            if s in dp:
                return dp[s]
            if len(s)==2 and s[0]!="0" and int(s)<=26:
                if s[1]=="0":
                    return 1
                return 2
            if len(s)==1 and s!="0":
                return len(s)
            if s == "":
                return 0

            ans = 0
            if s[0] != "0":
                dec = decodings(s[1:])
                ans+=dec
                if int(s[:2]) <= 26:
                    dec1 = decodings(s[2:])
                    ans+=dec1

            dp[s] = ans
            return dp[s]

        return decodings(s)
