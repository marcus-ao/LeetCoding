from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
            
        return False
