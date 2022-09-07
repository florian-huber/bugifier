#!/usr/bin/env python
import os
# read the contents of your README file
from pathlib import Path
from setuptools import find_packages, setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(here, "bugifier", "__version__.py")) as f:
    exec(f.read(), version)

setup(
    name="bugifier",
    version=version["__version__"],
    description="Opposite of what most people want: bugifier adds bugs to your Python code.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Florian Huber",
    author_email="florian.huber@hs-duesseldorf.de",
    url="https://github.com/florian-huber/bugifier",
    packages=find_packages(exclude=['*tests*']),
    package_data={"bugifier": ["data/*.csv"]},
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy",
        "scipy",
    ],
    extras_require={"dev": ["bump2version",
                            "decorator",
                            "isort>=5.1.0",
                            "pylint<2.12",
                            "prospector[with_pyroma]",
                            "pytest",
                            "pytest-cov",
                            "testfixtures",
                            "yapf",]},
)
