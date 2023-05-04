class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2**31 - 1
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = []

        # Add all gates to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        # BFS
        while q:
            x, y = q.pop(0)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    q.append((nx, ny))

        # Set unreachable rooms to INF
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == INF:
                    rooms[i][j] = INF
