from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 法1：计算链表长度后再进行断链

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length

        if k == 0:
            return head
        
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None
        tail.next = head

        return new_head

# 法2：成环后再进行断开

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k % length
        if k == 0:
            return head

        tail.next = head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        return new_head
