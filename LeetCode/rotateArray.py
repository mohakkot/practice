class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k = k%n
        # i = 0
        # while(i<k):
        #     prev = nums[i]
        #     j = (i+k)%n
        #     while(i!=j):
        #         temp = nums[j]
        #         nums[j] = prev
        #         prev = temp
        #         j = (j+k)%n
        #     nums[i] = prev
        #     print(nums)
        #     i+=1
        # return(nums)

        nums = nums[-k:] + nums[:-k] 
        return(nums)

print(Solution().rotate([1,2], 3))