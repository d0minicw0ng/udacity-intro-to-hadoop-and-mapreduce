#!/usr/bin/env python

import sys
from collections import Counter

top_ten = dict()
least_used_tag = None
least_used_count = 0

last_tag = None
tag_count = 0

for tag in sys.stdin:
    if last_tag != None and last_tag != tag:
        tag_count = 0

    last_tag = tag
    tag_count += 1

    if top_ten.has_key(tag):
        top_ten[tag] += 1
    else:
        if len(top_ten.keys()) >= 10:
            if tag_count > least_used_count:
                del top_ten[least_used_tag]
                top_ten[tag] = tag_count
        else:
            top_ten[tag] = 1

    if bool(top_ten) == True:
        least_used_tag = min(top_ten, key=top_ten.get)
        least_used_count = top_ten[least_used_tag]

counter = Counter(top_ten)
for data_node in counter.most_common():
    print "{0}\t{1}".format(data_node[0].strip(), data_node[1])




