from setuptools import find_packages, setup

setup(
    name         = '{{cookiecutter.project_slug}}',
    version      = '1.0.0',
    packages     = find_packages(),
    package_data = {'': ['.env', '*.yaml']},
    entry_points = {'scrapy': ['settings = {{cookiecutter.project_slug}}.settings']},
)
