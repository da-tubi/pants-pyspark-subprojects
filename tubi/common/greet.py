import pyspark

def greet(who, what):
    print(f"I am a {who}'s {what} with PySpark {pyspark.__version__}\n")
