
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.od=OrderedDict()
        self.size=capacity
        

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key]=value
            self.od.move_to_end(key)
        else:
            if len(self.od)<self.size:
                self.od[key]=value
            else:
                self.od.popitem(last=False)
                self.od[key]=value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)