class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        n = len(digits)
        if(digits[n-1] != 9):
            digits[n-1]+=1
            return digits
        elif(n==1 and digits[n-1]==9):
            return [1,0]
        else:
            i=n-2
            digits[n-1] = 0
            while(i>=0):
                if(digits[i] == 9):
                    digits[i]=0
                else:
                    digits[i]+=1
                    return digits
                i-=1
            if i==-1:
                digits.insert(0, 1)
                return digits
print(Solution().plusOne([9,9]))