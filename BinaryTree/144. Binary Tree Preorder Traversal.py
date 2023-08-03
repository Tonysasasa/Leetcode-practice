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
        # l = []
        # def preorder(root,l):
        #     if root:
        #         l.append(root.val)
        #         preorder(root.left,l)
        #         preorder(root.right,l)
        # preorder(root,l)
        # return l

        if root is None: return []
        stack = []; res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    
# Main idea: Recursion - Continously traverse the binary tree from left to right after getting the root.val. 
# Defining the recursion parameters, ending condition and traverse logic.
# - Stack - use a stack to replace recursion algorithm. Store the current root if it is not none. Save the 
# root.val into a res array, and then point to the right and left element. Need to store right first then left. 