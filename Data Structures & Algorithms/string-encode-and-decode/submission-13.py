class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            st = s[j + 1: j + 1 + length]
            ans.append(st)
            i = j + 1 + length
        
        return ans