# LinkedList - Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        s = head; f = head
        for _ in range(n): f = f.next
        if not f: return head.next
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head


# Main idea: use two-pointer approach. Let f (fast pointer) move n steps forward at first. Then move s (slow pointer) with f until 
# f.next is null. 