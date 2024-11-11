# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        
        for i in range(int((length/2))):
            temp = head
            head = head.next
            temp = None
        
        return head
