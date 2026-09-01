class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=[]
        re=0
        for i in range(n):
            l.append(start+2*i)
        for i in l:
            re^=i
        return re