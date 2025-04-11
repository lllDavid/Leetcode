class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def helper(n, base):
            digits = []
            while n > 0:
                digits.append(n % base)
                n //= base
            return digits == digits[::-1]

        for base in range(2, n - 1):
            if not helper(n, base):
                return False
        return True