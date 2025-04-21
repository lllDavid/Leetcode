class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_a = set()
        seen_b = set()
        common = set()
        result = []

        for i in range(n):
            seen_a.add(A[i])
            seen_b.add(B[i])
            if A[i] in seen_b:
                common.add(A[i])
            if B[i] in seen_a:
                common.add(B[i])
            result.append(len(common))

        return result