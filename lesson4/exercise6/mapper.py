import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        if line[0] == "id" or line[0] == "user_ptr_id":
            continue

        if len(line) == 5:
            user_id, reputation, gold, silver, bronze = line
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(user_id, "A", reputation, gold, silver, bronze)
        else:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}".format(author_id, "B", id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score)

def main():
    mapper()

main()
