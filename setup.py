"""Setup file which make distribution."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='meta',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['meta = core:main']
    },
)
