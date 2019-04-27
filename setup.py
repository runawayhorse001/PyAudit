from setuptools import setup, find_packages

try:
    with open("README.md") as f:
        long_description = f.read()
except IOError:
    long_description = ""

try:
    with open("requirements.txt") as f:
        requirements = [x.strip() for x in f.read().splitlines() if x.strip()]
except IOError:
    requirements = []

setup(name='PyAudit',
	  install_requires=requirements,
      version='1.0',
      description='Python Data Audit library',
      author='Wenqiang Feng and Ming Chen',
      author_email='von198@gmail.com',
      url='https://github.com/runawayhorse001/PyAudit.git',
      packages=find_packages(),
      long_description=long_description
     )