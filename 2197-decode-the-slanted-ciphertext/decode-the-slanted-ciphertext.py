class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l = len(encodedText)
        m = rows
        n = l//m

        ans = ""
        for j in range(n):
            for i in range(m):
                if j+i < n:
                    ans+=encodedText[i*n:(i+1)*n][j+i]

        return ans.rstrip()
        