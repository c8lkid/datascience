#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cat lab1_kassa.csv | python by_email_v2.py | sort -k3,3 -t$'\t' | python top_film_v2.py

import sys

for line in sys.stdin:
    try:
        film, people, email = map(lambda x: x.strip('"\n\r'), line.split(';'))
    except ValueError:
        continue
    print('{0}\t{1}\t{2}'.format(film, people, email))
