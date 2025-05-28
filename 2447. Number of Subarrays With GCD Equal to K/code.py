class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            gcd = 0
            for j in range(i, n):
                gcd = math.gcd(gcd, nums[j])
                if gcd < k:
                    break
                if gcd == k:
                    count += 1
        return count