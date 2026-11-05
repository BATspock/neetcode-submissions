from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len (board) , len (board[0])
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        queue = deque()

        for r in range(rows):
            if board[r][0] == 'O':
                queue.append((r,0))
            if board[r][cols - 1] == 'O':
                queue.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[rows - 1][c] == 'O':
                queue.append((rows - 1, c))               
        print(queue)
        
        def isValid(r, c):
            return (0 <= r < rows) and (0 <= c < cols)

        def caputure():

            while queue:
                r, c = queue.popleft()

                if board[r][c] == 'O':
                    board[r][c] = 'T'

                for dr in dirs:
                    nr, nc = r + dr[0], c + dr[1]

                    if isValid(nr, nc) and \
                        board[nr][nc] == 'O':

                        board[nr][nc] = 'T'
                        queue.append((nr, nc))

        caputure()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] ='X'
