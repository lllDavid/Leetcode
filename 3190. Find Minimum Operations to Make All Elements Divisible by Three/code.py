class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in nums:
            if i % 3 == 2:
                i += 1
                operations += 1
            elif i % 3 == 1:
                i -= 1
                operations += 1
                
        return operations
