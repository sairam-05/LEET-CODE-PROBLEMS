class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        r=0
        l=tuple(heights)
        heights.sort()
        for i in range(len(l)):
            if l[i]!=heights[i]:
                r+=1
        return r