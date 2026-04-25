class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        for c in s: 
            if c not in map_s:
                map_s[c] = 1
            else:
                new_value = map_s[c] + 1
                map_s[c] = new_value
        
        map_t = {}
        for c in t:
            if c not in map_t:
                map_t[c] = 1
            else:
                new_value = map_t[c] + 1
                map_t[c] = new_value
        
        return map_s == map_t
            
        
        
