# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.

python_requirement(
    name="cat_deps",
    requirements=["pyspark==3.1.2"],
    resolve="cat"
)

python_requirement(
    name="dog_deps",
    requirements=["pyspark==3.2.1"],
    resolve="dog"
)
