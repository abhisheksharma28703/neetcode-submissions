# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        array = []
        for i in range(n):
            first = lists[i]
            while first:
                temp1 = first.next
                array.append(first.val)
                first.next = temp1
                first = first.next
        array.sort()
        array.sort()

        dummy = ListNode()
        curr = dummy

        for val in array:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next




