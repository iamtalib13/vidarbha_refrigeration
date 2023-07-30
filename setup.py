from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vidarbha_refrigeration/__init__.py
from vidarbha_refrigeration import __version__ as version

setup(
	name="vidarbha_refrigeration",
	version=version,
	description="Refrigeration Buisness management",
	author="Talib Sheikh",
	author_email="talibsheikh16@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
