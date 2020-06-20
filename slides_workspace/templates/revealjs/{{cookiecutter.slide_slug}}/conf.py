# -- Path setup --------------------------------------------------------------

# -- Prepared proc -----------------------------------------------------------

# -- Project information -----------------------------------------------------
project = ""
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"

# The full version, including alpha/beta/rc tags
release = "{% now 'local', '%Y' %}"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_revealjs",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_includes"]
