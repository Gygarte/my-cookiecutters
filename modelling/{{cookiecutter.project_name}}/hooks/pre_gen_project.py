"""This hook validates that if 'as_cli' is not true then
the project should not have scientific dependencies"""

import sys

as_cli = '{{ cookiecutter.as_cli }}'
with_scientific_dependencies = '{{ cookiecutter.with_scientific_dependencies }}'

if not as_cli and with_scientific_dependencies:
    print("Error: Project cannot be a CLI and have scientific dependencies.")
    sys.exit(1)
