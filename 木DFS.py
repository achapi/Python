def dfs(v,c):
  global d
  d.append(v)
  for i in g[v]:
    if i==y:
      d.append(i)
      exit(print(*d))
    if i!=c:dfs(i,v)
  d.pop()
d=[]
dfs(0,-1)
