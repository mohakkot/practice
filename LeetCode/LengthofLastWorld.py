class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArr = s.split(' ')
        n = len(strArr)
        print(strArr)
        i = n-1
        while (i >= 0):
            if strArr[i] != '':
                return len(strArr[i])
            i-=1
        return 0

print(Solution().lengthOfLastWord(" "));