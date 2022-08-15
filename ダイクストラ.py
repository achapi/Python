import heapq
def dijkstra(s):
    d = [float('inf')]*n
    d[s] = 0
    used = [False]*n
    used[s] = True
    que = []
    for e in g[s]:
        heapq.heappush(que, e)
    while que:
        u, v = heapq.heappop(que)
        if used[v]:
            continue
        d[v] = u
        used[v] = True
        for e in g[v]:
            if not used[e[1]]:
                heapq.heappush(que, [e[0] + d[v], e[1]])
    return d
  #https://qiita.com/takayg1/items/eed6d84506cc3941ae8d
