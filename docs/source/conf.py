# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

import apitele
from datetime import datetime as dtm

author = 'geko1'
year = dtm.now().year
release = apitele.VERSION
project = apitele.__name__
copyright = f'{year}, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.duration']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_type_aliases = {} # to change type-aliases

autodoc_preserve_defaults = True # to preserve default arguments value
autodoc_typehints = 'description' # 'none'
autodoc_typehints_format = 'short'
toc_object_entries = True # if False, it doesn't index members

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo' #'sphinx_rtd_theme' # 'alabaster'
html_static_path = ['_static']
html_theme_options = {
    'light_logo': 'robot_light.png',
    'dark_logo': 'robot_dark.png',
    #'navigation_with_keys': True
}
