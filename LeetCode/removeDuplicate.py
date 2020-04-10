class Solution:
    def removeDuplicates(self, nums):
        final = 1
        j=0
        for i in range(1,len(nums)):
            if (nums[j] != nums[i]):
                temp = nums[j+1]
                nums[j+1] = nums[i]
                nums[i] = temp
                final+=1
                j+=1
        print(nums)
        return final
print(Solution().removeDuplicates([0,0,0,0,1,1,1,1,1,2,2,2,2,33,3,3,3,3,5]))