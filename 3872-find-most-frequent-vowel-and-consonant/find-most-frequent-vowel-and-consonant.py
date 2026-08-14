class Solution:
    def maxFreqSum(self, s: str) -> int:
        dv={}
        dc={}
        s.lower()
        for i in s:
            if i in "aeiou":
                if i in dv:
                    dv[i]+=1
                else:
                    dv[i]=1
            else:
                if i in dc:
                    dc[i]+=1
                else:
                    dc[i]=1
        m=0
        n=0
        for k,v in dc.items():
            if  v>m:
                m=v
        for k,v in dv.items():
            if v>n:
                n=v
        return m+n
        
