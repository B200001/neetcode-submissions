class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        hash_map2 = {}
        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1
        for c in t:
            hash_map2[c] = hash_map2.get(c, 0) + 1
        
        
        return hash_map == hash_map2