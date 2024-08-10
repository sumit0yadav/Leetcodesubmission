# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        minheap=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap,(lists[i].val,i,lists[i]))
        dummy=ListNode(0)
        curr= dummy
        while minheap:

            node,i,linked=heapq.heappop(minheap)
            curr.next=ListNode(node)
            curr=curr.next
            if linked.next:
                
                heapq.heappush(minheap,(linked.next.val,i,linked.next))
        return dummy.next


        