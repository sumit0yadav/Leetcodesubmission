# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=l1,l2
        dummy=ListNode(0)
        curr=dummy
        sum,rem=0,0
        while curr1 or curr2:
            if curr1:
                print(curr1.val)
                sum+=curr1.val
                curr1=curr1.next
            if curr2:
                print(curr2.val)
                sum+=curr2.val
                curr2=curr2.next
            quo=sum//10
            rem=sum%10
            sum=quo
            print(sum)
            print(quo,rem)
            curr.next=ListNode(rem)
            curr=curr.next
            if not curr1 and not curr2:
                if quo!=0:
                    curr.next=ListNode(quo)
                    curr=curr.next
        return dummy.next
                
            

        