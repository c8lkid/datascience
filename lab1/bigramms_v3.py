#!/usr/bin/env python

import sys

bigramm = {}

for line in sys.stdin:
    query = line.split('\t')[1]
    if len(query.split(' ')) > 1:

