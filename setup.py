import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open

with open("README.md", encoding="utf-8") as file:
    readme = file.read()

setup(
    name="outgraph",
    description="Outlier detection algorithm for graph datasets",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="v1.0.0",
    packages=["outgraph"],
    python_requires=">=3",
    url="https://github.com/shobrook/outgraph",
    author="shobrook",
    author_email="shobrookj@gmail.com",
    # classifiers=[],
    install_requires=[],
    keywords=["outlier-detection", "outlier", "graph", "mahalanobis"],
    license="MIT"
)
