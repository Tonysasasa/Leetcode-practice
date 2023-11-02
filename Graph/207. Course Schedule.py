# Graph - medium
# https://leetcode.com/problems/course-schedule

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque

        g = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            g[prerequisite[1]].append(prerequisite[0])

        indegree = [0] * numCourses
        for dependencies in g:
            for dependency in dependencies:
                indegree[dependency] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0  
        while queue:
            node = queue.popleft()
            count += 1

            for dependency in g[node]:
                indegree[dependency] -= 1
                if indegree[dependency] == 0:
                    queue.append(dependency)

        return count == numCourses

# BFS (Topological sorting algorithm) - Create an adjacent list first. Create an indgree list for num of prerequiste courses 
# of the current course. Then find the course with no prerequiste. Loop the queue and return if the count == numCourses

        def dfs(i,mp,visit):
            if i in visit: return False
            if mp[i] == []: return True
            visit.add(i)

            for req in mp[i]:
                if not dfs(req,mp,visit): return False
            visit.remove(i)
            mp[i] = []
            return True

        mp=defaultdict(list)
        for a,b in prerequisites:
            mp[a]+=[b]
        visit = set()
        for i in range(numCourses):
            if dfs(i,mp,visit) == False: return False
        return True

# DFS - Make a dictionary to perform the adjacent list of the current course. Create a visited list if we see the current one in
# the list and return False. Recursively traverse the courses in the adjacent list