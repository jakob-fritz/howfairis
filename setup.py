import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.rst", "rt", encoding="UTF-8") as readme_file:
    readme = readme_file.read()

setup(
    name="howfairis",
    entry_points={
        "console_scripts": ["howfairis=howfairis.cli.cli:cli"],
    },
    version="0.14.2",
    description="Python package to analyze compliance with fair-software.eu recommendations",
    long_description=readme + "\n\n",
    author="https://github.com/jspaaks",
    author_email="j.spaaks@esciencecenter.nl",
    url="https://github.com/fair-software/howfairis",
    packages=[
        "howfairis",
        "howfairis.cli",
        "howfairis.exceptions",
        "howfairis.mixins",
        "howfairis.requesting",
        "howfairis.workarounds"
    ],
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="howfairis",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    test_suite="tests",
    install_requires=[
        "backoff == 1.*",
        "beautifulsoup4 == 4.*",
        "click == 7.*",
        "colorama == 0.*",
        "docutils == 0.16.*",
        "pygments == 2.*",
        "ratelimit == 2.*",
        "requests == 2.*",
        "ruamel.yaml == 0.16.*",
        "voluptuous == 0.14.*"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    extras_require={
        "dev": [
            "bumpversion",
            "prospector[with_pyroma]",
            "pycodestyle",
            "pytest-cov",
            "pytest-runner",
            "pytest",
            "recommonmark",
            "requests_mock",
            "sphinx_rtd_theme",
            "sphinx-click",
            "sphinx",
            "yapf"
        ],
        "publishing": [
            "twine",
            "wheel"
        ]
    },
    data_files=[]
)
