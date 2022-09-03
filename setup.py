from setuptools import find_packages
from setuptools import setup


version = "1.0.0"

setup(
    author='Bastien Bo',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    description='A simple library for payment card validation, revived from the dead',
    name='pycard_reborn',
    packages=find_packages(),
    url='https://github.com/Bastien-BO/pycard_reborn',
    version=version,
)
