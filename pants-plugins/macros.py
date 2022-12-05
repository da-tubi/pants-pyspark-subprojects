def tubi_project(name, runtime_deps=[], customize_sources=False, customize_tests=False):
    python_requirements(
        name=f"{name}_requirements",
        source=f"tubi/{name}/requirements.txt",
        resolve=name,
    )

    if not customize_sources:
        deps = [f":{name}_requirements#{dep}" for dep in runtime_deps]
        python_sources(
            name=f"{name}_sources",
            sources=[f"tubi/{name}/*.py"],
            dependencies=deps,
            resolve=name,
        )
    
    if not customize_tests:
        python_tests(
            name=f"{name}_tests",
            sources=[f"tests/tubi/{name}/*.py"],
            resolve=name,
        )
