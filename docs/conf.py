"""Sphinx configuration."""
project = "Dan"
author = "Danh"
copyright = "2022, Danh"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
