import os
import sys

import setuptools  # Don't delete, hook for distutils

from distutils.core import setup


setup(
	name="regress",
	version="0.0.3",
	long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.md")).read(),
	long_description_content_type="text/markdown",
	package_dir={"regress": "regress"},
	packages=[
		"regress",
		"regress.ext",
		"regress.impl",
		"regress.impl.context",
		"regress.impl.serializer",
		"regress.impl.storage",
	],
    author="Alexander Ptakhin",
    author_email="me@aptakhin.name",
    description="Library",
    license="MIT",
    keywords="regression testing",
    url="https://github.com/aptakhin/regress",
    project_urls={
        "Source Code": "https://github.com/aptakhin/regress",
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
