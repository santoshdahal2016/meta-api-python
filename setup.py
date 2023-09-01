from setuptools import setup, find_packages

# Define package metadata
NAME = 'meta-api-python'
VERSION = '0.1.0'
DESCRIPTION = 'Python wrapper to the various APIs in Meta Platform'
AUTHOR = 'Santosh Dahal'
EMAIL = 'dahalsantosh2018@gmail.com'
URL = 'https://github.com/santoshdahal2016/meta-api-python.git'

# Specify package dependencies
INSTALL_REQUIRES = [
    "requests"
]

DEV_REQUIRES = [
    "pytest"
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

# Define the packages to be included in the distribution
PACKAGES = find_packages()

# Create the setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,

)
