# Tree - Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    import collections
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        # def dfs(node,cnt):
        #     if not node: return cnt
        #     return max (dfs(node.left,cnt+1),dfs(node.right,cnt+1))
        # return dfs(root,0)

        if not root: return 0
        cnt = 0; 
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            cnt +=1
        return cnt
  
# Main idea: DFS and BFS. For BFS: use queue (FIFO) to store nodes. Traverse each level and add cnt by 1.
