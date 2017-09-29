from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='ansiescapes',
  version='1.0.0',
  description='ANSI escape codes for manipulating the terminal - A Python port of sindresorhus\'s ansi-escapes Node.js module',
  long_description=long_description,
  url='https://github.com/kodie/ansiescapes',
  author='Kodie Grantham',
  author_email='kodie.grantham@gmail.com',
  license='MIT',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
  ],
  keywords='ansi terminal console cli string tty escape escapes formatting shell xterm log logging command-line text vt100 sequence control code codes cursor iterm iterm2',
  py_modules=['ansiescapes']
)
