class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
                
        return duplicates

        print(findSneakyNumbers([0,1,1,0]))  
        print(findSneakyNumbers([0,3,2,1,3,2])) 