def validate(n):
    return 

def binarysearch(a):
    left = 1
    right = 10 ** 9
    r=0
    while left <= right:
        mid = (left+right) // 2
        if validate(mid):
            r = mid
            left = mid + 1
        else:
            right = mid -1
    return r