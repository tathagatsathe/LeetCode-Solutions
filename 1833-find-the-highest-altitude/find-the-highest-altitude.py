class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr_altitude = 0

        for g in gain:
            curr_altitude+=g
            ans = max(ans, curr_altitude)

        return ans