class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_nums = [0] * 26
        for c in s:
            s_nums[ord(c) - ord('a')] += 1

        t_nums = [0] * 26
        for c in t:
            t_nums[ord(c) - ord('a')] += 1
        
        return t_nums == s_nums
        