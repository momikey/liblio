from setuptools import setup, find_packages

setup(
    name='liblio',
    version='0.0.1',
    author='Michael H. Potter',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask'
    ]
)
