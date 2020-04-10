class Solution:
    def backspaceCompare(self, S,  T):
        sList= []
        tList = []
        for val in S:
            if(val == "#"):
                if(len(sList) !=0):
                    sList.pop()
            else:
                sList.append(val)
        print(sList)
        for val in T:
            if(val == "#"):
                if(len(tList) !=0):
                    tList.pop()
            else:
                tList.append(val)
        print(tList)
        if(len(sList) != len(tList)):
            return False
        for i in range(len(sList)):
            if(sList[i] != tList[i]):
                return False
        return True
    
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))