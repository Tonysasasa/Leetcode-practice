# Stack - Medium
# https://leetcode.com/problems/basic-calculator-ii/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Get rid of empty space
        s = s.replace(" ", "")
        s += '+'
        op = '+'
        l = []; cur = 0
        for i in s:
            if i.isdigit():
                cur = cur*10 + int(i)
            else:
                if op == "+":
                    l.append(cur)
                elif op == "-":
                    l.append(-cur)
                elif op == "*":
                    l.append(cur*l.pop())
                elif op == "/":
                    l.append(int(float(l.pop())/cur))
                cur = 0
                op = i               
        return sum(l) 
    
# Main idea: Use Stack property. The key point is to set a variable op to point to the 'last_operand'. If we use i (operand) 
# directly, then it will take the last two numbers from the stack. ("3+2*2" becomes to take 3*2 first)