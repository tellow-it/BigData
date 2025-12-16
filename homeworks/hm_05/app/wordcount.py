from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("WordCount") \
    .master("local[*]") \
    .getOrCreate()

# Пример данных
lines = spark.sparkContext.parallelize([
    "hello world", "hello pyspark", "pyspark is great", "hello world again"
])

words = lines.flatMap(lambda line: line.split())
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

print("Word counts:")
for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()