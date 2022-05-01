#アルファベット
al=[chr(ord('a') + i) for i in range(26)]

#周辺埋め
h,w=map(int, input().split())
m=["."*(w+2)]+["."+input()+"." for i in range(h)]+["."*(w+2)]

#必須再帰関数
import sys
sys.setrecursionlimit(10000)