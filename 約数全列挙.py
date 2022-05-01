def div(n):
    i=1
    s=set()
    while i*i<=n:
        s.add(i)
        s.add(n//i)
        i+=1
    return s