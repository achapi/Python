from bisect import*
def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:return i
    return None
def lt(a, x):
    # x未満
    i = bisect_left(a, x)
    if i:return a[i-1]
    return None
def le(a, x):
    # x以下
    i = bisect_right(a, x)
    if i:return a[i-1]
    return None
def gt(a, x):
    # x超
    i = bisect_right(a, x)
    if i != len(a):return a[i]
    return None
def ge(a, x):
    # x以上
    i = bisect_left(a, x)
    if i != len(a):return a[i]
    return None
