import ast
import os
import sys

# from distutils.core import 
from setuptools import find_packages, setup, Extension

here = os.path.abspath(os.path.dirname(__file__))
src = os.path.join(here, "src/use")

# Instead of doing the obvious thing (importing 'use' directly and just reading '__version__'),
# we are parsing the version out of the source AST here, because if the user is missing any
# dependencies at setup time, an import error would prevent the installation.
# Two simple ways to verify the installation using this setup.py file:
#
#     python3 setup.py develop
#
#  or:
#
#    python3 setup.py install
#


with open(os.path.join(src, "__init__.py")) as f:
    mod = ast.parse(f.read())
    version = [t for t in [*filter(lambda n: isinstance(n, ast.Assign), mod.body)] if t.targets[0].id == "__version__"][0]
    while hasattr(version, "value") or isinstance(version, ast.Str):
        if hasattr(version, "value"):
            version = version.value
        if isinstance(version, ast.Str):
            version = version.s
with open(about_path := (os.path.join(src, "about.c")), "w") as f:
    f.write("extern int PyInit_about() {}")

meta = {
    "name": "justuse",
    "license": "MIT",
    "url": "https://github.com/amogorkon/justuse",
    "version": version,
    "author": "Anselm Kiefner",
    "author_email": "justuse-pypi@anselm.kiefner.de",
    "python_requires": ">=3.8",
    "keywords": [
        "installing",
        "packages",
        "hot reload",
        "auto install",
        "aspect oriented",
        "version checking",
        "functional",
    ],
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    "extras_require": {"test": ["pytest", "pytest-cov", "pytest-env"]},
    "fullname": "justuse",
    "dist_files": [],
    "description": "a pure-python alternative to import",
    "maintainer_email": "justuse-pypi@anselm.kiefner.de",
    "maintainer": "Anselm Kiefner",
    "platforms": ["any"],
    "download_url": "https://github.com/amogorkon/justuse/" "archive/refs/heads/main.zip",
    "ext_modules": [
        Extension(
            "about",
            [str(about_path)],
            optional=False,
        ),
    ],
}


requires = (
    "requests(>= 2.24.0)",
    "packaging(== 21.0)",
    "pydantic(>= 1.8.2)",
    "pip(== 21.2.1)",
    "furl(>= 2.1.2)",
    "wheel(>= 0.36.2)",
    "icontract(>= 2.5.4)",
    "beartype(>= 0.0.0)",
)


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    packages=[
      *find_packages(where="src"),
      "justuse",
    ],
    package_dir={"": "src", "justuse": "tests"},
    package_name="use",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    requires=requires,
    install_requires=requires,
    setup_requires=requires,
    zip_safe=True,
    **meta,
)

