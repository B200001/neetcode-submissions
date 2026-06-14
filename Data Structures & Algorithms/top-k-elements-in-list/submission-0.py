class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_m = {}
        for x in nums:
            h_m[x] = h_m.get(x, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in h_m.items():
            bucket[val].append(key)
        
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for x in bucket[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans