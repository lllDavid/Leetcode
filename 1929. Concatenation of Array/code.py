class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        n = len(nums)
        for i in range(n):
            arr1.append(nums[i])
            arr2.append(nums[i])
        return arr1+arr2