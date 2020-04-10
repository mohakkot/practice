class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for c in s:
            if(c == 'L'):
                balance+=1
            else:
                balance-=1
            if (balance == 0):
                count+=1
        return count
print(Solution().balancedStringSplit('RLRRLLRLRL'))

