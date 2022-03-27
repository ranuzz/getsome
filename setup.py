#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'SQLAlchemy==1.4.29',
    'click==7.1.2',
    'feedparser==6.0.8',
    'requests==2.27.1'
]

test_requirements = ['pytest>=3', ]

setup(
    author="shekhar chandra",
    author_email='ranuzz@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Get something interesting to consume on internet",
    entry_points={
        'console_scripts': [
            'getsome=getsome.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='getsome',
    name='getsome',
    packages=find_packages(include=['getsome', 'getsome.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ranuzz/getsome',
    version='0.1.5',
    zip_safe=False,
)
