# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k==0 or k==1:
            return head

        def rev(node):
            if not node or not node.next:
                return node
            temp=rev(node.next)
            node.next.next=node
            node.next=None
            return temp
        
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        loop=length//k

        def recu(node,loop,k):
            if node is None or loop==0:
                return node
            curr1=node
            for tt in range(k-1):
                curr1=curr1.next
            p=curr1.next
            curr1.next=None
            rev(node)
            pp=recu(p,loop-1,k)
            node.next=pp
            return curr1
        return recu(head,loop,k)


        