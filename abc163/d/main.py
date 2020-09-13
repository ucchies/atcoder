# python3
# -*- coding: utf-8 -*-
import sys
import math
import bisect
from fractions import gcd
from itertools import count, permutations
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
n, k = mis()

if n+1 == k:
    print('1')
    exit(0)

allsum = (n+1)*n//2
sums = [-1] * (n+1)
comb = 0

sums[0] = 0

for i in range(1, n+1):
    sums[i] = sums[i-1] + i

for i in range(k, n+2):
    comb += (allsum - sums[(n-i if (n-i>=0) else 0)]) - (sums[i-1] - 1)

print(comb)
