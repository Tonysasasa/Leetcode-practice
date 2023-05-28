# Stack - Easy
# https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = []; l2 = []

        for i in s:
            if l1 and i == '#': l1.pop()
            elif i != '#': l1.append(i)

        for j in t:
            if l2 and j == '#': l2.pop()
            elif j != '#': l2.append(j)

        return l1 == l2


# Main idea: Use Stack property. Traverse two Strings and append into the lists. If the element is "#", then pop the item