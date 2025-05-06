class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = sum(len(g) for g in garbage)
        time = 0

        for type in 'MPG':
            last = 0
            for i, g in enumerate(garbage):
                if type in g:
                    last = i
            time += sum(travel[:last])
        
        return total + time