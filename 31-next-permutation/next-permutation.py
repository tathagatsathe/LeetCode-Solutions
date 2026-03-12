class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = t = None
        n = len(nums)

        mx = [None]*n

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    if mx[i] == None or nums[j] < nums[mx[i]]:
                        mx[i] = j

        print(mx)

        for i in range(n-1, -1, -1):
            if mx[i] != None:
                temp = nums[mx[i]]
                nums[mx[i]] = nums[i]
                nums[i] = temp
                print('nums: ',nums)
                temp = sorted(nums[i+1:])
                for j in range(i+1, n):
                    nums[j] = temp[j - i - 1]

                return


        # for i in range(n):
        #     if l == None:
        #         l = i
        #     elif t!=None and nums[i] > nums[t]:
        #         l = t
        #         r = i
        #     elif nums[i] <= nums[l]:
        #         t = i
        #     elif r != None and nums[i] > nums[r]:
        #         l = r
        #         r = i
        #     elif nums[i] > nums[l]:
        #         r = i


        # print(l, r, t)
        
        # if l == None or r == None:
        nums.reverse()
        #     return 

        # # if t!=None and nums[t]!=nums[l]:
        # #     r = t

        # temp = nums[r]
        # for i in range(r, l, -1):
        #     nums[i] = nums[i-1]


        # nums[l] = temp


# [1,2,3]
# [2,3,None]

# [3,2,1]
# [None,None,None]

# [1,1,5]
# [5,5,None]

# [1,3,2]
# [2,None,None]

# [1,2,4]
# [2,4,None]

# [1,2,1]
# [2,None,None]

# [2,1,3]
# [3,3,None]

# [2,3,1]
# [3,None,None]