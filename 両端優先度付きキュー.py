class PriorityDeque:
    def __init__(self, a):
        self.d = a
        self.make_heap()
    def __len__(self):
        return len(self.d)
    def push(self,x):
        k = len(self.d)
        self.d.append(x)
        self.up(k)
    def pop_min(self):
        r = self.get_min()
        if len(self.d) < 3 :
            self.d.pop()
        else:
            self.d[1], self.d[-1] = self.d[-1], self.d[1]
            self.d.pop()
            k = self.down(1)
            self.up(k)
        return r
    def pop_max(self):
        r = self.get_max()
        if len(self.d) < 2:
            self.d.pop()
        else:
            self.d[0], self.d[-1] = self.d[-1], self.d[0]
            self.d.pop()
            k = self.down(0)
            self.up(k)
        return r
    def get_min(self):
        return self.d[0] if len(self.d) < 2 else self.d[1]
    def get_max(self):
        return self.d[0]
    def make_heap(self):
        for i in range(len(self.d))[::-1]:
            if i & 1 and self.d[i-1] < self.d[i]:
                self.d[i-1], self.d[i] = self.d[i], self.d[i-1]
            k = self.down(i)
            self.up(k, i)
    def parent(self, k):
        return ((k>>1)-1)&~1
    def down(self, k):
        n = len(self.d)
        if k & 1 :
            while (2*k+1 < n):
                c = 2*k+3
                if n <= c or self.d[c-2] < self.d[c]:
                    c -= 2
                if c < n and self.d[c] < self.d[k]:
                    self.d[k], self.d[c] = self.d[c], self.d[k]
                    k = c
                else:break
        else:
            while 2*k+2 < n:
                c = 2*k+4
                if n <= c or self.d[c] < self.d[c-2]:
                    c -= 2
                if c < n and self.d[k] < self.d[c]:
                    self.d[k], self.d[c] = self.d[c], self.d[k]
                    k = c
                else:break
        return k
    def up(self, k, root=1):
        if (k|1) < len(self.d) and self.d[k&~1] < self.d[k|1]:
            self.d[k&~1], self.d[k|1] = self.d[k|1], self.d[k&~1]
            k ^= 1
        
        p=self.parent(k)
        while root < k and self.d[p] < self.d[k]:
            self.d[p], self.d[k] = self.d[k], self.d[p]
            k = p
            p=self.parent(k)
        p=self.parent(k)|1
        while root < k and self.d[k] < self.d[p]:
            self.d[p], self.d[k] = self.d[k], self.d[p]
            k = p
            p=self.parent(k)|1
        return k
"""
s=PriorityDeque(list)
s.pop_max() 最小値を削除して返す・O(1)
s.get_max() 最小値を返す・・・・・O(log N)
s.pop_max() 最大値を削除して返す・O(1)
s.get_max() 最大値を返す・・・・・O(log N)
"""
