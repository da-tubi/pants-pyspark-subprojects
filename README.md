# pants-pyspark: A Demo for PySpark based monorepo

## Three reasons to adopt pants
1. virutalenv/conda/pyenv is NOT needed
2. monorepo friendly
   + test/lint/fmt only the changed part ./pants --changed-since=main  test
   + the way to track dependencies for subprojects
   + …
3. Smart dependencies inference via python imports
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
├── BUILD
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

#### Part 3: Put sources/tests/package info in `tubi/BUILD`
```
--- a/tubi/BUILD
+++ b/tubi/BUILD
@@ -1,11 +1,13 @@
-project_names = ["cat", "dog"]
+project_names = ["cat", "dog", "duck"]
 project_srcs = {
     "cat": ["cat/**", "common/**"],
     "dog": ["dog/**", "common/**"],
+    "duck": ["duck/**", "common/**"],
 }
 project_tests = {
     "cat": ["cat/*_test.py"],
     "dog": ["dog/*_test.py"],
+    "duck": ["duck/*_test.py"],
 }

 for proj in project_names:
@@ -46,3 +48,16 @@ python_distribution(
         version="0.1.0",
     ),
 )
+
+
+########################################
+# Packaging for duck
+########################################
+python_distribution(
+    name="tubi-duck",
+    dependencies=[":duck-srcs"],
+    provides=python_artifact(
+        name="tubi-duck",
+        version="0.1.0",
+    ),
+)
```



## Cheatsheat
``` bash
# run single unit tests
./pants test tubi/cat/tail_test.py --  -s

# run all unit tests
./pants test :: --  -s

# test only the changed part
./pants --changed-since=main  test

# package all subprojects
./pants package ::

# generate lockfiles
./pants generate-lockfiles

# REPL
./pants repl tubi/cat/tail.py

# format
./pants update-build-files
./pants fmt ::
```

## IDE Integration
``` bash
./pants export ::
```
For PyCharm, just select the Python interpreter. For example,
```
dist/export/python/virtualenvs/cat/3.8.10/bin/python
```
