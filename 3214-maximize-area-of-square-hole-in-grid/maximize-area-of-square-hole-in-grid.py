class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def getLongestSeq(arr):
            arr.sort()
            temp = 1
            res = 1
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] == 1:
                    temp+=1
                    if temp > res:
                        res = temp
                else:
                    temp = 1

            return res

        longest_seq_h = getLongestSeq(hBars)
        longest_seq_v = getLongestSeq(vBars)

        return (min(longest_seq_h, longest_seq_v) + 1)**2
        