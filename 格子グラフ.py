from collections import deque
def bfs(S, H, W, r0, c0):
    dist = [[-1]*W for i in range(H)]
    que = deque([(r0, c0)])
    dist[r0][c0] = 0
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr = r + dr; nc = c + dc
            if not 0 <= nr < H or not 0 <= nc < W or S[nr][nc] == '#':
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur+1
                que.append((nr, nc))
    return dist
dist = bfs(s,h,w,0,0)
