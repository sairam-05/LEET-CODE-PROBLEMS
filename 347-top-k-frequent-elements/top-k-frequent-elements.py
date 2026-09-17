class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        f=[]
        for ke,v in d.items():
            f.append(v)
        f.sort(reverse=True)
        f=f[:k]
        res=[]
        for ke,v in d.items():
            if v in f:
                res.append(ke)
                
        return res

        
