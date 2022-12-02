def tubi_project(**kwargs):
    name=kwargs['name']

    python_requirements(
        name=f"{name}_requirements",
        source=f"tubi/{name}/requirements.txt",
        resolve=name,
    )
    
    python_sources(
        name=f"{name}_sources",
        sources=[f"tubi/{name}/*.py"],
        resolve=name,
    )
    
    python_tests(
        name=f"{name}_tests",
        sources=[f"tests/tubi/{name}/*.py"],
        resolve=name,
    )
