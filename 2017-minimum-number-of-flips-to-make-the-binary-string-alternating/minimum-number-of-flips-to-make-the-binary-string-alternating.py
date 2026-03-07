class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        print(n)
        continuos_ones = False
        def countOnes(s):
            no_of_ones_at_odd_pos = no_of_ones_at_even_pos = 0
            n = len(s)
            nonlocal continuos_ones
            ones = False

            for i in range(n):
                if s[i] == "1":
                    if i % 2:
                        no_of_ones_at_even_pos+=1
                    else:
                        no_of_ones_at_odd_pos+=1
                    if ones:
                        continuos_ones = True
                    ones = True
                else:
                    ones = False
            return no_of_ones_at_odd_pos, no_of_ones_at_even_pos

        no_of_ones_at_odd_pos, no_of_ones_at_even_pos = countOnes(s)
        
        mx, mn = max(no_of_ones_at_odd_pos, no_of_ones_at_even_pos), min(no_of_ones_at_odd_pos, no_of_ones_at_even_pos)

        print(no_of_ones_at_odd_pos, no_of_ones_at_even_pos)
        o, e = no_of_ones_at_odd_pos, no_of_ones_at_even_pos

        odd = n//2
        even = n//2
        if n%2:
            odd+=1

        ans = even - mx + mn
        if o > e:
            ans = odd - o + e
        else:
            ans = even - e + o
        # print('ans: ',ans, o, e)

        if n%2:
            for i in range(n):
                # print(o, e, s)
                o, e = e, o
                if s[0] == "1":
                    o+=1
                    e-=1
                s = s[1:] + s[0]
                if o > e:
                    temp = odd - o + e
                else:
                    temp = even - e + o
                if temp < ans:
                    ans = temp
                # if even - max(o, e) + min(o, e) < ans:
                #     ans = even - max(o, e) + min(o, e)
                # if s[0] == s[-1] == "1":
                #     break

        return ans
        8 - 4 + 1
        # if no_of_ones_at_odd_pos > no_of_ones_at_even_pos:
        #     ans = odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos
        # else:
        #     ans = even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos

        # print(ans)
        # o, e = 

        # if n%2:
        #     if no_of_ones_at_even_pos > 0 and (s[0] == "1" or s[-1] == "1") and s[0]!=s[-1]:
        #         no_of_ones_at_odd_pos, no_of_ones_at_even_pos = min(no_of_ones_at_odd_pos, no_of_ones_at_even_pos) - 1, max(no_of_ones_at_odd_pos, no_of_ones_at_even_pos) + 1

        #     # if no_of_ones_at_odd_pos > no_of_ones_at_even_pos:
        #     #     temp = no_of_ones_at_odd_pos
        #     #     no_of_ones_at_odd_pos = no_of_ones_at_even_pos
        #     #     no_of_ones_at_even_pos = temp

        #     print(no_of_ones_at_odd_pos, no_of_ones_at_even_pos, odd)

        #     if no_of_ones_at_odd_pos > no_of_ones_at_even_pos:
        #         if odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos < ans:
        #             ans = odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos
        #     else:
        #         if even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos < ans:
        #             ans = even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos

        # return ans
            

        # print(ans)

        for i in range(n):
            s = s[1:] + s[0]
            # temp = no_of_ones_at_odd_pos
            # no_of_ones_at_odd_pos = no_of_ones_at_even_pos
            # no_of_ones_at_even_pos = temp
            no_of_ones_at_odd_pos, no_of_ones_at_even_pos = countOnes(s)
            # if n%2 and s[0] == "1" and s[-1] != "0":


            print(s)
            print(no_of_ones_at_odd_pos, no_of_ones_at_even_pos)
            if no_of_ones_at_odd_pos > no_of_ones_at_even_pos:
                if odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos < ans:
                    ans = odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos
            else:
                if even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos < ans:
                    ans = even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos

            print(no_of_ones_at_odd_pos, no_of_ones_at_even_pos)

        return ans
# 1234567891011
# 01001001101  3, 2
# 10010011010  2, 3
# 00100110101  


# 12345
# 00111

# 101 2, 1
# 011 1, 1