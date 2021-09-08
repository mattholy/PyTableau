# -*- encoding: utf-8 -*-

import setuptools
from setuptools import setup

setup(name='pytableau',
        version='0.1',
        description='Let you control your Tableau Server via Python!',
        url='https://github.com/mattholy/PyTableau',
        author='Mattholy',
        author_email='smile.used@hotmail.com',
        license='MIT',
        packages=setuptools.find_packages(),
        zip_safe=True,
        python_requires='>=3.6',
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
    )