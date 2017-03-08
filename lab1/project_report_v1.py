#!/usr/bin/env python

import sys

if len(sys.argv) <= 1:
    print(sys.argv[0] + ' filename')
    sys.exit(1)

# create dict with uniq project ids
projects = {}
for line in open(sys.argv[1]):
    project_id, project_name = line.split('\t')
    projects[project_id] = project_name.strip()

# for key, value in projects.items():
#     print('{0}\t{1}'.format(key, value))

# output proceedes by project name
for line in sys.stdin:
    project_id, proceedes = line.split()
    if project_id in projects.keys():
        print('{0:<30} {1:>10}'.format(projects[project_id], proceedes))
