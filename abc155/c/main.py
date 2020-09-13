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


# main
N = ii()
slist = {}
maxvalue = 0

for _ in range(N):
    S = input()
    try:
        slist[S] += 1
    except KeyError:
        slist[S] = 1

    if maxvalue < slist[S]:
        maxvalue = slist[S]

maxs = []
for s in slist:
    if slist[s] == maxvalue:
        maxs.append(s)


for s in sorted(maxs):
    print(s)

