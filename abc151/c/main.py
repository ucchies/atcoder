# python3
# -*- coding: utf-8 -*-
# featuring...
# https://atcoder.jp/contests/abc151/submissions/9451830
import sys
import math
from math import gcd
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
n, m = mis()

ac = 0
pe = 0
ac_flag = [0] * 10000
wa_count = [0] * 10000
for _ in range(m):
    p, s = input.split()
    if s == 'WA' and ac_flag[int(p)] == 0:
        wa_count[int(p)] += 1
    else:
        ac_flag[int(p)] = 1
        pe += wa_count[int(p)]



print(ac + " " + pe)