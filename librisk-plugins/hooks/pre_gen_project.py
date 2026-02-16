"""This hook validates that if 'as_cli' is not true then
the project should not have scientific dependencies"""

import sys
import warnings

as_cli = {{ cookiecutter.as_cli }}
with_scientific_dependencies = {{ cookiecutter.install_scientific_dependencies }}

if not as_cli and with_scientific_dependencies:
    warnings.warn(
        Warning("Project will install scientific dependencies in the global scope.")
    )
