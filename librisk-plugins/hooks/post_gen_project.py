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


def remove_placeholders():
    PLACEHOLDERS_PATHS = [
        os.path.join(root, file) for root, dirs, files in os.walk('.') for file in files if file.startswith('.placeholder')
    ]
    for path in PLACEHOLDERS_PATHS:
        path = path.strip()
        if path and os.path.exists(path) and os.path.isfile(path):
            print(f"Removing placeholder at {path}")
            os.unlink(path)

if __name__ == '__main__':
    remove_placeholders()
    print("Setup complete!")
