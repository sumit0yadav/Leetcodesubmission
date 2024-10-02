class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        arr=1
        p.sort(key = lambda x:x[1])
        end=p[0][1]


        for balloon in p[1:]:
            if end<balloon[0]:
                arr+=1
                end=balloon[1]
        return arr


        