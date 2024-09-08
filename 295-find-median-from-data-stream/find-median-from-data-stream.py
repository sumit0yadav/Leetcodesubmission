import heapq
class MedianFinder:

    def __init__(self):
        self.mini,self.maxi=[],[]
        

    def addNum(self, num: int) -> None:
        mini,maxi=self.mini,self.maxi
        if not maxi:
            heapq.heappush(maxi,-num)
        elif maxi and len(mini)!=len(maxi):
            ele=-maxi[0]
            if ele<=num:
                heapq.heappush(mini,num)
            else:
                heapq.heappush(maxi,-num)
                x=heapq.heappop(maxi)
                heapq.heappush(mini,-x)



        elif maxi and len(mini)==len(maxi):
            ele=-maxi[0]
            if num<ele:
                heapq.heappush(maxi,-num)
            else:
                heapq.heappush(mini,num)
                x=heapq.heappop(mini)
                heapq.heappush(maxi,-x)

        

    def findMedian(self) -> float:
        mini,maxi=self.mini,self.maxi
        if len(mini)==len(maxi):
            return (mini[0]-maxi[0])/2
        return -maxi[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()