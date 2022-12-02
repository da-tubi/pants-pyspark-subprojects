# pants-pyspark: A Demo for PySpark based monorepo [slides](docs/pants.md)

## Three reasons to adopt pants
+ User Friendly
+ Fast
+ Reproducible
## Howto
### How to install the pants build tool
Just use `./pants` bootstrap script and make sure that `python3` is available. If `python3` is not available,
just use `homebrew` to install python3 or use `conda` to create a python3 environment. Please use Python >=3.8.

You could use the following command line to test installation of pants:
```
./pants version
```

### How to add a new subproject
See https://github.com/da-tubi/pants-pyspark/pull/5

And do not forget to generate the lockfile, eg.
```
bin/lock cat
```

## Cheatsheat
``` bash
# run single unit tests
./pants test tests/tubi/cat/tail_test.py --  -s

# run all unit tests
./pants test :: --  -s

# test only the changed part
./pants --changed-since=main  test

# list all packages
bin/package

# package for tubi-cat
bin/package tubi-cat
```

## IDE Integration
``` bash
./pants export ::
```
For PyCharm, just select the Python interpreter. For example,
```
dist/export/python/virtualenvs/cat/3.8.10/bin/python
```
