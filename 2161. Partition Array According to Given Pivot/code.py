class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums2 = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                nums2.append(nums[i])

        for i in range(len(nums)):
            if nums[i] == pivot:
                nums2.append(nums[i])

        for i in range(len(nums)):
            if nums[i] > pivot:
                nums2.append(nums[i])

        return nums2
