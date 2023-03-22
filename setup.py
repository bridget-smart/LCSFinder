# setup.py

from distutils.core import setup, Extension


lcs_module = Extension('_LCSFinder', sources=['LCSFinder_wrap.cxx', 'LCSFinder.cpp'], extra_compile_args=['-std=c++11'])

setup(name='LCSFinder', 
      ext_modules=[lcs_module], 
      py_modules=["LCSFinder"])