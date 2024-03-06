from pyspark.sql import SparkSession


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Read MS SQL Data with PySpark") \
    .config("spark.driver.extraClassPath", "./mssql-jdbc-12.6.0.jre11.jar") \
    .getOrCreate()

# Set up the connection to your MS SQL Server
jdbc_url = "jdbc:sqlserver://127.0.0.1:1433;databaseName=x5"
connection_properties = {
    "user": "SA",
    "password": "MyPass@word",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver",
    "encrypt": "false"
}

# Read data from your MS SQL Server table
df = spark.read.jdbc(url=jdbc_url, table="Employees", properties=connection_properties)

# Display the data
df.show()
