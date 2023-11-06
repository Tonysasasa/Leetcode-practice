# Graph - medium
# https://leetcode.com/problems/number-of-provinces

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        from collections import deque
        res = 0
        seen = set()
        for i in range (len(isConnected)):
            if i not in seen:
                res+=1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    seen.add(i)
                    for j,v in enumerate(isConnected[cur]):
                        if v ==1 and j not in seen:
                            q.append(j)
                            seen.add(j)
        return res



        d = collections.defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i !=j and isConnected[i][j] == 1:
                    d[i].append(j)
        seen = set()
        cnt = 0
        def dfs(node):
            if node in seen: return
            seen.add(node)
            for nei in d[node]:
                dfs(nei)
            return True
  
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)  
                cnt+=1
        return cnt

# Use DFS&BFS. Since it only need to return the number of connected provinces, we can treat the starting index to 0.
