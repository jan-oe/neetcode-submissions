class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_s, hash_map_t = {}, {}
        for i in s:
            hash_map_s[i] = hash_map_s.get(i, 0) + 1
        for i in t:
            hash_map_t[i] = hash_map_t.get(i, 0) + 1
        
        if hash_map_s == hash_map_t: 
            return True

        return False