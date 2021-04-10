
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='testgen',
    version='0.2.2',
    description='Auto generate templates for unit tests based on source code',
    python_requires='==3.*,>=3.6.0',
    project_urls={"repository": "https://github.com/ryanchao2012/testgen"},
    author='ryanchao2012',
    author_email='ryanchao2012@gmail.com',
    license='MIT',
    entry_points={"console_scripts": ["testgen = testgen.cli.main:main"]},
    packages=['examples.my_awesome_package', 'examples.mytests', 'examples.mytests.my_awesome_package', 'testgen', 'testgen.cli'],
    package_dir={"": "src"},
    package_data={},
    install_requires=['click==7.*,>=7.1.2'],
    extras_require={"dev": ["black==20.*,>=20.8.0.b1", "flake8==3.*,>=3.9.0", "invoke==1.*,>=1.5.0", "ipython==6.*,>=6.0.0", "pytest==6.*,>=6.2.2", "pytest-cov==2.*,>=2.11.1"]},
)
