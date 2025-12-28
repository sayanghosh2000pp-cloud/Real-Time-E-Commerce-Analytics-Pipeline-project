from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("RealTimeEcommerce").getOrCreate()

schema = StructType([
    StructField("order_id", IntegerType()),
    StructField("user_id", IntegerType()),
    StructField("amount", FloatType()),
    StructField("category", StringType()),
    StructField("timestamp", FloatType())
])

df = spark.readStream.format("kafka")    .option("kafka.bootstrap.servers", "localhost:9092")    .option("subscribe", "transactions")    .load()

json_df = df.selectExpr("CAST(value AS STRING)")    .select(from_json(col("value"), schema).alias("data"))    .select("data.*")

agg_df = json_df.groupBy("category").sum("amount")

query = agg_df.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
