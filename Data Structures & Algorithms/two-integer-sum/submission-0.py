class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            # key: value needed to satisfy target, value: index
            key = target - nums[i]
            if nums[i] in hmap:
                return [hmap[nums[i]], i]

            hmap[key] = i
        
        return []
