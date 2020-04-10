class Solution:
    def isHappy(self, n: int):
        check = True
        temp = []
        sol = False
        while(check):
            s = 0
            while(n>0):
                r = n%10
                n = n//10
                s += (r*r)
            if(s==1):
                check = False
                sol= True
            if(s not in temp):
                temp.append(s)
                n = s
            else:
                check = False
        return sol

print(Solution().isHappy(24))