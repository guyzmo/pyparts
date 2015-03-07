from setuptools import setup
import os
import sys

if sys.version_info.major != 3:
    raise Exception("Sorry this package only works with python3.")

def read(*names):
    values = dict()
    for name in names:
        if os.path.isfile(name):
            with open(name) as f:
                value = f.read()
        else:
            value = ''
        values[name.split('.')[0]] = value
    return values

long_description = """

{README}

""".format(**read('README.md'))

setup(name='pyparts',
      version='0.3',
      description="Python electronic parts tool",
      long_description=long_description,
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
      url='http://m0g.net',
      license='GPLv3',
      packages=['pyparts'],
      zip_safe=False,
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
""")
