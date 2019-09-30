#-------------------------------------------------------------------------------
#
#  Distutils Setup Script
#
# Project: Earth magnetic field in Python.
#
# Author: Steve Shi Chen <chenshi80@gmail.com>
# 
# Original Author: Martin Paces <martin.paces@eox.at>
#-------------------------------------------------------------------------------
# Copyright (C) 2019 Geoist team
#
#-------------------------------------------------------------------------------


import sys
from os.path import join
from distutils.core import setup
from distutils.extension import Extension
import magmod


COMMON_INCLUDE_DIRS = [
    './magmod',
    './magmod/include',
    join(sys.prefix, 'include'),
]

try:
    import numpy
    COMMON_INCLUDE_DIRS.append(numpy.get_include())
except ImportError:
    pass

setup(
    name="magmod",
    description="Earth magnetic field utilities.",
    author="Shi Chen",
    author_email="chenshi80@gmail.com",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Utilities',
    ],
    install_requires=[
        'numpy>=1.13.0',
    ],
    packages=[
        'magmod',
        'magmod.data',
        'magmod.tests',
        'magmod.tests.data',
        'magmod.magnetic_model',
        'magmod.magnetic_model.tests',
        'magmod.magnetic_model.tests.data',
    ],
    license='MIT licence',
    version=magmod.__version__,
    package_data={
        'magmod': [
            'data/*',
            'tests/data/*.tsv',
            'magnetic_model/tests/data/*.txt',
            'magnetic_model/tests/data/*.cdf',
        ],
    },
    ext_modules=[
        Extension(
            'magmod._pymm',
            sources=[
                'magmod/pymm.c',
            ],
            libraries=[],
            library_dirs=[],
            include_dirs=COMMON_INCLUDE_DIRS,
        ),
        Extension(
            'magmod._pysunpos',
            sources=[
                'magmod/pysunpos.c',
            ],
            libraries=[],
            library_dirs=[],
            include_dirs=COMMON_INCLUDE_DIRS,
        ),
        Extension(
            'magmod._pytimeconv',
            sources=[
                'magmod/pytimeconv.c',
            ],
            libraries=[],
            library_dirs=[],
            include_dirs=COMMON_INCLUDE_DIRS,
        ),
    ]
)
