from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='myapp',
      version=version,
      description="tomasdalmo",
      long_description="""\
tomasdalmo""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='tomasdalmo',
      author='tomas dalmo',
      author_email='tomas.dalmo@scilifelab.se',
      url='https://github.com/tomasdalmo/Tomas',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )