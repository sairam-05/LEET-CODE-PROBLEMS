class Solution:
    def processStr(self, s: str) -> str:
        res=[]

        for i in s:
            i.lower()
            if i.isalpha():
                res.append(i)
                print(res)
            elif i=="*" and len(res)>=1:
                res.pop()
            elif i=="#":
                res+=res
            elif i=="%":
                res.reverse()
                
        return "".join(res)