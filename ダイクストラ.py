import heapq
def dijkstra(s):
    # 始点から各頂点への最短距離
    d = [float('inf')]*n
    d[s] = 0
    # 各頂点が訪問済みかどうか
    used = [False]*n
    used[s] = True
    # 仮の距離を記録するヒープ
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
