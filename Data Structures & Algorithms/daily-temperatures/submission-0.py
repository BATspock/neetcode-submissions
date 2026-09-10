class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        res = []

        for i in range(len(temperatures)-1, -1, -1):
            if not monotonic_stack:
                monotonic_stack.append((temperatures[i], i))
                res.append(0)

            elif temperatures[i] < monotonic_stack[-1][0]:
                res.append(monotonic_stack[-1][1] - i)
                monotonic_stack.append((temperatures[i], i))
           
            elif temperatures[i] >= monotonic_stack[-1][0]:
                    while monotonic_stack and monotonic_stack[-1][0] <= temperatures[i]:
                        monotonic_stack.pop()
                    if monotonic_stack:
                        res.append(monotonic_stack[-1][1] - i)
                    else:
                        res.append(0)
                    monotonic_stack.append((temperatures[i], i))
                    
        
        return res[::-1]

        # [(40, 6), (38, 1), (30, 0) ], [0, 0, 1, 2, 1, 4, 1 ]