#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

total = 0
i = 0

if (len(sys.argv) < 2):
    print sys.argv[0] + ' filename'
    sys.exit(1)

fb = open(sys.argv[1])

for bigramm in sys.stdin:
    for line in fb:
        if bigramm.strip() in line:
            total += 1
    print('{0} {1}'.format(bigramm.strip(), total))
    total = 0
    fb.seek(0)
fb.close()
