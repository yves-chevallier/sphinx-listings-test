# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Sphinx Listings'
copyright = '2020, Nowox'
author = 'Nowox'

sys.path.append(os.path.abspath("./_ext"))
extensions = [
    'listings'
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']

# To support unicode chars
latex_engine = 'xelatex'
latex_elements = {
    'babel': r'\usepackage[english]{babel}',
    'preamble': open('_templates/preamble.tex').read()
}
