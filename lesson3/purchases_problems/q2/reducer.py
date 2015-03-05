#!/usr/bin/env python

import sys

max_sale = 0
old_store = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    store, sale = data
    sale = float(sale)

    if old_store and old_store != store:
        print "{0}\t{1}".format(old_store, max_sale)
        max_sale = 0

    if sale > max_sale:
        max_sale = sale
    old_store = store

if old_store != None:
    print "{0}\t{1}".format(old_store, max_sale)
