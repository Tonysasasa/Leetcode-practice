# Stack - Median
# https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = []; s = list(path.split('/'))
        for i in s:
            print(l)
            if l and i == '..':
                l.pop()
            elif i not in [".", "", ".."]:
                l.append(i)
        return "/" + "/".join(l)
    
# Main idea: Use Stack property (LIFO). If the element is "..", pop the valid right element. 