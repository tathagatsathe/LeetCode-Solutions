class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                l = j+1
                m = n-1
                while(l<m):
                    if([nums[i],nums[j],nums[l],nums[m]] in ans):
                        l+=1
                        continue
                    if(nums[l]+nums[m]+nums[i]+nums[j] == target):
                        ans.append([nums[i],nums[j],nums[l],nums[m]])
                        l+=1
                    elif(nums[l]+nums[m]+nums[i]+nums[j] > target):
                        m-=1
                    else:
                        l+=1

        return ans