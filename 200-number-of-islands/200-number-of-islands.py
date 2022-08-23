class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def bfs(x, y):
            queue = deque()
            queue.append((x,y))
            grid[x][y] = '0'
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] == '0':
                        continue
                    if grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        queue.append((nx,ny))



        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)
                    count += 1
        return count