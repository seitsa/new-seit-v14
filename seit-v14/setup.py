from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fayez2/__init__.py
from fayez2 import __version__ as version

setup(
	name="fayez2",
	version=version,
	description="fayez",
	author="fayez",
	author_email="fauzaladeem@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
