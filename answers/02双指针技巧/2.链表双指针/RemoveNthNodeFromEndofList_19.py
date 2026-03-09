from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            assert fast is not None
            fast = fast.next

        while fast:
            assert slow is not None
            fast = fast.next
            slow = slow.next

        assert slow is not None and slow.next is not None
        slow.next = slow.next.next

        return dummy.next
