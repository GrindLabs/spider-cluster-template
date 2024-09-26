from pkg_resources import resource_filename
import json


def schema_path(name: str) -> str:
    return resource_filename("{{cookiecutter.project_slug}}", f"schemas/{name}.json")


def load_schema(name: str) -> dict:
    with open(schema_path(name)) as f:
        schema = json.load(f)
    return schema
