from setuptools import setup,Extension

setup(ext_modules=[Extension("gcd",["c/gcd.c"])])
