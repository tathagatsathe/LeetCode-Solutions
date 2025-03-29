class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = 0
        prev = 0
        i=0
        j = 1
        count = 0

        if(n==1):
            return 1
        while(j<n):
            if(j<n and ratings[j]==ratings[j-1]):
                count=1
                while(j<n and ratings[j]==ratings[j-1]):
                    count+=1
                    j+=1
                
                ans+=count - min(prev, 1)
                prev = 1

            count=1
            if(j<n and ratings[j]<ratings[j-1]):
                while(j<n and ratings[j]<ratings[j-1]):
                    count+=1
                    j+=1
                
                ans+=((count+1)*count)//2 - min(prev,count)
                prev = 1
            # print(count, j, prev, ans)
            count=1
            if(j<n and ratings[j]>ratings[j-1]):
                while(j<n and ratings[j]>ratings[j-1]):
                    count+=1
                    j+=1
                ans+=((count+1)*count)//2 - min(prev,count)
                prev = count


        return ans