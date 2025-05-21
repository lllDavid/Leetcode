class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for mid in range(len(s)):
            if freq[s[mid]] < k:
                left = self.longestSubstring(s[:mid], k)
                right = self.longestSubstring(s[mid+1:], k)
                return max(left, right)

        return len(s)
