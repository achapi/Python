d=[i for i in range(n) if root[i]==1]
while d:
  v=d.pop()
  root[v]-=1
  for i in g[v]:
    root[i]-=1
    if root[i]==1:d.append(i)
roop=set(i for i in range(n) if root[i]==2)
root[i]:頂点iの次数の個数
#N頂点N辺の閉路を探す
#roopに閉路がset型で入る
