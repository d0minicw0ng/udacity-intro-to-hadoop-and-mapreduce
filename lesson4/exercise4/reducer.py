#!/usr/bin/env python

import sys
from datetime import datetime
import collections

sales_for_each_day_of_the_week = collections.defaultdict(list)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        date, sale = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        sales_for_each_day_of_the_week[weekday].append(float(sale))

for weekday in sales_for_each_day_of_the_week:
    mean = sum(sales_for_each_day_of_the_week[weekday]) / len(sales_for_each_day_of_the_week[weekday])
    print "{0}\t{1}".format(weekday, mean)
