# Tree - Easy
# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
       
        # cur1 = p; cur2 = q
        # s = [(cur1,cur2)]
        # while s:
        #     cur1,cur2 = s.pop()
        #     if not cur1 and not cur2: continue
        #     elif not cur1 or not cur2: return False
        #     else:
        #         if cur1.val != cur2.val: return False
        #         s.append([cur1.left,cur2.left])
        #         s.append([cur1.right,cur2.right])
        # return True

# Main idea: BFS and DFS. For DFS: defining the conditions to return True/False, then do the recursion
# For BFS: use stack to store a pair of the nodes in two trees at same leve same time.