class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        res = []
        sum = 0

        def backtracking(index, current, sum):
            if sum == target:
                res.append(current[:])
                return
            
            if sum > target:
                return

            for i in range(index, len(nums)):
                sum += nums[i]
                
                current.append(nums[i])

                backtracking(i, current, sum)

                sum -= nums[i]

                current.pop()
            
        backtracking(0, current, sum)
        return res