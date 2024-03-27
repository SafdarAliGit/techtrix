from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in techtrix/__init__.py
from techtrix import __version__ as version

setup(
	name="techtrix",
	version=version,
	description="techrix",
	author="techrix",
	author_email="safdar211@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
