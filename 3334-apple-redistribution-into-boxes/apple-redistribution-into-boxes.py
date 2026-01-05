class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        ans = 0
        for cap in capacity:
            total_apples-=cap
            ans+=1
            if total_apples <=0:
                break


        return ans