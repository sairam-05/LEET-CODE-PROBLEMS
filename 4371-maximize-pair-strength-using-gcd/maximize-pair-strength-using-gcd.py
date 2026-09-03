class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ma=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                g=gcd(nums[i],nums[j])
                
                ma=max(ma,nums[i]*nums[j]//(g*g))
        return ma
