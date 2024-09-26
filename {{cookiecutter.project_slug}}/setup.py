from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.project_slug}}",
    url="{{cookiecutter.project_url}}",
    version="{{cookiecutter.project_version}}",
    description="{{cookiecutter.project_description}}",
    author="{{cookiecutter.project_author}}",
    author_email="{{cookiecutter.project_author_email}}",
    packages=find_packages(),
    package_data={
        "": [
            "schemas/*.json",
        ],
    },
    entry_points={
        "scrapy": [
            "settings = {{cookiecutter.project_slug}}.settings",
        ],
    },
    python_requires=">={{cookiecutter.python_min_version}}",
)
