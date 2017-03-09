#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Context_data.txt | python proceeds_v1.py 2011-03-01 2018-03-04 | sort -k1,1 | python projects_v1.py Context_dict.txt

import sys
from datetime import datetime

if (len(sys.argv) != 3):
    print sys.argv[0] + ' YYYY-MM-DD YYYY-MM-DD'
    sys.exit(1)

# convert date format YYYY-mm-dd to dd.mm.YYYY
date_from_str = (datetime.strptime(sys.argv[1], '%Y-%m-%d')).strftime('%d.%m.%Y')
date_to_str = (datetime.strptime(sys.argv[2], '%Y-%m-%d')).strftime('%d.%m.%Y')

# convert date to obj
date_from_obj = (datetime.strptime(date_from_str, '%d.%m.%Y'))
date_to_obj = (datetime.strptime(date_to_str, '%d.%m.%Y'))

for line in sys.stdin:
    d, project, proceeds = map(lambda x: x.strip(), line.split('\t'))
    try:
        d = datetime.strptime(d, '%d.%m.%Y')
    except ValueError:
        continue
    if date_from_obj < d < date_to_obj:
        print('{0:<7} {1:>7}'.format(project, proceeds))
