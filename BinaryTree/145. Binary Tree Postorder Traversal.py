# Tree - Easy
# https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        def postorder(root,l):
            if root:
                postorder(root.left,l)
                postorder(root.right,l)
                l.append(root.val)
        postorder(root,l)
        return l
    
# Main idea: Recursion - Continously traverse the binary tree from left to right before getting the root.val. 
# Defining the recursion parameters, ending condition and traverse logic.