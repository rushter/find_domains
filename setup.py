from setuptools import setup, find_packages
import os

ROOT = os.path.dirname(os.path.realpath(__file__))

with open('README.md') as inp:
    readme_content = inp.read()

setup(
    name = 'find_domains',
    version = '0.0.6',
    author = 'Gregory Petukhov',
    author_email = 'lorien@lorien.name',
    maintainer='Gregory Petukhov',
    maintainer_email='lorien@lorien.name',
    url='https://github.com/lorien/find_domains',
    description = 'Library to search domain names in text data',
    long_description = readme_content,
    long_description_content_type='text/markdown',
    packages = find_packages(exclude=['test']),
    download_url='https://github.com/lorien/find_domains/releases',
    license = "MIT",
    install_requires = [
        'tldextract',
    ],
    keywords='domain search hostname dns parser',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
