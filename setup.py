#!/usr/bin/env python
"""
django_nymta
======



"""

from setuptools import setup


setup(
    name='django_nymta',
    version='0.0.0',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description="Models for the NYC MTA's website",
    long_description=__doc__,
    py_modules = [
        "wnyc_monitor/__init__",
        "wnyc_monitor/models",
        "wnyc_monitor/tests",
        "wnyc_monitor/views",
        ],
    packages = ["django_nymta"],
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        ],
    scripts = [
        ],
    url = "https://github.com/wnyc/django_nymta",
    install_requires = [
        'django',
        ]
)

