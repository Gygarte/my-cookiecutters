"""This hook performs post_init proceses as:
    1. Cleans up the project directory if the project is not a CLI
    2. Install scientific dependencies if required"""


import os
import sys
import subprocess
import shutil

if sys.version_info > (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata



def remove_cli_dirs():
    REMOVE_PATHS = [
        '{% if cookiecutter.as_cli != true %}src/{% endif %}',
        '{% if cookiecutter.as_cli != true %}tests/{% endif %}',
        '{% if cookiecutter.as_cli != true %}pyproject.toml{% endif %}',
        '{% if cookiecutter.as_cli != true %}MANIFEST.in{% endif %}',
    ]
    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            print(f"Removing {path}")
            try:
                os.unlink(path) if os.path.isfile(path) else os.removedirs(path)
            except OSError as e:
                print(f"Error removing {path}: {e}")
                shutil.rmtree(path, ignore_errors=True)


def install_scientific_deps():

    default_packages = ['numpy', 'pandas', 'scipy', 'matplotlib', 'seaborn', 'polars', 'click', 'rich', 'statsmodels']
    as_cli = {{ cookiecutter.as_cli}}
    with_scientific_deps = {{ cookiecutter.with_scientific_dependencies}}

    if as_cli and with_scientific_deps:
        print('Installing basic scientific dependencies')
        subprocess.run(
            [
                sys.executable,
                '-m',
                'pip',
                'install',
                *default_packages
            ],
            check=True
        )

        # Also generate a requirements.txt file
        print("Generating requirements.txt")
        with open("requirements.txt", "w") as file:
            for dist in importlib_metadata.distributions():
                name = dist.metadata["Name"]
                version = dist.version
                file.write(f"{name}=={version}\n")

        if os.path.exists('requirements.txt'):
            print('requirements.txt file generated')
        else:
            print('requirements.txt file not generated')
            sys.exit(1)

if __name__ == '__main__':
    remove_cli_dirs()
    install_scientific_deps()
    print("Setup complete!")
