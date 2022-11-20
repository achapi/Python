#アルファベット
al=[chr(ord('a') + i) for i in range(26)]

#周辺埋め
h,w=map(int, input().split())
m=["."*(w+2)]+["."+input()+"." for i in range(h)]+["."*(w+2)]

#必須再帰関数
import sys
sys.setrecursionlimit(202020)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

#python用メモ化再起
from functools import lru_cache
@lru_cache
