from setuptools import setup, find_packages

from liblio import LIBLIO_VERSION

setup(
    name='liblio',
    version=LIBLIO_VERSION,
    author='Michael H. Potter',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask'
    ]
)
