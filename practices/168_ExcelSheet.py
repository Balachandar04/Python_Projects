class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber-1, 26)
            result.append(chr(65+remainder))
        return "".join(reversed(result))


sol = Solution()
print(sol.convertToTitle(200))
