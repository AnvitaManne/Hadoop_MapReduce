# Hadoop MapReduce for Image Analytics

Python-based Hadoop MapReduce workflow for aggregating image-classification data by terrain type.

## Project Overview

This project uses the Intel Image Classification dataset and prepares image metadata into a structured CSV before processing it through a Python-based MapReduce workflow.

The implementation demonstrates:

- Dataset preparation from image folders
- Map
- Combine
- Partition
- Shuffle and Sort
- Reduce
- HDFS data preparation
- Hadoop Streaming job execution
- Output verification

## Dataset

The project uses the Intel Image Classification dataset with six terrain categories:

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

The original image dataset is **not included** in this repository.

## Files

- `dataset.py` — creates `geodataset.csv` from the image-folder structure and randomly shuffles the records.
- `mapper.py` — reads the CSV, performs the map/combine/partition stages, and emits intermediate key-value pairs.
- `reducer.py` — performs shuffle/sort and reduction to aggregate counts by terrain type.

## Local Test

```bash
cat geodataset.csv | python ./mapper.py | sort | python ./reducer.py
```

## Hadoop / HDFS Execution

The project was executed in a Cloudera QuickStart Hadoop environment.

```bash
chmod +x dataset.py mapper.py reducer.py

hdfs dfs -rm -r /user/cloudera/my_project
hdfs dfs -mkdir -p /user/cloudera/my_project
hdfs dfs -put geodataset.csv /user/cloudera/my_project
hdfs dfs -ls /user/cloudera/my_project
```

Hadoop Streaming job:

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper ./mapper.py \
-reducer ./reducer.py \
-input /user/cloudera/my_project/geodataset.csv \
-output /user/cloudera/my_project/output
```

Retrieve the output:

```bash
hdfs dfs -cat /user/cloudera/my_project/output/part-00000
```

## Results

Final aggregated counts reported from the Hadoop job:

| Terrain | Image Count |
|---|---:|
| Buildings | 2191 |
| Forest | 2271 |
| Glacier | 2404 |
| Mountain | 2512 |
| Sea | 2274 |
| Street | 2382 |

## Tech Stack

Python · Hadoop · HDFS · MapReduce · Hadoop Streaming · Cloudera QuickStart VM

## Note

The Python source files in this repository preserve the code shown in the project report. The original report and full image dataset are intentionally not included.
