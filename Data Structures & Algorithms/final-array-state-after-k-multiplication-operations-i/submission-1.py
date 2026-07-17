class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        tuples = []
        for i in range(len(nums)):
            tuples.append((nums[i], i))
        
        heapq.heapify(tuples)

        for i in range(k):
            value, index = heapq.heappop(tuples)
            heapq.heappush(tuples, (value * multiplier, index))

        for t in tuples:
            nums[t[1]] = t[0]
        
        return nums