class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []

        def fn(s, res):
            nonlocal ans
            if (res.count(".") > 3) or (res.count(".") == 3 and s != "" and int(s) > 255):
                return
            if s == "" and res.count(".") == 3:
                ans.append(res)

            temp = ""
            for i in range(min(3, len(s))):
                temp+=s[i]
                if len(temp) > 1 and temp[0] == '0':
                    break
                if 0 <= int(temp) <= 255:
                    t = ""
                    if res != "":
                        t = res + "." 
                    fn(s[i+1:], t + temp)

        
        fn(s, "")

        return ans