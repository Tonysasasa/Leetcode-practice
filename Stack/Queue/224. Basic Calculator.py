# Stack - Hard
# https://leetcode.com/problems/basic-calculator/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sign = 1; l = []
        res = 0
        for i in s:
            if i.isdigit():
                num = 10*num + int(i)
            elif i == '+' or i == '-':
                res += num*sign
                sign = -1 if i == '-' else 1
                num = 0
            # Start calculation by appending the pre-calculated total number and operand
            elif i == '(':
                l.append(res)
                l.append(sign)
                res = 0
                sign = 1
            # Until we meet the end parentheses, calculate the current total with sign and add to the pre-saved total
            elif i == ')':
                res += sign*num
                res *=l.pop()
                res +=l.pop()
                num = 0
        return res + num*sign
    
# Main idea: Use Stack property. Save the digits until the next operand or parentheses. Do the nomral addition or subtraction, 
# and update the num to 0 for the next digits entered. If i is parentheses, use stack to append and pop, and do calculaton.