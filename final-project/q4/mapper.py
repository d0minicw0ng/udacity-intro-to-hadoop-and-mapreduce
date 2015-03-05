#!/usr/bin/env python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():
            continue

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]

        if node_type == "question":
            identifier = node_id
        else:
            identifier = abs_parent_id

        print "{0}\t{1}".format(identifier, author_id)
