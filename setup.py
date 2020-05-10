import os

from setuptools import setup

import testoot

setup(
    name="testoot",
    version=testoot.version,
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.md")).read(),
    long_description_content_type="text/markdown",
    package_dir={"testoot": "testoot"},
    packages=[
        "testoot",
        "testoot.ext",
    ],
    author="Alexander Ptakhin",
    author_email="me@aptakhin.name",
    description="Library",
    license="MIT",
    keywords="testing out of code",
    url="https://github.com/aptakhin/testoot",
    project_urls={
        "Source Code": "https://github.com/aptakhin/testoot",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Framework :: Pytest",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing :: Unit",
    ],
)
