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
        # l = []
        # def postorder(root,l):
        #     if root:
        #         postorder(root.left,l)
        #         postorder(root.right,l)
        #         l.append(root.val)
        # postorder(root,l)
        # return l
        if not root: return []
        res = []; stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]
    
# Main idea: Recursion - Continously traverse the binary tree from left to right before getting the root.val. 
# Defining the recursion parameters, ending condition and traverse logic.
# - stack - Same idea with Preorder traversal byusing stack method. Needs to change the order from
# mid-left-right to mid-right-left then inverse the order to left-right-mid