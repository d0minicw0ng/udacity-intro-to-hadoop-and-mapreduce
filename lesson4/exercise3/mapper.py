import sys
import re
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    delimiters = ['.',',','$',';','!','?',':','"','(',')','[',']','<','>','#','=','-','/',' ']
    regex = '|'.join(map(re.escape, delimiters))
    for line in reader:
        node_id = line[0]
        if node_id == "id":
            continue
        body = re.split(regex, line[4])
        for token in body:
            print "{0}\t{1}".format(node_id, token)

def main():
    mapper()

main()
