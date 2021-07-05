from pyspark.sql import SparkSession
from pyspark import SparkContext


sc = SparkContext(master='local')

spark = SparkSession(sc)

cat = spark.read.csv("hdfs://namenode:9000/data/openbeer/cat/cat.csv")

cat.registerTempTable('tab_name')

spark.sql("""
insert into table test.comments
select
cast(_c0 as int),
cast(_c1 as int),
cast(_c2 as int),
_c3
_c4,
_c5,
_c6,
_c7,
_c8,
cast(_c9 as timestamp),
cast(_c10 as int),
_c11,
cast(_c12 as int),
cast(_c13 as binary),
_c14,
_c15,
_c16,
_c17,
_c18,
_c19,
_c20
from tab_name
""")

spark.stop()
