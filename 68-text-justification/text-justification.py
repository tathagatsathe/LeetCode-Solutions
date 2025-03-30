
import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        arr = []
        temp = []
        rem = maxWidth
        count = 0
        temp_l = 0
        l = []
        c=0
        i=0
        while(i<len(words)):
            word = words[i]
            if(len(temp)!=0):
                c=1
            if(len(word)+c<=rem):
                temp.append(word)
                temp_l+=len(word)
                rem = rem - (len(word)+c)
                i+=1
            else:
                arr.append(temp)
                temp = []
                rem = maxWidth
                c=0
                l.append(temp_l)
                temp_l=0

        arr.append(temp)
        l.append(temp_l)


        # print(arr)
        # print(l)

        i=0
        while(i<len(arr)-1):
            r = l[i]
            rem = maxWidth - r
            j=0
            n= len(arr[i])-1
            m = n
            temp = ""
            while(j<=n):
                if(m==0):
                    t=0
                else:
                    t = math.ceil(rem/m)
                temp+=arr[i][j]
                temp+=" "*t
                rem-=t
                m-=1
                j+=1

            if(rem>0):
                temp+= " "*rem
            ans.append(temp)
            i+=1
        
        temp = ""
        rem = maxWidth
        j = 0
        while(j<len(arr[i])):
            temp+=arr[i][j]
            rem-=len(arr[i][j])
            if(j!=len(arr[i])-1):
                temp+= " "
                rem-=1

            j+=1

        temp+=" "*rem
        ans.append(temp)


        return ans