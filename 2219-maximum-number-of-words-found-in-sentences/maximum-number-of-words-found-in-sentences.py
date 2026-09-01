class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x=0
        
        for i in sentences:
            n=i.count(" ")+1
            if n>x:
                x=n
        return x

