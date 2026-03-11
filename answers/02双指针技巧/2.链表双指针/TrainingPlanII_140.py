from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for _ in range(cnt):
            assert fast is not None
            fast = fast.next

        while fast:
            assert slow is not None
            fast = fast.next
            slow = slow.next

        return slow # LeetCode上提供的return签名为ListNode类型，而解析中要求返回int类型，自行区分即可
