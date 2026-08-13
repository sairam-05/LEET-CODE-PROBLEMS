class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        while n>0:
            x=n%10
            if x in d:
                d[x]+=1
            else:
                d[x]=1
            n=n//10
        res=0
        m=0
        for k,v in d.items():
            m=k*v
            res+=m
        return res