class DSU:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.parents[pv] = pu
        self.size[pu] += self.size[pv]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        dsu = DSU(n)

        for e1, e2 in edges:
            if not dsu.union(e1, e2):
                return [e1, e2]