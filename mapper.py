#!/usr/bin/env python3
from __future__ import print_function
import sys
import csv
#1. Input data
sys.stderr.write("1. Input data\n\n")
reader=csv.reader(sys.stdin)
header=next(reader, None)
rows=[row for row in reader if len(row)>=2]
split=len(rows) // 2
split1=rows[:split]
split2=rows[split:]
sys.stderr.write("Input split 1 :\n\n")
for r in split1[:5]:
    sys.stderr.write(str(r) + "\n")
sys.stderr.write("\n\n")
sys.stderr.write("Input split 2 :\n\n")
for r in split2[:5]:
    sys.stderr.write(str(r) + "\n")
#2. Map
sys.stderr.write("2. Map\n\n")
sys.stderr.write("Node A\n")
mapped_data1=[]
for r in split1:
    terrain=r[1]
    mapped_data1.append((terrain, 1))
for pair in mapped_data1[:10]:
    sys.stderr.write(str(pair) + "\n")
sys.stderr.write("\n\n")
sys.stderr.write("Node B\n")
mapped_data2 = []
for r in split2:
    terrain = r[1]
    mapped_data2.append((terrain, 1))
for pair in mapped_data2[:10]:
    sys.stderr.write(str(pair) + "\n")
#3. Combine
sys.stderr.write("3. Combine\n")
sys.stderr.write("Node A\n")
combined_data1={}
for key, value in mapped_data1:
    if key not in combined_data1:
        combined_data1[key]=1
    else:
        combined_data1[key]+=1
for key, value in combined_data1.items():
    sys.stderr.write("({0}, {1})\n".format(key, value))
sys.stderr.write("\n\n")
sys.stderr.write(" Node B\n")
combined_data2={}
for key, value in mapped_data2:
    if key not in combined_data2:
        combined_data2[key]=1
    else:
        combined_data2[key]+=1
for key, value in combined_data2.items():
    sys.stderr.write("({0}, {1})\n".format(key, value))
#4. Partition
sys.stderr.write("4. Partition\n\n")
all_keys=set(list(combined_data1.keys())+list(combined_data2.keys()))
n=2
r0_keys=[]
r1_keys=[]
for key in all_keys:
    if hash(key)% n== 0:
        r0_keys.append(key)
        sys.stderr.write("'{0}' assigned to Reducer 0\n".format(key))
    else:
        r1_keys.append(key)
        sys.stderr.write("'{0}' assigned to Reducer 1\n".format(key))
sys.stderr.write("\n\n")
sys.stderr.write("Keys assigned to Reducer 0: {0}\n".format(r0_keys))
sys.stderr.write("Keys assigned to Reducer 1: {0}\n".format(r1_keys))
#Outputs intermediate key-value pairs
#Merge the two dictionaries for output
combined_all = combined_data1.copy()
combined_all.update(combined_data2)
for key, value in combined_all.items():
    print("{0}\t{1}".format(key, value))
