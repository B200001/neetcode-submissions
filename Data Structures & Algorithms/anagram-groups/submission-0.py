class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h_m = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            h_m[key].append(s)
        
        return list(h_m.values())
