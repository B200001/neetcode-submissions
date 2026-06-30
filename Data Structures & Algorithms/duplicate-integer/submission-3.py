class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = {}
        for num in nums:
            if num in hashm:
                return True
            hashm[num] = 1
        return False