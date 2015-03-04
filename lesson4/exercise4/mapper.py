import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print "{0}\t{1}".format(date, cost)

def main():
    mapper()

main()
