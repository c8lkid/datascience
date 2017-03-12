#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python get_interest_v4.py group_name count_items

import sys
import json
import requests

interests = {}

if (len(sys.argv) < 2):
    print sys.argv[0] + ' group_name count_items'
    sys.exit(1)

GROUP_REQ = 'https://api.vk.com/method/groups.getMembers?group_id=' + sys.argv[1] \
            + '&count=' + sys.argv[2] + '&v=5.52'

user_ids = json.loads(requests.get(GROUP_REQ).text)
user_ids = user_ids['response']['items']

j = 0
for user_id in user_ids:
    i = json.loads(requests.get('https://api.vk.com/method/users.get?user_ids=' + str(user_id) + '&fields=interests&v=5.52').text)
    for interest in i['response'][0].get('interests', '').split(','):
        interests[interest.strip()] = interests.get(interest.strip(), 0) + 1 

    # if j%50 == 0: print('{0:<4} items of {1:>4}'.format(j, len(user_ids)))
    # j += 1

print(len(interests.keys()))

for k, v in interests.items():
    print('{0}\t{1}'.format(k.encode('utf-8'), v))
