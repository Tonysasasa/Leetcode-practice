# LinkedList - Medium
# https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head

        # Set two pointer s and f. Take f move ahead to the last element
        s = head; cnt = 1; f = head
        while f.next:
            f = f.next
            cnt += 1
        k = k % cnt
        
        if k == 0: return head

        # Then take s to move the cnt-k element 
        for _ in range(1, cnt-k):
            s = s.next
        
        # f is currently the last element of the linked list; then its next is pointed to the head element
        f.next= head
        # Set new head to the s.next, which is the staring point of the new linked list
        head = s.next
        # Don't forget to end up with a None to set to the original s.next
        s.next = None     
        return head
    
# Main idea: use two-pointer approach. Must notice if the length of the linked list is greater than the k, then it should
# take count of len - k. 