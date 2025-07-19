# -*- coding: utf-8 -*-
import re, ast
from setuptools import setup, find_packages

# get version from __version__ variable in woocommerceconnector/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('woocommerceconnector/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)
    ))

with open('requirements.txt') as f:
    install_requires = [r.strip() for r in f if r.strip()]

setup(
    name='woocommerceconnector',
    version=version,
    description='WooCommerce Connector for ERPNext',
    author='libracore',
    author_email='info@libracore.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
