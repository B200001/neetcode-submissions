class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        p[0] = 1
        for i in range(1, len(nums)):
        	p[i] = p[i -1] * nums[i - 1]
        s = [1] * len(nums)
        s[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
        	s[i] = s[i + 1] * nums[i + 1]
        ans = [1] * len(nums)
        for i in range(len(nums)):
        	ans[i] = p[i] * s[i]
        return ans
