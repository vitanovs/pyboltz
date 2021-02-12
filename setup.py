import subprocess
from setuptools import (
    setup,
    find_packages
)

_version_cmd = 'git describe --tags'.split()
VERSION = subprocess.run(_version_cmd).stdout

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.read().strip().split('\n')

setup(
    name='pyboltz',
    version=VERSION,
    description='Boltzmann Machine implementation with PyTorch',
    long_description=LONG_DESCRIPTION,
    author='Stoyan Vitanov',
    author_email='stoyan.a.vitanov@gmail.com',
    packages=find_packages('src'),
    install_requires=INSTALL_REQUIRES
)
