class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(index, sum, current):
            # ans.append(current[:])
            if sum == target:
                ans.append(current[:])
                return
            
            if sum > target:
                return

            for i in range(index, len(nums)):
                current.append(nums[i])
                sum += nums[i]
                backtrack(i, sum, current)
                current.pop()
                sum -= nums[i]
            
        
        backtrack(0, 0, [])

        return ans