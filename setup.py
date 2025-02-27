from setuptools import setup,Extension

setup(ext_modules=[Extension("num",["c/num.c"])])
