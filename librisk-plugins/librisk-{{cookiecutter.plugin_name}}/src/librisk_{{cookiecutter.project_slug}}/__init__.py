""" This is the top level module for horizon-{{ cookiecutter.plugin_name }}"""

""" This is not intended as an entry point of the plugin, but as an 
single import point for usefull modules"""

__author__ = """{{ cookiecutter.author_name }}"""
__email__ = """{{ cookiecutter.author_email }}"""

from librisk_{{ cookiecutter.project_slug }}.cli import cli
from librisk_{{ cookiecutter.project_slug }}.man.load_man import AVAILABLE_MAN_PAGES

# If you created templates for this plugin, uncomment this line after you registered the templates
# from librisk_{{ cookiecutter.project_slug }}.template.load_template import AVAILABLE_TEMPLATES

__all__ = ["cli", "AVAILABLE_MAN_PAGES", "AVAILABLE_TEMPLATES"]
