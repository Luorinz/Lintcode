# medium 

# 477. Surrounded Regions
# Given a 2D board con477. Surrounded Regionstaining 'X' and 'O', capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

# Example
# X X X X
# X O O X
# X X O X
# X O X X
# After capture all regions surrounded by 'X', the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def bfs(self,board,sx,sy):
        if board[sx][sy] != 'O':
            return
        
        n = len(board)
        m = len(board[0])

        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        qx = []
        qy = []

        qx.append(sx)
        qy.append(sy)

        board[sx][sy] = 'W'

        while qx != []:
            cx = qx.pop(0)  
            cy = qx.pop(0)

            for i in range(4):·
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == 'O':
                    board[nx][ny] = 'W'
                    qx.append(nx)
                    qy.append(ny)


    def surroundedRegions(self, board):
        # write your code here
        if not board:
            return
        n = len(board)
        m = len(board[0])

        for i in range(n):
            self.bfs(board,i,0)
            self.bfs(board,i,m-1)

        for j in range(m):
            self.bfs(board,0,j)
            self.bfs(board,n-1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'W':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        