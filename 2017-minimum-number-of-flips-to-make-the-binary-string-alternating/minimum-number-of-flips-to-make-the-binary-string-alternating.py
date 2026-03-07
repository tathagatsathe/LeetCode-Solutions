class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        def countOnes(s):
            no_of_ones_at_odd_pos = no_of_ones_at_even_pos = 0

            for i in range(n):
                if s[i] == "1":
                    if i % 2:
                        no_of_ones_at_even_pos+=1
                    else:
                        no_of_ones_at_odd_pos+=1

            return no_of_ones_at_odd_pos, no_of_ones_at_even_pos

        o, e = countOnes(s)

        odd = even = n//2
        if n%2:
            odd+=1

        if o > e:
            ans = odd - o + e
        else:
            ans = even - e + o

        if n%2:
            for i in range(n):
                o, e = e, o
                if s[i] == "1":
                    o+=1
                    e-=1

                if o > e:
                    if odd - o + e < ans:
                        ans = odd - o + e
                else:
                    if even - e + o < ans:
                        ans = even - e + o

        return ans