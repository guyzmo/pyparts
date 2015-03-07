from setuptools import setup
from subprocess import call
import os
import sys

if sys.version_info.major != 3:
    raise Exception("Sorry this package only works with python3.")

setup(name='pyparts',
      version='0.5',
      description="Python electronic parts tool",
      long_description_markdown_filename='README.md',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Development Status :: 4 - Beta',
          'License :: OSI Approved',
          'Operating System :: Unix',
      ],
      keywords='download tv show',
      author='Bernard `Guyzmo` Pratz',
      author_email='pyparts@m0g.net',
      url='https://github.com/guyzmo/pyparts',
      license='GPLv3',
      packages=['pyparts'],
      zip_safe=False,
      setup_requires=['setuptools-markdown'],
      install_requires=[
          'pyparts',
          'pyoctopart',
          'docopt',
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pyparts = pyparts.parts:main
      """,
      )

if "install" in sys.argv:
    print("""
Python parts commandline utility installed!

To start using it, call:

    pyparts help

""")
