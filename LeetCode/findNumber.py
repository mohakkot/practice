class Solution:
    def findNumbers(self, nums: [int]) -> int:
        result = 0;
        for num in nums:
            if (num >9 and num < 100) or (num> 999 and num < 10000):
                result+=1
        return result

print(Solution().findNumbers([12,346,2,6,7896]))


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, m = 0, 1
        while n > 0:
            s += n % 10
            m *= n % 10
            n = n // 10
        return m - s

print(Solution().subtractProductAndSum(234))