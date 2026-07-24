class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        heapq.heapify(g)
        heapq.heapify(s)

        while s and g:
            if s[0] >= g[0]:
                heapq.heappop(s)
                heapq.heappop(g)
                content += 1
            else:
                heapq.heappop(s)
        
        return content