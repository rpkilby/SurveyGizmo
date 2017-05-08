import os
import unittest
from setuptools import setup, find_packages

PATH = os.path.join(os.path.dirname(__file__), 'README.md')

try:
    import pypandoc
    README = pypandoc.convert(PATH, 'rst')
except ImportError:
    README = open(PATH).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name='SurveyGizmo',
    version='1.2.2',
    description='A Python Wrapper for SurveyGizmo\'s restful API service.',
    long_description=README,
    author='Ryan P Kilby',
    author_email='rpkilby@ncsu.edu',
    keywords="Survey Gizmo SurveyGizmo surveygizmo",
    url='https://github.com/ITNG/SurveyGizmo/',
    packages=find_packages(),
    install_requires=['requests'],
    test_suite='setup.test_suite',
    license='BSD License',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
