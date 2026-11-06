from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        outdegree = [0]*numCourses

        # create adj List
        for (c1, c2) in prerequisites:
            adj_list[c2].append(c1)
            outdegree[c1]+=1

        queue = deque()

        for i, deg in enumerate(outdegree):
            if deg == 0:
                queue.append(i)

        courses = 0

        while queue:
            node = queue.popleft()
            courses+=1
            for course in adj_list[node]:
                outdegree[course]-=1

                if outdegree[course] == 0:
                    queue.append(course)

        return numCourses == courses

