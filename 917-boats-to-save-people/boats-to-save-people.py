class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        ans=0
        i=0
        j=len(people)-1
        temp = 0
        while(i<j):
            if(people[i]+people[j]<=limit):
                i+=1
            j-=1
            ans+=1
        if(i==j):
            ans+=1

        return ans
