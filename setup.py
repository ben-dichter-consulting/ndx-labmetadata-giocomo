# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from shutil import copy2


# Get the long description from the README file
with open('README.md', 'r') as f:
    long_description = f.read()

# Get requirements
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup_args = dict(
    name='ndx-labmetadata-giocomo',
    version='0.1.0',
    description='NWB extension for storing metadata for Giocomo lab',
    author='Luiz Tauffer, Szonja Weigl and Ben Dichter',
    author_email='ben.dichter@gmail.com',
    url='https://github.com/catalystneuro/ndx-labmetadata-giocomo',
    packages=find_packages('src/pynwb'),
    package_dir={'': 'src/pynwb'},
    include_package_data=True,
    package_data={'ndx_labmetadata_giocomo': ['spec/ndx-labmetadata-giocomo.namespace.yaml',
                                              'spec/ndx-labmetadata-giocomo.extensions.yaml']},
    classifiers=["Intended Audience :: Developers",
                 "Intended Audience :: Science/Research"],
    zip_safe=False,
    install_requires=install_requires,
)


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-labmetadata-giocomo.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-labmetadata-giocomo.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx_labmetadata_giocomo', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)
