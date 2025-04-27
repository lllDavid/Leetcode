class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        res = []

        for num in nums:
            if freq[num] >= len(res):
                res.append([])
            res[freq[num]].append(num)
            freq[num] += 1

        return res