class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h_m = {}

        for c in s:
            h_m[c] = h_m.get(c, 0) + 1
        
        for c in t:

            if c in h_m:
                h_m[c] -= 1
                if h_m[c] == 0:
                    del h_m[c]
        
        return len(h_m) == 0
        