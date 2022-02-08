from unicodedata import name
from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='binary_parser',
    version='0.0.3',
    description='convert integers to binary and vice-a-versa',
    long_description=open('README.rst', encoding="utf8").read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Dhananjay Pai',
    author_email='dhananjay2002pai@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='binary to numbers',
    packages=find_packages(exclude=['tests']),
    install_requires=['']
)