---
marp: true
theme: uncover
__class: invert
---

# Intro to Pants
Da
2022/08/08

---

## What is Pants
Pants 2 is a fast, scalable, user-friendly build system for codebases of **all sizes**.

> currently for **Python, Go, Java, Scala, Shell, and Docker**

---

## Advantages of monorepos
+ Simplified organization
+ Simplified dependencies
+ Tooling (e.g. the tool adopt at Tubi to manage Databricks clusters)
+ Cross-project changes

See:
http://danluu.com/monorepo/

---

## Pants for Data/ML Engineering

+ Airflow Dags in Pants
+ PySpark/Spark Jobs in Pants
+ Dataset Definitions in Pants

Using pants, we can centralize all Data/ML Engineering code in one Git repo.

> **How about create only one pull request with one approvement for your ticket?!**

---
## Why Pants

### Now: Python is the first class language
+ BUILD.pants and macros are in Python language without import
+ Pants Plugins are in Python
+ PEX: a library for generating .pex files which are executable Python environments
### Future: mature Python/Java/Scala (for Data/ML) support

---
## Core Concepts
+ Resolve and Lockfile
+ Dependency Management
  + bound to resolve
  + per python file (shading like Maven)
  + dependency inference
+ Advanced Caching just like Maven/SBT

---
## Pants-PySpark
The DEMO Project for PySpark based monorepo

https://github.com/da-tubi/pants-pyspark

+ cat: pyspark 3.2.1
+ dog: pyspark 3.1.2
+ common: either pyspark 3.1.2 or pyspark 3.2.1
