# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'MTH 448/548'
copyright = '2020, Bernard Badzioch'
author = 'Bernard Badzioch'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx_copybutton',
    #'sphinxcontrib.srclinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'RUBRICS']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css', 
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Don't add .txt suffix to source files:
html_sourcelink_suffix = ''

# Work-around until https://github.com/sphinx-doc/sphinx/issues/4229 is solved:
html_scaled_image_link = True #False

# Show source files

#html_show_sourcelink =  False #True
#srclink_project = 'https://github.com/MTH548'
#srclink_branch = 'master'
#srclink_src_path = '/'

# View on GitHub setup
html_context = {
"display_github": True, # Add 'Edit on Github' link instead of 'View page source'
"commit": False,
#'source_url_prefix': "https://github.com/MTH548",
"github_host": "github.com",
"github_user": "MTH548",
"github_repo": 'MTH548_site',
"theme_vcs_pageview_mode" : 'blob',
"github_version": "master/sources/",
"github_version2": "master/",
}

github_url = 'https://github.com/MTH548'

# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 200}",
]


# Environment variables to be passed to the kernel:
#os.environ['MY_DUMMY_VARIABLE'] = 'Hello from conf.py!'

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'