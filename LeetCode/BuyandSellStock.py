class Solution:
    def maxProfit(self, prices) :
        if len(prices) < 2: return 0

        diff_list = []
        
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                diff_list.append(prices[i] - prices[i-1])
        
        return sum(diff_list)
print(Solution().maxProfit([7,1,5,3,6,4]))
    