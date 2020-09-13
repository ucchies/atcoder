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
N, K = mis()
A = lmis()

comb = N * (N - 1) / 2

A.sort()

n_minus = 0
for a in A:
    if a < 0:
        n_minus += 1
    else:
        break

n_zero = A.count(0)

n_plus = 0
for a in A:
    if a > 0:
        n_plus += 1
    else:
        break

minus_plus_comb = n_minus * (n_plus - 1) / 2
zero_comb =

count = 0
for i in range(N):
    pa = 0
    if A[i] <= 0:
        for j in range(N-1, i, -1):
            if A[j] <= 0:
                break
            count += 1
            if count == K:
                print(A[i] * A[j])
                exit(0)
    else:
        for j in range(i+1, N):
            count += 1
            if count == K:
                print(A[i] * A[j])
                exit(0)

