class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        l=[]
        c=0
        for i in range(1,len(mountain)-1):
            
            if (mountain[i-1])<(mountain[i])and mountain[i]>(mountain[i+1]):
                l.append(i)
        return l