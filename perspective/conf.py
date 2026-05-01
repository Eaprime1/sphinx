from __future__ import annotations

project = 'Perspective'
author = 'Perspective Project'
copyright = '2026, Perspective Project'
version = '0.1'
release = '0.1'

extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
]

source_suffix = {
    '.md': 'myst',
    '.rst': 'restructuredtext',
}

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'fieldlist',
]

exclude_patterns = ['_build', 'play/**', '.DS_Store']

# HTML output
html_theme = 'furo'
html_title = 'Perspective'
html_theme_options = {
    'sidebar_hide_name': False,
}

# LaTeX / PDF output
latex_documents = [
    ('index', 'perspective.tex', 'Perspective Documentation', author, 'manual'),
]
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
}

# ePub output
epub_show_urls = 'footnote'
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

autosectionlabel_prefix_document = True
