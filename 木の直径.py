from collections import deque
import sys
readline = sys.stdin.readline
N = int(readline())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, readline().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    d = max(dist)
    return dist.index(d), d
u, _ = bfs(0)
v, d = bfs(u)
#dが木の直径
#print(d)
