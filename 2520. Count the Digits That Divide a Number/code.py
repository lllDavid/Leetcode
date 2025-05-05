class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for digit_char in str(num):
            digit = int(digit_char)
            if digit != 0 and num % digit == 0:
                count += 1
        return count