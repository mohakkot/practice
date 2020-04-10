class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return checkCount(self.countAndSay(n-1))


def checkCount(s: str) -> str:
    print(len(s))
    result = ""
    i = 0
    while (i < len(s)):
        num = s[i]
        count = 1
        i += 1
        while (i < len(s) and num == s[i]):
            count += 1
            i += 1
        result += str(count) + num
    return result


print(Solution().countAndSay(2))