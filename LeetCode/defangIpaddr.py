class Solution:
    def defangIPaddr(self, address: str) -> str:
        data = []
        if address == "":
            return address
        for s in address:
            if s == '.':
                data.append('[.]')
            else:
                data.append(s)
        return ''.join(data)

print(Solution().defangIPaddr('1.1.1.1'))