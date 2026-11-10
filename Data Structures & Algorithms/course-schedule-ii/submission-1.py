from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree  =[0]*numCourses
        adj_list = [[] for _ in range(numCourses)]

        for (c1, c2) in prerequisites:
            adj_list[c1].append(c2)
            indegree[c2]+=1
        
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for n in adj_list[node]:
                indegree[n]-=1
                if indegree[n] == 0:
                    queue.append(n)
        if len(order)!=numCourses:
            return []
        return order[::-1]
        