class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for  i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v>=2:
                l.append(k)
        return l
