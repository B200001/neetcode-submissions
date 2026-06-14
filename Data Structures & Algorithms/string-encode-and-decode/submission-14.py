class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs)):
            l = len(strs[i])
            res += f"{l}#{strs[i]}"
        
        return res
                
        
    

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            l = int(s[i: j])
            re = s[j + 1:j+l + 1]
            strs.append(re)

            i = j + l + 1
        
        return strs
