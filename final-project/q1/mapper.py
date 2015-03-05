#!/usr/bin/env python

import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    author_id = line[3]
    added_at = line[8]

    if author_id == "author_id":
        continue

    print "{0}\t{1}".format(author_id, added_at)
