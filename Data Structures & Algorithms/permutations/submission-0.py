class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res  = []
        curr = []
        used = set()

        def solve():
            # 1. base case
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            # 2. har element try karo
            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                curr.append(nums[i])   # PICK
                used.add(nums[i])
                solve()

                curr.pop()             # UNDO
                used.remove(nums[i])   # next iteration = SKIP

        solve()
        return res