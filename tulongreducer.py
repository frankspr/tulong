#!/usr/bin/env python
from operator import itemgetter
import operator
import sys
count_dict = {}
for line in sys.stdin:
    line = line.strip()
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count_dict:
    print "%s\t%d" % (item[0], item[1])
