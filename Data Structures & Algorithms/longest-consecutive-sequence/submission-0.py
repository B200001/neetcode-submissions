class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in s:
                smallest = n
                count = 1
                while smallest + 1 in s:
                    count += 1
                    smallest += 1
                longest = max(longest, count)
        return longest