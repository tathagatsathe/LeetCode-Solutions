class Solution:
    def canChange(self, start: str, target: str) -> bool:

        i=0
        sr, tr, sl, tl = 0, 0, 0, 0

        while(i<len(start)):
            if(start[i]=='R'):
                sr+=1
            if(target[i]=='R'):
                tr+=1
            if(start[i]=='L'):
                sl+=1
            if(target[i]=='L'):
                tl+=1
            i+=1

        if (tl!=sl or sr!=tr):
            return False

        i = 0
        j = 0
        rcount = 0
        lcount = 0
        while(i<len(start)):
            if(start[i]=='R'):
                # print('i',i,' ',' j: ',j,' s ',start[i])
                rcount+=1
                while(j<len(target)):
                    if(target[j]=='L' or start[j]=='L'):
                        return False
                    if(target[j]=='R'):
                        rcount-=1
                        j+=1
                        break
                    j+=1
                i+=1
            else:
                i+=1
                if(j<i):
                    j+=1

        if(rcount!=0):
            return False

        # print('rcount: ',rcount)

        # print('i: ',i, 'j: ',j)
        i = len(start) - 1
        j = i
        while(i>=0):
            if(start[i]=='L'):
                lcount+=1
                while(j>=0):
                    if(target[j]=='R' or start[j]=='R'):
                        return False
                    if(target[j]=='L'):
                        lcount-=1
                        j-=1
                        break
                    j-=1
                i-=1
            else:
                i-=1
                if(j>i):
                    j-=1

        # print('i: ',i, 'j: ',j)

        if(lcount!=0):
            return False

        return True


        
        