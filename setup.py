'''
Copyright 2022 Airbus SAS
Modifications on 2023/11/02 Copyright 2023 Capgemini

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
# coding: utf-8

from setuptools import setup, find_packages
from datetime import date


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# Read the requirements.in file and extract the required dependencies
with open('requirements.in', 'r') as requirements_file:
    reqs_list = [line.strip() for line in requirements_file if line.strip()]

# Manage module version using date
today = date.today()

# formating the date as yy.mm.dd
version = today.strftime('%y.%m.%d')

setup(
    name='ontology',
    version=version,
    description='Package containing the Ontology data and functions used in SoSTrades project',
    long_description=readme,
    author='Airbus SAS, Capgemini',
    url='https://github.com/os-climate/sostrades-ontology',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=reqs_list,
)
