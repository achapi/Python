from collections import deque
dist = [[-1]*w for i in range(h)]
d = 0
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
while S:
    while S:
        x,y = S.popleft()
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if not 0 <= nx < h or not 0 <= ny < w:continue
            if s[nx][ny]=="#":c=1
            else:c=0
            if d+c < dist[nx][ny]:
                dist[nx][ny] = d+c
                if c:
                    T.append((nx,ny))
                else:
                    S.append((nx,ny))
    S, T = T, S
    d += 1
