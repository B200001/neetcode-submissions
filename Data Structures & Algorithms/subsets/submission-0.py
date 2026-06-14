class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current = []
        res = []


        def backtrack(index, currrnt):
            res.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        backtrack(0, current)
        return res