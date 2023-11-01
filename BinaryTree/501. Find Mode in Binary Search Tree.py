# Tree - Easy
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=daily-question&envId=2023-11-01

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        if not root: return root
        from collections import deque
        que = deque([root])
        d = defaultdict(int)
        ans = []
        while que:            
            for i in range(len(que)):
                cur = que.popleft()
                d[cur.val] += 1
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        freq = max(d.values())
        for k,v in d.items():
            if d[k] == freq:
                ans.append(k)
        return ans
    
# BFS search. Use a default dictionary to store the frequency of the number appeared. Append all modes to the list. 