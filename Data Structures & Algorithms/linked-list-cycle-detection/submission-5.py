# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hass = []
        curr = head
        while curr:
            if curr in hass:
                return True
            hass.append(curr)
            curr = curr.next
        return False