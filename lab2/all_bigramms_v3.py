#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import itertools

# pattern to return words greater 4 chars length
pattern = ur'(?u)[a-zA-Zа-яА-Я_]{4,}'

for line in sys.stdin:
    query = line.split('\t')[1].decode('utf-8')

    # all digramm combinations with a word length greater than 4 chars
    for bigramm in itertools.combinations(re.findall(pattern, query), 2):
        print(' '.join(bigramm).encode('utf-8'))

