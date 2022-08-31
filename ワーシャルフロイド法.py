def Warshall(G,N):
  #G[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if G[i][k]!= and G[k][j]!=INF:G[i][j] = min(G[i][j], G[i][k] + G[k][j])
  return G
