class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for mask in range(1 << n):  
            xor_sum = 0
            for i in range(n):
                if (mask >> i) & 1:  
                    xor_sum ^= nums[i]
            total += xor_sum
        return total