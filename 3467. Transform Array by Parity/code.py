class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i, v in enumerate(nums):
            if v % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        for j in range(len(nums)):
            for k in range(len(nums) - j - 1):
                if nums[k] > nums[k+1]:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
        return nums