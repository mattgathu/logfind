"""
Package setup

"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': ('logfind is a simple commandline tool that allows log files'
                    ' scanning without having to explicitly declare every file on'
                    ' the command line.'),
    'author': 'Matt Gathu',
    'url': 'http://github.com/mattgathu/logfind',
    'download_url': 'download url',
    'author_email': 'mattgathu@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'entry_points': {'console_scripts': ['logfind = logfind.logfind:main']},
    'scripts': [],
    'name': 'logfind',
    'test_suite': 'tests'
}

setup(**config)
