import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'python-box',
    'logzero',
    'requests',
    'maya',
    'click',
    'tablib',
    ]

tests_require = [
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='grpf',
      version='0.1',
      description='Gibson Ridge Placefile library for python',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Module"
      ],
      author='Stephan M Ellis',
      author_email='stephan.ellis@gmail.com',
      url='',
      keywords='gibson ridge placefiles parser generator',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [console_scripts]
      grpf=grpf.cli:cli
      """,
      )
