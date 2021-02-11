from setuptools import (
    setup,
    find_packages
)

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.read().strip().split('\n')

setup(
    name='pyrbm',
    version='0.1.0',
    description='Restricted Boltzmann Machine implementation with PyTorch',
    long_description=LONG_DESCRIPTION,
    author='Stoyan Vitanov',
    author_email='stoyan.a.vitanov@gmail.com',
    packages=find_packages('src'),
    install_requires=INSTALL_REQUIRES
)
