# Tree - Easy
# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def helper(leftN,rightN):
        #     if not leftN and not rightN: return True
        #     if (not leftN and rightN) or (leftN and not rightN): return False
        #     if leftN.val != rightN.val: return False
        #     return helper(leftN.left, rightN.right) and helper(leftN.right, rightN.left)
        # return helper(root.left, root.right)

        L = [root]; R =[root]
        while L or R:
            l = L.pop()
            r = R.pop()
            if not l and not r: continue
            elif not l and r or l and not r: return False
            elif l.val != r.val: return False           
            L.append(l.right)
            R.append(r.left)
            L.append(l.left)
            R.append(r.right)
        return True
    
# Main idea: DFS and BFS. DFS: defining the condition to return True/False, then recursively do left branch and right branch
# BFS: use two stacks to store left branch and right branch. 