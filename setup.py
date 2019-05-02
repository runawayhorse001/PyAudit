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
      version='1.0.3',
      description='Python Data Audit library',
      author='Wenqiang Feng and Ming Chen',
      author_email='von198@gmail.com',
      url='https://github.com/runawayhorse001/PyAudit.git',
      packages=find_packages(),
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="MIT",
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Operating System :: MacOS',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      include_package_data=True
     )