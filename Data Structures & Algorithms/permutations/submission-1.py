class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def solve():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                
                curr.append(nums[i])
                used.add(nums[i])
                solve()

                curr.pop()
                used.remove(nums[i])
            
        solve()
        return res