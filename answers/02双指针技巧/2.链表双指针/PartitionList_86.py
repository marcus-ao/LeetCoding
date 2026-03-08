from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left_tail = left_dummy
        right_tail = right_dummy

        cur = head
        while cur:
            next_node = cur.next

            cur.next = None

            if cur.val < x:
                left_tail.next = cur
                left_tail = left_tail.next
            else:
                right_tail.next = cur
                right_tail = right_tail.next

            cur = next_node

        left_tail.next = right_dummy.next

        return left_dummy.next
