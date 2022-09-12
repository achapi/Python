def dfs(v,c):
  global roop
  if len(roop)!=0:return
  used[v]=True
  q.append(v)
  for i in s[v]:
    if i==c:continue
    if used[i]:
      if len(roop)==0:roop=set(q[q.index(i):])
      flag=False
    dfs(i,v)
  q.pop()
q=[]
roop=[]
used=[False]*n
dfs(0,-1)
#N頂点N辺の閉路を探す
#roopに閉路がset型で入る
