import glob
from setuptools import setup, find_packages

__version__ = open('version.txt').read()

__doc__ = (
    'logging_helper contains logging utilty functions. '
    'See the README file for more information.'
)

setup(
    name = 'logging_helper',
    version = __version__,
    author = 'Fred Loney',
    author_email = 'loneyf@ohsu.edu',
    packages = find_packages(),
    url = 'https://gist.github.com/FredLoney/5454553',
    description = __doc__.split('.', 1)[0],
    long_description = __doc__,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires = []
)
