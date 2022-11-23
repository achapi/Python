import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()
 
    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1
 
    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            return
        else:
            self.d[x]-=1
 
        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break
 
    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False
 
    def get_min(self):
        return self.h[0]
