#!/usr/bin/env python

import sys

sales_total = 0
old_key = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_sale = data

    if old_key and old_key != this_key:
        print "#{0}\t{1}".format(old_key, sales_total)
        sales_total = 0

    old_key = this_key
    sales_total += float(this_sale)

if old_key != None:
    print "#{0}\t{1}".format(old_key, sales_total)
