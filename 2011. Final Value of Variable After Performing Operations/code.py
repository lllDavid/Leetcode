class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_dict = {"++X":+1, "X++":+1, "--X":-1, "X--":-1}
        X = 0

        for op in operations:
            X += operations_dict[op]
        return X
