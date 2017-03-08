#!/usr/bin/env python

import sys

d = {}
for line in sys.stdin:
    try:
        film, tickets, hash_sum = line.split(';')
        hash_sum = hash_sum.strip()[1:-1]
        film = film.strip()[1:-1]
        tickets = tickets.strip()[1:-1]
    except ValueError:
        continue
    if not d.has_key(film):
        d[film] = int(tickets)
        continue
    d[film] += int(tickets)

max = 0
tmp = {}
for k, v in d.items():
    if v > max:
        max = v
        tmp = k
print(k)
print(max)
