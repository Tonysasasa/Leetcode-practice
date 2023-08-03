# Tree - Easy
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
        # l = []
        # def inorder(root,l):
        #     if root: 
        #         inorder(root.left,l)
        #         l.append(root.val)
        #         inorder(root.right,l)           
        # inorder(root,l)
        # return l

        if not root: return []
        stack = []; res = []; cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:               
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
    
# Main idea: Recursion - Continously traverse the binary tree from left to right. Defining the recursion parameters, 
# ending condition and traverse logic.
# - Stack - Note: idea is different with Preorder search. It starts with continously traversing to the left-most element,
# then save the value and pop the stack to go to the right branch. 