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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "SmidgeBit"
copyright = "2022, Ben Wart"
author = "Ben Wart"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_gitstamp",
    "ablog",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- GitStamp Options --------------------------------------------------------

gitstamp_fmt = "%b %d, %Y"

# -- ABlog Options -----------------------------------------------------------

blog_path = "archive"
blog_title = "SmidgeBit"
blog_baseurl = "blog.smidgebit.com"
blog_authors = {
    "Ben": ("Ben Wart", "https://github.com/benwart"),
}
blog_default_author = "Ben"
post_auto_excerpt = 1
post_auto_image = 1
post_show_prev_next = True
blog_feed_fulltext = True
blog_feed_length = 10

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_logo = "_static/logo.png"

html_theme_options = {
    "favicons": [
        {
            "rel": "icon",
            "href": "favicon.svg",
        },
    ]
}

html_sidebars = {
    "**": [
        "postcard.html",
        "recentposts.html",
        "archives.html",
    ],
}
