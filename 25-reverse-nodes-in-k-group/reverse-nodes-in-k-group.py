# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(node):
            if not node or not node.next:
                return node

            temp=rev(node.next)
            node.next.next=node
            node.next=None
            return temp
        curr=head

        cnt=0
        while curr:
            curr=curr.next
            cnt+=1
        
        if k==0:return head
        if k==1:return head

        loop=cnt//k
        curr=head
        def recu(loop,k,curr):
            if curr is None:
                return None
            if loop==0:
                return curr
            curr1=curr
            for tt in range(k-1):
                curr1=curr1.next
            p=curr1.next
            curr1.next=None
            temp=rev(curr)
            temp2=recu(loop-1,k,p)
            curr.next=temp2

            return temp
        return recu(loop,k,curr)


        