#!/usr/bin/env python

import sys

current_path = None
requested_count = 0

for line in sys.stdin:
    new_path = line.strip().split()
    if len(new_path) != 1:
        continue

    if current_path and current_path != new_path:
        print "{0}\t{1}".format(current_path, requested_count)
        requested_count = 0

    current_path = new_path
    requested_count += 1

if current_path != None:
    print "{0}\t{1}".format(current_path, requested_count)

