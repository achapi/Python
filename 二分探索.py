def validate(x):
  return 

def binarysearch(left=1,right=10**18,r=0):
    while left<=right:
        mid=(left+right)//2
        if validate(mid):r=mid;left=mid+1
        else:right=mid-1
    return r
