class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hash_set = {}
        for i in range(len(nums)):
            hash_set[nums[i]] = i
        
        for i in range(len(nums)):
            x = target - nums[i]

            if x in hash_set and hash_set[x] != i:
                return [i, hash_set[x]]

            
            