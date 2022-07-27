# pants-pyspark: A Demo for PySpark based monorepo
## Cheatsheat
``` bash
# run single unit tests
./pants test tubi/cat/tail_test.py --  -s

# run all unit tests
./pants test :: --  -s

# package all subprojects
./pants package ::

# generate lockfiles
./pants generate-lockfiles

# REPL
./pants repl tubi/cat/tail.py
```

## IDE Integration
``` bash
./pants export ::
```
For PyCharm, just select the Python interpreter. For example,
```
dist/export/python/virtualenvs/cat/3.8.10/bin/python
```
