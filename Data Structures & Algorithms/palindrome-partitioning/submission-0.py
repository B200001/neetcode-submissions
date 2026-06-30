class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def solve(start):
            if start == len(s):
                res.append(curr.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]

                if is_palindrome(piece):
                    curr.append(piece)
                    solve(end)
                    curr.pop()

        def is_palindrome(sub):
            return sub == sub[::-1]

        solve(0)
        return res