from setuptools import find_packages, setup

PROJECT_NAME = "homn"

with open("CHANGELOG.md", "r") as fh:
    for line in fh.readlines():
        if "Current Version: " in line:
            version = line.replace("Current Version: ", "").strip()
            break

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

try:
    with open("dev_requirements.txt", "r") as fh:
        dev_requirements = fh.readlines()
except FileNotFoundError:
    dev_requirements = []

setup(
    name=PROJECT_NAME,
    version=version,
    description="Scriptable CI/CD Pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Anthony Post",
    author_email="postanthony3000@gmail.com",
    license="MIT License",
    url=f"https://github.com/Ayehavgunne/{PROJECT_NAME}/",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    python_requires=">=3.10",
)
