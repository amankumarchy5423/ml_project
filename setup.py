from setuptools import setup,find_packages


def get_requirement()->list[str] :
    require: list[str] = []
    with open('Requirement.txt','r') as f:
        lines = f.readlines()
        # print(lines)
        for i in lines:
            line=i.strip()
            if line and line != '-e.':
                require.append(i)
    
    return require

setup(
    name = "ML_Project",
    version = "1.0",
    packages = find_packages(),
    install_requires = get_requirement(),
    author="Aman choudhary"
)

repr = get_requirement()
print(repr)

    