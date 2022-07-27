########################################
# Project cat
########################################

python_sources(
    name="cat",
    sources = [
        "cat/**",
        "common/**"
    ],
    resolve="cat",
)

python_tests(
    name="cat-tests",
    sources = [
        "cat/*_test.py"
    ],
    resolve="cat",
)

python_distribution(
    name="tubi-cat",
    dependencies=[":cat"],
    provides=python_artifact(
        name="tubi-cat",
        version="0.1.0",
    ),
)

########################################
# Project dog
########################################

python_sources(
    name="dog",
    sources = [
        "dog/**",
        "common/**"
    ],
    resolve="dog",
)

python_tests(
    name="dog-tests",
    sources = [
        "dog/*_test.py"
    ],
    resolve="dog",
)

python_distribution(
    name="tubi-dog",
    dependencies=[":dog"],
    provides=python_artifact(
        name="tubi-dog",
        version="0.1.0",
    ),
)
