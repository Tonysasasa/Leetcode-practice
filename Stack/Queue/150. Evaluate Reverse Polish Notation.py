# Stack - Medium
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        l = []
        for i in tokens:         
            if i == '+':
                cur = l.pop() + l.pop()
                l.append(cur)       
            elif i == '-':
                a = l.pop()
                b = l.pop()
                cur = b - a
                l.append(cur)
            elif i == '*':
                cur = l.pop() * l.pop()
                l.append(cur)   
            elif i == '/':
                a = l.pop()
                b = l.pop()
                cur = int (float(b) / a)
                l.append(cur)      
            else:
                 l.append(int(i))
        return l[0]
    
# Main idea: Use Stack property (LIFO). Save numbers into stack. Do operations by pop the last numbers from the stack.