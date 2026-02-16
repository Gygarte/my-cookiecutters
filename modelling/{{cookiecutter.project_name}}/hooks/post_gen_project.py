"""This hook performs post_init proceses as:
    1. Cleans up the project directory if the project is not a CLI
    2. Install scientific dependencies if required"""


import os
import pip
import sys
import subprocess


# Implementation of part 1
REMOVE_PATHS = [
    '{% if cookiecutter.as_cli != true %}src/{% endif %}',
    '{% if cookiecutter.as_cli != true %}tests/{% endif %}',
    '{% if cookiecutter.as_cli != true %}pyproject.toml{% endif %}'
]



for path in REMOVE_PATHS:
    path = path.strip()
    if path in os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

# Implementation of part 2
as_cli = '{{ cookiecutter.as_cli }}'
with_scientific_deps = '{{ cookiecutter.with_scientific_dependencies }}'

default_packages = ['numpy', 'pandas', 'scipy', 'matplotlib', 'seaborn', 'polars', 'click', 'rich', 'statsmodels']

if as_cli and with_scientific_deps == 'true':
    subprocess.check_call(
        [
            sys.executable,
            '-m',
            'pip',
            'install',
            *default_packages
        ]
    )

    # Also generate a requirements.txt file
    subprocess.check_call(
        [
            sys.executable,
            '-m',
            'pip',
            'freeze',
            '>',
            'requirements.txt'
        ]
    )
