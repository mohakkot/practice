class Solution:
    def countElements(self, arr):
        d = dict()
        count = 0
        for val in arr:
            if(val in d.keys()):
                d[val]+=1
            else:
                d[val] = 1 
        for k,v in d.items():
            if k+1 in d.keys():
                count+=v
        return count


print(Solution().countElements([1,2,3,2]))