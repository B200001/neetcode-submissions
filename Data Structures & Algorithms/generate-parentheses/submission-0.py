class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def solve(open, close):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            if open < n:
                curr.append("(")
                solve(open + 1, close)
                curr.pop()
            
            if close < open:
                curr.append(")")
                solve(open, close + 1)
                curr.pop()
        solve(0,0)
        return res