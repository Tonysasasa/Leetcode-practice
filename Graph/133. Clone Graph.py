# Graph - medium
# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """      
        # DFS recursive traversal - if the node entered is not in dictionary, add it as our start point. Then, traverse the neighbors.
        # Do repeat the same to neighbors. Need to add a set to mitigate into the infinite loop search
        from collections import deque
        if not node: return
         # map original nodes to their clones
        d = {}
        q = deque([node])
        seen = set()

        def dfs(node,d):
            if node in seen: return 
            seen.add(node)
            if node not in d:
                d[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                d[node].neighbors.append(d[nei])
                dfs(nei,d)

        dfs(node,d)
        return d[node]
        
        # # BFS iterative traversal - use deque to popleft. Same idea to DFS
        # while q:
        #     currNode = q.popleft()
        #     for nei in currNode.neighbors:
        #         if nei not in d:
        #             # store copy of the neighboring node
        #             d[nei] = Node(nei.val)
        #             q.append(nei)
        #         # connect the node copy at hand to its neighboring nodes (also copies) -------- [1]
        #         d[currNode].neighbors.append(d[nei])
        # # return copy of the starting node ------- [2]
        # return d[node]