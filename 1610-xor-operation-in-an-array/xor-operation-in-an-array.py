class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        for i in range(n):
            l.append(start)
            start=start+2
        res=l[0]
        for i in range(1,len(l)):
            res^=l[i]
        return res
