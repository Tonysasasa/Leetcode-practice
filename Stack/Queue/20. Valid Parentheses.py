# Array - Easy
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i == '(' or i == '[' or i == '{': l.append(i)
            else:
                # return False if the stack is either empty or all the right parenthases
                if not l: return False

                # Only pop when two parentheses are matched
                if i == ')' and l[-1] == '(': l.pop()
                elif i == ']' and l[-1] == '[': l.pop()
                elif i == '}' and l[-1] == '{': l.pop()
                # return false if it is invalid i.e: (])
                else: return False

        # Return False if stack is not empty at the end after elimination
        return True if not l else False
    

# Main idea: Stack. A typical stack question. The main idea is to treat left parentheses and right parentheses individually by 
# using stack property (LIFO). If the right parentheses is matched with the top of stack element, then pop and move to next.
