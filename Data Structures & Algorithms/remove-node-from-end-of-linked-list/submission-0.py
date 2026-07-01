# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        temp1 = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        dummy = ListNode(0,head)
        left = dummy
        fromStart = length - n 
        while fromStart>0 and left:
            left = left.next
            fromStart -= 1
        left.next = left.next.next
        return dummy.next
        



            




