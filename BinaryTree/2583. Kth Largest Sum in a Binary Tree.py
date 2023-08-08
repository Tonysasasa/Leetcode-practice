# Tree - Medium
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    import collections
    from collections import deque
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        from collections import deque
        if not root: return 0
        queue = collections.deque([root])
        value = 0; l = []
        while queue:            
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                value = value + cur.val
            l.append(value)
            value = 0
        if len(l) < k: return -1  
        l.sort()
        return l[-k]
    
# Main idea: use BFS to traverse the binary tree by level. Store the sum of each level into a list