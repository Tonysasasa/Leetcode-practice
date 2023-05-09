# LinkedList - Easy
# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Approach 1: two-pointer method. Find the mid of the LinkedList, then reverse the remaining part, finally check if two 
        # parts are equal or not. Need to set a temp pointer for reverse 

        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Found the mid of the LinkerList
        prev = slow
        slow = slow.next
        prev.next = None
        # Reverse the back part of the LinkedList
        while slow:
            slow.next= prev
            prev = slow
            slow = slow.next
        # set fast to head, slow to the previous saved slow head, then compare the two parts 
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
        
        
        # Approach 2: Convert the LinkedList to a List and check if it is palindrome
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return l  == l[::-1]