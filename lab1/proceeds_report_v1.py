#!/usr/bin/env python

import sys
from datetime import datetime

if (len(sys.argv) != 3):
    print sys.argv[0] + ' date_from date_to.'
    sys.exit(1)

# convert date format YYYY-mm-dd to dd.mm.YYYY
date_from_str = (datetime.strptime(sys.argv[1], '%Y-%m-%d')).strftime('%d.%m.%Y')
date_to_str = (datetime.strptime(sys.argv[2], '%Y-%m-%d')).strftime('%d.%m.%Y')

# convert date to obj
date_from_obj = (datetime.strptime(date_from_str, '%d.%m.%Y'))
date_to_obj = (datetime.strptime(date_to_str, '%d.%m.%Y'))

tmp_stdin = []
result = {}

for line in sys.stdin:
    tmp_stdin.append(tuple(line.split()))

# remove header
tmp_stdin.pop(0)

# sort by date
sorted(tmp_stdin, key=lambda x: datetime.strptime(x[0], '%d.%m.%Y'))

# calculate total summ by project id with date condition
for line in tmp_stdin:
    if date_from_obj <= datetime.strptime(line[0], '%d.%m.%Y') <= date_to_obj:
        if line[1] not in result: result[line[1]] = int(line[2])
        result[line[1]] += int(line[2])

# output result
print('Project ID\tSumm')
for key, value in result.items():
    print('{0:>} {1:>11}'.format(key, value))
