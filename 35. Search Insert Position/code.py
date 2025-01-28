class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target not in nums:
                for i in range(len(nums)):
                    if target < nums[0]:
                        nums.insert(0, target)
                        return 0
                    elif target > nums[-1]:
                        nums.append(target)
                        return len(nums) - 1

                    for i in range(len(nums)):
                        if target <= nums[i]:
                            nums.insert(i, target)
                            return i
