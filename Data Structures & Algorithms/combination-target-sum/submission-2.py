class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        last = []
        ans = []


        def func(index, target, ans):
            if target == 0:
                last.append(ans[:])
                return 
            
            if index == len(nums) or target < 0:
                return
            

            ans.append(nums[index])
            func(index, target - nums[index], ans)
            
            ans.pop()
            func(index + 1, target, ans)
            
            
        func(0, target, ans)
        return last
