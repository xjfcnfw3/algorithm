from collections import deque
import sys

input = sys.stdin.readline
s = int(input())
visited = [0] * (s + 1)
MAX = 3000

def bfs():
    queue = deque(1)
    visited[1] =