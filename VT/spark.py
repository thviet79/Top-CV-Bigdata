# PySpark
import os
os.environ['SPARK_LOCAL_IP'] = '192.168.100.200'

from pyspark.sql import SparkSession
# sc.setLogLevel("INFO")

spark = SparkSession.builder \
    .appName("ReadFromHDFS") \
    .getOrCreate()
