class Solution:
    def maximum69Number (self, num: int) -> int:
        idx = -1
        i= 0
        n =num
        while num >0 :
            if num%10==6:
                idx = i
            num = num//10
            i+=1
        if idx !=-1:
            return (n + 3*(10**idx))
        else:
            return n
print(Solution().maximum69Number(9669))