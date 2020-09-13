# python3
# -*- coding: utf-8 -*-
import sys
import math
from fractions import gcd
from itertools import count, permutations, combinations, combinations_with_replacement, product
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
lmtx = lambda h: [list(map(int, lmis())) for _ in range(h)]
sys.setrecursionlimit(1000000000)


def lcm(a, b):
    return (a * b) // gcd(a, b)


# main
k = ii()
d = deque()

for i in range(1, 10):
    d.append(i)

x = 1

for _ in range(k):
    x = int(d.popleft())

    if x % 10 != 0:
        d.append(10 * x + x % 10 - 1)

    d.append(10 * x + x % 10)

    if x % 10 != 9:
        d.append(10 * x + x % 10 + 1)

print(x)
