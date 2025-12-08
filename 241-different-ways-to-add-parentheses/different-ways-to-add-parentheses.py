class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def fn(exp):
            n = len(exp)

            if n == 1:
                return exp
            ans = []
            for i in range(1,n,2):
                left = fn(exp[:i])
                right = fn(exp[i+1:])
                for l in left:
                    for r in right:
                        if exp[i] == "-":
                            ans.append(l-r)
                        elif exp[i] == "+":
                            ans.append(l+r)
                        elif exp[i] == "*":
                            ans.append(l*r)

            return ans
        n = len(expression)
        i = 0
        arr = []
        j = 0
        while j<n:
            if expression[j] == "+" or expression[j] == "-" or expression[j] == "*":
                arr.append(int(expression[i:j]))
                arr.append(expression[j])
                i=j+1
            j+=1

        arr.append(int(expression[i:j]))

        return fn(arr)