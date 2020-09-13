# python3
# -*- coding: utf-8 -*-
import sys
import math
#from math import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
sys.setrecursionlimit(1000000000)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def ex(s):
    n = int(s)
    nn = (n+1) * (n/2)
    return nn / n

# main
N, K = mis()
exs = list(map(ex, input().split()))

if N == K:
    print(sum(exs))
    exit(0)

ex_max = 0

for i in range(K):
    ex_max += exs[i]

left = 0
ex_temp = ex_max
for i in range(K, N):
    ex_temp = ex_temp - exs[left] + exs[i]
    left += 1
    if ex_max < ex_temp:
        ex_max = ex_temp

print('{:.7f}'.format(ex_max))
