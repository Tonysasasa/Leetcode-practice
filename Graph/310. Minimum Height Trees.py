# Graph - medium
# https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if edges == []: return [0]
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        
        res = []
        for k,v in d.items():
            if len(v) == 1:
                res.append(k)
        
        while n >2:
            n -= len(res)
            temp = []
            for node in res:
                for nei in d[node]:
                    d[nei].remove(node)
                    if len(d[nei]) == 1:
                        temp.append(nei)
            res = temp
        return res

# Use topological sort. Create the graph for each node with neighbors (with undirect path). If the size of the node's neighbor
# is 1, then it is a leaf node. Find and cut the leave node first, and remove it in the related root node. 
# Reset the root node. 