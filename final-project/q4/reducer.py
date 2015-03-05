#!/usr/bin/env python

import sys

last_question = None
students = []

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue

    question, author = data

    if last_question != None and last_question != question:
        print "{0}\t{1}".format(last_question, students)
        students = []

    last_question = question
    students.append(author)

if last_question != None:
    print "{0}\t{1}".format(last_question, students)



