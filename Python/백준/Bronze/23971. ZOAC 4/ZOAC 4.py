import sys

H,W,N,M=map(int, sys.stdin.readline().split())
row = (W-1) // (M+1) +1
col = (H-1) // (N+1) +1
print(row*col)