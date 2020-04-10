class Solution:
    def findPeakElement(self, nums):
        maxPeakIndex = -1
        if(len(nums)<=1):
            return 0
        for i in range(1, len(nums)-1):
            if(nums[i-1]< nums[i] and nums[i]> nums[i+1]):
                maxPeakIndex = i
                break
        if(maxPeakIndex == -1):
            if(nums[0]> nums[1]):
                maxPeakIndex = 0
            elif(nums[len(nums)-1] >nums[len(nums)-2]):
                maxPeakIndex = len(nums)-1
            
        return maxPeakIndex
        
print(Solution().findPeakElement([1]))