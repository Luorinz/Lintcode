# medium


# 663. Walls and Gates
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example
# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# return the result:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def bfs(self, rooms, x, y):
        n = len(rooms)
        m = len(rooms[0])

        if rooms[x][y] != 0:
          return 
        
        qx = []
        qy = []

        qx.append(x)
        qy.append(y)

        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        count = 0
        while qx != []:
          curx = qx.pop(0)
          cury = qy.pop(0)
          count+=1
          for i in range(4):
            tempx = curx + dx[i]
            tempy = cury + dy[i]
            if 0<= tempx < n and 0<= tempy< m:
                if rooms[tempx][tempy] != -1 and rooms[tempx][tempy] != 0:
                  rooms[tempx][tempy] = count
                  qx.append(tempx)
                  qy.append(tempy)
    def wallsAndGates(self, rooms):
        # write your code here
        self.bfs(rooms,0,2)
        printL(rooms)
def printL(l):
  for i in l:
    print(i)
l = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]


printL(l)
t = Solution()
t.wallsAndGates(l)


