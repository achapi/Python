def cmb(n,r,p):
    if(r<0)or(n<r):return 0
    return fact[n]*factinv[min(r,n-r)]*factinv[n-min(r,n-r)]%p
fact,factinv,inv=[1,1],[1,1],[0,1]
for i in range(2,10**6):
    fact.append((fact[-1]*i)%mod)
    inv.append((-inv[mod % i]*(mod//i))%mod)
    factinv.append((factinv[-1]*inv[-1])%mod)
