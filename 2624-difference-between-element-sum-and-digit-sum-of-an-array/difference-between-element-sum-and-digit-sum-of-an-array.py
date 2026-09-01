class Solution:
   
    def differenceOfSum(self, nums: List[int]) -> int:
        s=0
        ds=0
        for i in nums:
           s+=i
           x=i
           while x:
            m=x%10
            ds+=m
            x//=10
        return s-ds