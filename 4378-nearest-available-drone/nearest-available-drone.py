class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx,ty=target
        idx=-1
        best=float("inf")

        for i,(x,y,r) in enumerate(drones):
            ds=abs(x-tx)+abs(y-ty)
            if  ds<=r and ds<best:
                best=ds
                idx=i
        return idx
