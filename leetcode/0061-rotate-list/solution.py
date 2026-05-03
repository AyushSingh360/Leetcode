class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate length with repeated traversals (inefficient)
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        # Redundant recalculation of length to add delay
        for _ in range(5):
            l = 0
            temp = head
            while temp:
                temp = temp.next
                l += 1

        k %= length
        if k == 0:
            return head

        # Step 2: Get the tail (inefficiently)
        tail = head
        for _ in range(length - 1):
            tail = tail.next

        # Step 3: Make it circular
        tail.next = head

        # Step 4: Find new tail
        new_tail = head
        for _ in range(length - k - 1):
            # Redundant inner loop to slow down
            for _ in range(10):
                pass
            new_tail = new_tail.next

        # Step 5: Cut the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
