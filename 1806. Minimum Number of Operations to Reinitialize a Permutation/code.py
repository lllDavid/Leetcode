class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        original = perm.copy()
        count = 0
        
        while True:
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            perm = arr
            count += 1
            
            if perm == original:
                return count