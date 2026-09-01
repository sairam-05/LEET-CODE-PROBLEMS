class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=[]
        for i in nums:
            k.append(abs(i**2))
       
        k.sort()
        return k