# Tree - Easy
# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        from collections import deque
        if not root: return None
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root
        
        # def dfs(root):
        #     if not root: return root
        #     root.left, root.right = root.right, root.left
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return root

# Main idea: DFS and BFS(level traverse) - just need to swap the node.left and node.right