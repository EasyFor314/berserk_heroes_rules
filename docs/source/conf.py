# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Правила Берсерк Герои'
author = 'EasyFor314'

release = '0.1'
version = '0.6.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    "sphinx_inline_tabs",
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "furo"

html_title = "Правила ККИ Берсерк. Герои"
html_theme_options = {
    "prev_next_buttons_location": "both",
    "navigation_with_keys": True,
    "top_of_page_button": None,
    # "announcement": "",
    "light_css_variables": {
        "color-brand-primary": "#336790",  # "blue"
        "color-brand-content": "#336790",
    },
    "dark_css_variables": {
        "color-brand-primary": "#E5B62F",  # "yellow"
        "color-brand-content": "#E5B62F",
    },
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_show_copyright = False
html_show_sphinx = False
