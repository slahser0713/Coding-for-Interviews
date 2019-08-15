class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return
        slow = head
        fast = head
        for _ in range(k-1):
            if fast.next:
                fast = fast.next
            else:
                return
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow