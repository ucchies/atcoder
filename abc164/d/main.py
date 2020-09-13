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
s = input()

c = 0

for i in range(len(s)-3):
    for j in range(i+4, len(s)+1):
        if int(s[i:j]) % 2019 == 0:
            c += 1

print(c)