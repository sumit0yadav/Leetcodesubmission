# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        hare,tor=head.next,head

        while hare.next and hare.next.next:
            if tor==hare:
                return True
            tor=tor.next
            hare=hare.next.next
        return False


        