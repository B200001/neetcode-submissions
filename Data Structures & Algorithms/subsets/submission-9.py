class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        def solve(start):
            res.append(curr.copy())

            for i in range(start, len(nums)):
                curr.append(nums[i])
                solve(i + 1 )
                curr.pop()
            
        solve(0)
        return res
            
            