class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s=set(nums[0])
        for i in nums:
            s=s.intersection(set(i))
        l1=list(s)
        l1.sort()
        return l1

            