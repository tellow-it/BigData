# Отчет по ДЗ 1

## Развертывание Standalone hadoop

в docker-compose.yml 2 контейнера, с хадупом и клиентом, в клиенте будут выполняться указанные задачи

## Выполнение задач
### 1. Создайте директорию на HDFS /createme
```
hdfs dfs -fs hdfs://master:8020 -mkdir /createme
```
### 2. Удалите директорию на HDFS
```
hdfs dfs -fs hdfs://master:8020 -rm -r -f /delme
```
### 3. Создайте файл на HDFS /nonnull.txt
```
echo "sometext to file" | hdfs dfs -fs hdfs://master:8020 -put - /nonnull.txt
hdfs dfs -fs hdfs://master:8020 -cat /nonnull.txt
```
вывод
```
sometext to file
```
### 4. Выполните джобу MR wordcount через YARN для файла /shadow.txt
добавление файла
```
hdfs dfs -fs hdfs://master:8020 -put /task_data/shadow.txt /shadow.txt
```
проверка наличия файла
```
hdfs dfs -fs hdfs://master:8020 -ls /
```
выполение подсчета слов через yarn
```
hadoop jar \
  /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar \
  wordcount \
  hdfs://master:8020/shadow.txt \
  hdfs://master:8020/shadow-output
```
вывод
```
Job:1773 - Counters: 36
        File System Counters
                FILE: Number of bytes read=566658
                FILE: Number of bytes written=1839688
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=2710
                HDFS: Number of bytes written=1476
                HDFS: Number of read operations=15
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=4
                HDFS: Number of bytes read erasure-coded=0
        Map-Reduce Framework
                Map input records=2
                Map output records=94
                Map output bytes=1730
                Map output materialized bytes=1818
                Input split bytes=94
                Combine input records=94
                Combine output records=84
                Reduce input groups=84
                Reduce shuffle bytes=1818
                Reduce input records=84
                Reduce output records=84
                Spilled Records=168
                Shuffled Maps =1
                Failed Shuffles=0
                Merged Map outputs=1
                GC time elapsed (ms)=4
                Total committed heap usage (bytes)=832569344
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters 
                Bytes Read=1355
        File Output Format Counters 
                Bytes Written=1476
```

### 5. Запишите число вхождений слова "Анализ" в файл /whataboutinsmouth.txt
```
count=$(hdfs dfs -fs hdfs://master:8020 -cat /shadow-output/* | awk '$1 == "Анализ" {print $2}')
echo "${count:-0}" > /task_data/whataboutinsmouth.txt
```
в файле указано количество слов "Анализ"