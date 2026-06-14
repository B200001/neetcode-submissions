class Solution:
    def subsets(self, nums):
        self.last = [] 
        ans = []

        def func(nums, index, ans):
            if index == len(nums):
                self.last.append(ans[:])
                return

            ans.append(nums[index])
            func(nums, index + 1, ans)
            ans.pop()
            func(nums, index + 1, ans)

        func(nums, 0, ans)
        return self.last