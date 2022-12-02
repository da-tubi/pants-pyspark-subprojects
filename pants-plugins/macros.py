def tubi_project(name, customize_sources = False, customize_tests = False):
    python_requirements(
        name=f"{name}_requirements",
        source=f"tubi/{name}/requirements.txt",
        resolve=name,
    )
    
    if not customize_sources:
        python_sources(
            name=f"{name}_sources",
            sources=[f"tubi/{name}/*.py"],
            resolve=name,
        )
    
    if not customize_tests:
        python_tests(
            name=f"{name}_tests",
            sources=[f"tests/tubi/{name}/*.py"],
            resolve=name,
        )
