class Solution:
    def simplifyPath(self, path: str) -> str:

        arr = path.split('/')
        arr = list(filter(lambda x: x!="" and x!=".", arr))

        i=0
        while(i<len(arr)):
            if(arr[i]==".."):
                arr.pop(i)
                if(i-1>=0):
                    arr.pop(i-1)
                    i-=1
            else:
                i+=1



        return "/"+ "/".join(arr)

        