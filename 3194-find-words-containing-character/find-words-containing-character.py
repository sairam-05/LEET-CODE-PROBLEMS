class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        k=[]
        for i in range(len(words)):
            if x in words[i]:
                k.append(i)
        return k
