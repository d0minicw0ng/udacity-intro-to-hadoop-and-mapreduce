import sys

def reducer():
    sales_total = 0
    total_number_of_sales = 0

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        store, sale = data
        sales_total += float(sale)
        total_number_of_sales += 1

    print "{0}\t{1}".format(sales_total, total_number_of_sales)

def main():
    reducer()

main()
