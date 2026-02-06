from importlib import resurces

AVAILABLE_MAN_PAGES = {
     """{{cookiecutter.plugin_name}}""":resource.files("__main__") / "man" / {{cookiecutter.plugin_name}}
