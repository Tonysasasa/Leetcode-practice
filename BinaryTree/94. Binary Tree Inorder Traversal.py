# Array - Easy
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        def inorder(root,l):
            if root: 
                inorder(root.left,l)
                l.append(root.val)
                inorder(root.right,l)           
        inorder(root,l)
        return l
    
# Main idea: Recursion - Continously traverse the binary tree from left to right. Defining the recursion parameters, 
# ending condition and traverse logic.