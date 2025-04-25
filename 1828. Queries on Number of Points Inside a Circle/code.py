class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        
        for qx, qy, r in queries:
            count = 0
            r_squared = r * r
            
            for px, py in points:
                if (px - qx) ** 2 + (py - qy) ** 2 <= r_squared:
                    count += 1
            
            result.append(count)
        
        return result