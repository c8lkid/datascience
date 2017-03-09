#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Context_data.txt | python proceeds_v1.py 2011-03-01 2018-03-04 | sort -k1,1 | python projects_v1.py Context_dict.txt

import sys

cur_project = None
total = 0

if (len(sys.argv) < 2):
    print sys.argv[0] + ' filename'
    sys.exit(1)

projects = {}

# dict with project ids
for line in open(sys.argv[1]):
    project_id, project_name = map(lambda x: x.strip(), line.split('\t'))
    projects[project_id] = project_name

for line in sys.stdin:
    project_id, proceeds = map(lambda x: x.strip(), line.split())
    if project_id != cur_project and cur_project is not None:
        print('{0:<30} {1:>9}'.format(projects.get(project_id, 'None'), total))
        total = 0
    total += int(proceeds)
    cur_project = project_id
        
