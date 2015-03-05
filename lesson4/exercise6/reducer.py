#!/usr/bin/env python

import sys

users_attrs = dict()
posts_attrs = dict()

for line in sys.stdin:
    data = line.strip().split("\t")

    if data[1] == "A":
        user_id, type, reputation, gold, silver, bronze = data
        users_attrs[user_id] = [reputation, gold, silver, bronze]
    elif data[1] == "B":
        author_id, type, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data
        posts_attrs[id] = [id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score]

for post_id in posts_attrs:
    id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score = posts_attrs[post_id]
    reputation, gold, silver, bronze = users_attrs[author_id]
    print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze)
