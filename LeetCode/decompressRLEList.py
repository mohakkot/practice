class Solution:
    def decompressRLElist(self, nums: [int]) -> [int]:
        if len(nums) <= 1:
            return
        if len(nums) % 2 != 0:
            return
        result = []
        for i in range(0, len(nums), 2):
            result += [nums[i + 1]] * nums[i]
        return result

print(Solution().decompressRLElist([1,2,3,4]))