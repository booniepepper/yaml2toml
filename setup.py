import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="yaml2toml",
    version="1.0.0",
    description="Convert YAML to TOML",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hiljusti/yaml2toml",
    author="J.R. \"hiljusti\" Hill",
    author_email="hiljusti@pm.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    scripts=["yaml2toml"],
    include_package_data=True,
    install_requires=["yaml", "toml"],
)
