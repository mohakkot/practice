
class Solution:
    def singleNumber(self, nums):
        test = []
        for val in nums:
            if(val in test):
                test.remove(val)
            else:
                test.append(val)
        return(test.pop())

print(Solution().singleNumber([2,2,1]))




