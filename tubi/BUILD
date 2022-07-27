########################################
# Project cat
########################################

python_sources(
    name="cat-srcs",
    sources = [
        "cat/**",
        "common/**"
    ],
    resolve="cat_req",
)

python_tests(
    name="cat-tests",
    sources = [
        "cat/*_test.py"
    ],
    resolve="cat_req",
)

python_distribution(
    name="tubi-cat",
    dependencies=[":cat-srcs"],
    provides=python_artifact(
        name="tubi-cat",
        version="0.1.0",
    ),
)

########################################
# Project dog
########################################

python_sources(
    name="dog-srcs",
    sources = [
        "dog/**",
        "common/**"
    ],
    resolve="dog_req",
)

python_tests(
    name="dog-tests",
    sources = [
        "dog/*_test.py"
    ],
    resolve="dog_req",
)

python_distribution(
    name="tubi-dog",
    dependencies=[":dog-srcs"],
    provides=python_artifact(
        name="tubi-dog",
        version="0.1.0",
    ),
)
