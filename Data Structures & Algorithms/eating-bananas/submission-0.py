class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force is iterate from 1 to n 
        # check first i where all banans can be eaten in h hour

        # 1 ........... max(piles)

        # do binary searach on the len and
        # check piles[x] for each x//k + x%k <= h

        def check_eat(k):
            time = 0
            for p in piles:
                time+= (p//k + ( p%k!= 0))
            return time

        start, end = 1, max(piles)

        k = 0

        while start <= end:
            k = (start + end) // 2
            
            # k is too slow
            if check_eat(k) > h:
                start = k + 1
            # k works, try smaller k
            else:
                end = k - 1

        return start
            