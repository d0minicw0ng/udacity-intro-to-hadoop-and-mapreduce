import sys
from datetime import datetime

def combiner():
    sales_for_each_day_of_the_week = [0] * 7
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 2:
            date, sale = data
            weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
            sales_for_each_day_of_the_week[weekday] += float(sale)

    for weekday, sales_total in enumerate(sales_for_each_day_of_the_week):
        print "{0}\t{1}".format(weekday, sales_total)

def main():
    combiner()

main()
