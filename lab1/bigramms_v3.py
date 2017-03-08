#!/usr/bin/env python

import sys

bigramms = {}

for line in sys.stdin:

    query = line.split('\t')[1].split(' ')

    if len(query) > 1:
        bigramm_fst = '{0} {1}'.format(' '.join(query[:2]), ' '.join(query[3:]))
        if bigramms.has_key(bigramm_fst):
            bigramms[bigramm_fst] += 1
        else:
            bigramms[bigramm_fst] = 0

    if len(query[1:]) > 1:
        bigramm_snd = '{0}'.format(' '.join(query[1:]))
        if bigramms.has_key(bigramm_snd):
            bigramms[bigramm_snd] += 1
        else:
            bigramms[bigramm_snd] = 0

for k, v in bigramms.items():
    print('{1:>3} {0}'.format(k, v))
