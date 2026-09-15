# Execution Notes

The following commands are taken from the project report.

## Local file transfer

cp "/media/sf_Downloads/archive (2).zip" .
cp /media/sf_Downloads/dataset.py .
cp /media/sf_Downloads/mapper.py .
cp /media/sf_Downloads/reducer.py .

## Dataset processing

mv "archive (2).zip" archive.zip
unzip archive.zip
python ./dataset.py

## Local testing

cat geodataset.csv | python ./mapper.py | sort | python ./reducer.py

## HDFS preparation

chmod +x dataset.py mapper.py reducer.py
hdfs dfs -rm -r /user/cloudera/my_project
hdfs dfs -mkdir -p /user/cloudera/my_project
hdfs dfs -put geodataset.csv /user/cloudera/my_project
hdfs dfs -ls /user/cloudera/my_project

## Hadoop Streaming

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper ./mapper.py \
-reducer ./reducer.py \
-input /user/cloudera/my_project/geodataset.csv \
-output /user/cloudera/my_project/output

## Output

hdfs dfs -cat /user/cloudera/my_project/output/part-00000

## YARN logs

yarn application -list -appStates FINISHED
yarn logs -applicationId <application_id>
