import sys

def reducer():
    most_popular_pathname = None
    most_popular_pathname_count = 0

    current_pathname = None
    current_pathname_count = 0

    for line in sys.stdin:
        pathname = line.strip().split()
        if len(pathname) != 1:
            continue

        if current_pathname and current_pathname != pathname:
            if current_pathname_count > most_popular_pathname_count:
                most_popular_pathname = current_pathname
                most_popular_pathname_count = current_pathname_count

            current_pathname_count = 0

        current_pathname = pathname
        current_pathname_count += 1

    print "{0}\t{1}".format(most_popular_pathname, most_popular_pathname_count)


def main():
    reducer()

main()
