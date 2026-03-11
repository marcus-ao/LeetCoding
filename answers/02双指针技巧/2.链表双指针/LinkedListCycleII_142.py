from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            assert slow is not None
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head

                while slow != fast:
                    assert slow is not None
                    slow = slow.next
                    fast = fast.next

                return slow

        return None
