#!/bin/python
from distutils.core import setup
setup(name='foo',
      version="1.0",
      author="sam",
      author_email="local@local.com",
      url="http://1.1.1.1",
      py_modules=['hello'],
      setup_requires=['pbr>=1.8', 
                      'python>=3.7'],
      requires=['pbr', 'python'],
      package_dir={'':'foo1'}, # foo1 is the base
      packages=['foo'],  # foo1/foo
     )
