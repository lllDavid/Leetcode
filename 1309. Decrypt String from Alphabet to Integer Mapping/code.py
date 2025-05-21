class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        result = []

        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                result.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i -= 1

        return ''.join(reversed(result))