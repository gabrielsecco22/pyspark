from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.master("local").config(conf=SparkConf()).getOrCreate()

df = spark.read.format("csv") \
        .option("header", "true") \
        .load("/user-data-*.csv")

df.show()
# results = df.groupBy("`dob.age`","`gender`") \
#             .count() \
#             .orderBy(col("count").desc())
#
# results.show()
#
# results.coalesce(1).write.csv("hdfs:///results", sep=",", header="true")