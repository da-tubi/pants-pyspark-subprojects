project_names = ["cat", "dog"]
project_srcs = {
    "cat": ["cat/**", "common/**"],
    "dog": ["dog/**", "common/**"],
}
project_tests = {
    "cat": ["cat/*_test.py"],
    "dog": ["dog/*_test.py"],
}

for proj in project_names:
    sources = project_srcs[proj]
    sources.append("!*_test.py")
    python_sources(
        name=f"{proj}-srcs",
        sources=sources,
        resolve=f"{proj}_req",
    )

    python_tests(
        name=f"{proj}-tests",
        sources=project_tests[proj],
        resolve=f"{proj}_req",
    )

########################################
# Packaging for cat
########################################
python_distribution(
    name="tubi-cat",
    dependencies=[":cat-srcs"],
    provides=python_artifact(
        name="tubi-cat",
        version="0.1.0",
    ),
)

########################################
# Packaging for dog
########################################
python_distribution(
    name="tubi-dog",
    dependencies=[":dog-srcs"],
    provides=python_artifact(
        name="tubi-dog",
        version="0.1.0",
    ),
)
