class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len (isWater), len(isWater[0])
        q = deque() #3 (r, c)
        res = [[-1] * COLS for _ in range(ROWS)] # -1 = unvisited
        # Enqueue all water cells
        for r in range (ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0
        # BFS
        while q:
            r, c = q.popleft()
            h = res[r][c]
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or
                    nr == ROWS or nc == COLS or
                    res[nr][nc] != -1
                ):
                    continue
                q.append((nr, nc))
                res[nr] [nc] = h + 1
        return res