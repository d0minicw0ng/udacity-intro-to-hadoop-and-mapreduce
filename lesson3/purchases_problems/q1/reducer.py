import sys

def reducer():
    old_product_category = None
    sales_total = 0

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        new_product_category, this_sale = data

        if old_product_category and old_product_category != new_product_category:
            print "{0}\t{1}".format(old_product_category, sales_total)
            sales_total = 0

        old_product_category = new_product_category
        sales_total += float(this_sale)

    if old_product_category != None:
        print "{0}\t{1}".format(old_product_category, sales_total)

def main():
    reducer()

main()

