class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        s=set()
        for k,v in d.items():
           l.append(v)
           s.add(v)
        return (len(s)==len(l))