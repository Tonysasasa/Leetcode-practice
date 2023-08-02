# LinkedList - Medium
# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0,None); head = dummy
        h1 = l1; h2 = l2; cur = 0; carry = 0
        while h1 or h2 or carry != 0:
            digit1 = h1.val if h1 is not None else 0
            digit2 = h2.val if h2 is not None else 0

            cur = digit1 + digit2 + carry
            carry = 0
            if cur >= 10:
                carry = 1
                cur = cur % 10
            new = ListNode(cur,None)
            head.next = new
            head = head.next
            h1 = h1.next if h1 is not None else None
            h2 = h2.next if h2 is not None else None

        result = dummy.next
        dummy.next = None
        return result
        
        # dummy = ListNode()
        # tail = dummy
        # s1 =[]; s2 = []
        # h1 = l1; h2 = l2
        # while h1:
        #     s1.append(h1.val)
        #     h1 = h1.next
        # while h2:
        #     s2.append(h2.val)
        #     h2 = h2.next
        # s1 = s1[::-1]; s2 = s2[::-1]
        # num = 0; num1 = 0
        # for current_digit in s1:
        #     num1 = num1*10 + current_digit
        # num2 = 0
        # for current_digit in s2:
        #     num2 = num2*10 + current_digit
        # num = num1 + num2
        # res = [int(x) for x in str(num)]; res = res[::-1]
        
        # for i in res:
        #     tail.next = ListNode(i)
        #     tail = tail.next
        # return dummy.next

# Main idea: Either using two arrays to store two linked list values, or directly calculate two linked list and save the result
# into a new linked list