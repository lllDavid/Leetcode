class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        n = len(s)

        for i in range(0, n - 1):
            diff = abs(ord(s[i]) - ord(s[i + 1]))
            total += diff
        return total
