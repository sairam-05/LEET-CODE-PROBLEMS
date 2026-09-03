class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        heap=[(-freq,char) for char,freq in counter.items()]
        heapq.heapify(heap)
        res=""
        while heap:
            freq,char=heapq.heappop(heap)
            res+=char*-freq
        return res