class Solution:
    def removeZeros(self, n: int) -> int:
        p=0
        while n:
            
            x=n%10
            if x !=0:
                p=p*10+x
            n=n//10
        p=int(str(p)[::-1])

        return p
        
            