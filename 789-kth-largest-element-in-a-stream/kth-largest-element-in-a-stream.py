import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.num=nums.copy()
        heapq.heapify(self.num)
        while len(self.num)>self.k:
            heapq.heappop(self.num)
        

        

    def add(self, val: int) -> int:
        heapq.heappush(self.num,val)
        while len(self.num)>self.k:
            heapq.heappop(self.num)
        return self.num[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)