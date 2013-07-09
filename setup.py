import os
from setuptools import setup, find_packages
from surveygizmo import __version__

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='SurveyGizmo',
    version=__version__,
    description='A Python Wrapper for SurveyGizmo\'s restful API service.',
    long_description=README,
    author='Ryan P Kilby',
    author_email='rpkilby@ncsu.edu',
    keywords="Survey Gizmo SurveyGizmo surveygizmo",
    url='https://github.com/rpkilby/SurveyGizmo/',
    packages=find_packages(),
    install_requires=['requests==1.2.3', 'rauth'],
    license='BSD License',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
