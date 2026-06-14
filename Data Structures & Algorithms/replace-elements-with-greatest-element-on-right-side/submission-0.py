class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def maxi(arr):
            return max(arr)
        
        for i in range(len(arr) - 1):
            arr[i] = maxi(arr[i+1:])
        

        arr[len(arr) - 1] = -1
    
        return arr