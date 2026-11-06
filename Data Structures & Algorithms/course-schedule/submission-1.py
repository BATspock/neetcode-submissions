from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        indegree = [0]*numCourses

        # create adj List
        for (c1, c2) in prerequisites:
            adj_list[c2].append(c1)
            indegree[c1]+=1

        queue = deque()

        for i, deg in enumerate(indegree):
            if deg == 0:
                queue.append(i)

        courses = 0

        while queue:
            node = queue.popleft()
            courses+=1
            for course in adj_list[node]:
                indegree[course]-=1

                if indegree[course] == 0:
                    queue.append(course)

        return numCourses == courses

