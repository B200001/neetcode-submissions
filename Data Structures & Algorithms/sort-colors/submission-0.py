class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0,0,0

        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1
        i = 0
        while red != 0:
            nums[i] = 0
            i += 1
            red -= 1
        
        while white != 0:
            nums[i] = 1
            i += 1
            white -= 1
        while blue != 0:
            nums[i] = 2
            i += 1
            blue -= 1
        