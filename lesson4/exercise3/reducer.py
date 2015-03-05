#!/usr/bin/env python

import sys
import re
import collections

inverted_index = collections.defaultdict(list)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    word = data[1].lower()
    inverted_index[word].append(data[0])

for word in inverted_index:
    print "{0}\t{1}\t{2}".format(word, len(inverted_index[word]), inverted_index[word])

