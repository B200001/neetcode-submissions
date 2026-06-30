class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        candidates.sort()

        def solve(index, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            if index >= len(candidates) or target < 0:
                return
            
            curr.append(candidates[index])
            solve(index + 1, target - candidates[index])
            curr.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            solve(index + 1, target)
        
        solve(0, target)
        return res
