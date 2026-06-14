class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_m = {}
        for i in range(len(nums)):
            h_m[nums[i]] = i
        for i in range(len(nums)):
            
            x = target - nums[i]
            if x in h_m and h_m[x] != i:
                return [i, h_m[x]]
        