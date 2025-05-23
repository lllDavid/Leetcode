class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        result = []

        for i in range(m):
            r, c = startPos
            count = 0
            
            for j in range(i, m):
                move = s[j]
                if move == 'L':
                    c -= 1
                elif move == 'R':
                    c += 1
                elif move == 'U':
                    r -= 1
                elif move == 'D':
                    r += 1

                if r < 0 or r >= n or c < 0 or c >= n:
                    break
                count += 1

            result.append(count)

        return result