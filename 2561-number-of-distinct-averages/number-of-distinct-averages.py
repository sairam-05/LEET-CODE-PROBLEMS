class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        r=[]
        for i in range(len(nums)//2):
            mi=min(nums)
            ma=max(nums)
            av=(mi+ma)/2
            r.append(av)
            nums.remove(mi)
            nums.remove(ma)
        return len(list(set(r)))