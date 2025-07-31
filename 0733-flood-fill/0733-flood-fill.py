from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        old_color = image[sr][sc]

        if old_color == color:
            return image

        q = deque([[sr, sc]])
        vis[sr][sc] = 1
        image[sr][sc] = color

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and image[nr][nc] == old_color:
                    q.append([nr, nc])
                    vis[nr][nc] = 1
                    image[nr][nc] = color

        return image
