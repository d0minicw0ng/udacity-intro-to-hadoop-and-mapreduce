#!/usr/bin/env python

import sys

current_ip_address = None
current_ip_address_count = 0

for line in sys.stdin:
    new_ip_address = line.strip().split()
    if len(new_ip_address) != 1:
        continue

    if current_ip_address and current_ip_address != new_ip_address:
        print "{0}\t{1}".format(current_ip_address, current_ip_address_count)
        current_ip_address_count = 0

    current_ip_address = new_ip_address
    current_ip_address_count += 1

if current_ip_address != None:
    print "{0}\t{1}".format(current_ip_address, current_ip_address_count)
