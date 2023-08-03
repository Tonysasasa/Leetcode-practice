# Tree - Easy
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        def preorder(root,l):
            if root:
                l.append(root.val)
                preorder(root.left,l)
                preorder(root.right,l)
        preorder(root,l)
        return l
    
# Main idea: Recursion - Continously traverse the binary tree from left to right after getting the root.val. 
# Defining the recursion parameters, ending condition and traverse logic.