from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='Dalmo',
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
      scripts=['scripts/getting_data.py','scripts/check_repo.py','Dalmo/session4.py'],
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
