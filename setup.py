from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in duys/__init__.py
from duys import __version__ as version

setup(
	name="duys",
	version=version,
	description="Duys Apps",
	author="Duys",
	author_email="dercio.bobo@duys.co.mz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
