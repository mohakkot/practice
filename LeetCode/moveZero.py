class Solution:
    def moveZeroes(self, nums):
        i=0
        j=1
        while(j<len(nums)):
            print(nums[i], nums[j])
            if(nums[i]==0 and nums[j]==0):
                j+=1
            elif(nums[i]==0):
                temp = nums[j]
                nums[j]= nums[i]
                nums[i] = temp
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        return(nums)



print(Solution().moveZeroes([1,1,1,0,1]))