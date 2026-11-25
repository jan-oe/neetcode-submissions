class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for i in s:
            hash_map_s[i] = hash_map_s.get(i, 0) + 1
        for i in t:
            hash_map_t[i] = hash_map_t.get(i, 0) + 1
        if len(hash_map_s) != len(hash_map_t):
            return False
        try:
            for k in hash_map_s.keys():
                if hash_map_s[k] != hash_map_t[k]:
                    return False

        except:
            return False
        return True