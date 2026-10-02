def gP(left,right,s,answer):
    if(left==0 and right==0):
        answer.append(s)
    if(left>right or left<0 or right<0):
        return
    s+='('
    gP(left-1,right,s,answer)
    s=s[:-1]
    s+=')'
    gP(left,right-1,s,answer)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        s = ""
        gP(n,n,s,answer)

        return answer