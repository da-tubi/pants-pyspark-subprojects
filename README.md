# pants-pyspark: A Demo for PySpark based monorepo

## Three reasons to adopt pants
1. virutalenv/conda/pyenv is **NOT** needed
2. **Monorepo friendly**
   + test/lint/fmt **only the changed part** ./pants --changed-since=main  test
   + the way to track dependencies for subprojects
   + …
3. **Smart dependencies inference** via python imports
   + eg. in the cat subproject, I add the rikai==0.1.13 , and I have not imported rikai. In this way, rikai will not be a dep in the whl python package

## Monorepo
### How to install the pants build tool
Just use `./pants` bootstrap script and make sure that `python3` is available. If `python3` is not available,
just use `homebrew` to install python3 or use `conda` to create a python3 environment. Please use Python >=3.8.

You could use the following command line to test installation of pants:
```
./pants version
```

### How to add a new subproject
See https://github.com/da-tubi/pants-pyspark/pull/3

#### Part 1: sources/tests/dependencies
```
tubi/duck
├── BUILD.pants
├── tail.py
└── tail_test.py
```
The new project is maintained in `tubi/{proj_name}` as above. There are python sources and tests and a `BUILD` file
to define the 3rd dependencies under the resolve `{proj_name}_req`.

#### Part 2: Lock down the resolve
```
--- a/pants.toml
+++ b/pants.toml
@@ -19,7 +19,6 @@ enable_resolves = true
 [python.resolves]
   cat_req = "3rdparty/cat.lock"
   dog_req = "3rdparty/dog.lock"
+  duck_req = "3rdparty/duck.lock"

```
You must generate the lockfile via `./pants generate-lockfiles` to lock down all defined dependencies before developing.

#### Part 3: Put package info in `tubi/BUILD.pants`
```
--- a/tubi/BUILD.pants
+++ b/tubi/BUILD.pants
@@ -27,3 +27,19 @@ python_distribution(
         version="0.1.0",
     ),
 )
+
+########################################
+# Packaging for duck
+########################################
+python_distribution(
+    name="tubi-duck",
+    dependencies=[
+        "tubi/duck:sources",
+        "tubi/common:sources@resolve=duck_req",
+    ],
+    provides=python_artifact(
+        name="tubi-duck",
+        version="0.1.0",
+    ),
+)
+
```



## Cheatsheat
``` bash
# run single unit tests
./pants test tubi/cat/tail_test.py --  -s

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
