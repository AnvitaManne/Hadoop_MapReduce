#!/usr/bin/env python3
from __future__ import print_function
import sys
#5. Shuffle and Sort
sys.stderr.write("5. Shuffle and Sort\n\n")
sys.stderr.write("Shuffle\n")
shuffled={}
for line in sys.stdin:
    key, value=line.strip().split("\t")
    value=int(value)
    if key not in shuffled:
        shuffled[key]=[]
    shuffled[key].append(value)
r0=[]
r1=[]
for key, values in shuffled.items():
    if hash(key)%2==0:
        for v in values:
            r0.append((key, v))
    else:
        for v in values:
            r1.append((key, v))
sys.stderr.write("Reducer 0\n")
for key, value in r0:
    sys.stderr.write("('{0}', {1})\n".format(key, value))
sys.stderr.write("\n\n")
sys.stderr.write("Reducer 1\n")
for key, value in r1:
    sys.stderr.write("('{0}', {1})\n".format(key, value))
sys.stderr.write("\n\n")
sys.stderr.write("Sort and Merge\n")
r0=sorted(r0)
r1=sorted(r1)
sys.stderr.write("Reducer 0\n")
merged_data0={}
for key, value in r0:
    merged_data0.setdefault(key, []).append(value)
for key, values in merged_data0.items():
    sys.stderr.write("('{0}', {1})\n".format(key, values))
sys.stderr.write("\n\n")
sys.stderr.write("Reducer 1\n")
merged_data1={}
for key, value in r1:
    merged_data1.setdefault(key, []).append(value)
for key, values in merged_data1.items():
    sys.stderr.write("('{0}', {1})\n".format(key, values))
sys.stderr.write("\n\n")
# 6. Reduce
sys.stderr.write("6. Reduce\n\n")
reduced_output=[]
for key, values in merged_data0.items():
    count = sum(values)
    reduced_output.append((key, count))
    sys.stderr.write("{0}, {1}\n".format(key, count))
for key, values in merged_data1.items():
    count=sum(values)
    reduced_output.append((key, count))
    sys.stderr.write("{0}, {1}\n".format(key, count))
print("The count of images corresponding to each terrain type is:")
for key, count in reduced_output:
    print("{0}:{1}".format(key, count))
