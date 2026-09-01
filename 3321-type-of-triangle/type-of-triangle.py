class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums
        if not (a+b>c and a+c>b and b+c>a):
            return "none"
        s=set(nums)
        if len(s)==1:
            return "equilateral"
        elif len(s)==2:
            return "isosceles"
        elif len(s)==3:
            return "scalene"
  

