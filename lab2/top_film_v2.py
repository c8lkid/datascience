#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cat lab1_kassa.csv | python by_email_v2.py | sort -k3,3 -t$'\t' | python top_film_v2.py

import sys

cur_email = None
maximum = ('Film', 0)
chart = {}

def max_tuple(a, b):
    return max((a, b), key=lambda x: x[1])

for line in sys.stdin:
    film, people, email = map(lambda x: x.strip('"\n\r'), line.split('\t'))

    if email != cur_email and cur_email is not None:
        maximum = max_tuple(
                max(chart.items(), key=lambda x: x[1]),
                maximum
                )
        chart = {}

    chart[film] = chart.get(film, 0) + int(people)
    cur_email = email

print('{0[0]} {0[1]}'.format(maximum))
