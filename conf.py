"""Read the Docs documentation landing page."""

import re


project = "Read the Docs documentation landing"
slug = re.sub(r"[^\w\s]", "", project)
copyright = "2026, Read the Docs, Inc"
author = "Read the Docs, Inc"

language = "en"
version = "1.0"
release = version

extensions = []

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", "README.rst"]
pygments_style = "sphinx"

html_theme = "landing"
html_theme_path = ["_themes"]
html_theme_options = {
    "description": "Documentation landing page for Read the Docs.",
}
html_additional_pages = {
    "index": "landing.html",
}
html_logo = "_themes/landing/static/img/logo.svg"
html_extra_path = ["_extra"]

html_context = {
    "projects": [
        {
            "name": "Platform documentation",
            "meta": "readthedocs/readthedocs.org",
            "meta_url": "https://github.com/readthedocs/readthedocs.org",
            "description": "Guides, reference, and API docs for Read the Docs.",
            "url": "https://docs.readthedocs.com/platform",
            "versions": [
                {"language": "", "version": "stable"},
            ],
        },
        {
            "name": "Development documentation",
            "meta": "readthedocs/readthedocs.org",
            "meta_url": "https://github.com/readthedocs/readthedocs.org",
            "description": "Developer-focused documentation and internal workflows.",
            "url": "https://docs.readthedocs.com/dev",
            "versions": [
                {"language": "", "version": "latest"},
            ],
        },
    ],
}

# Output formats
htmlhelp_basename = f"{slug}doc"

latex_elements = {}
latex_documents = [(master_doc, f"{slug}.tex", project, author, "manual")]

man_pages = [(master_doc, slug, project, [author], 1)]

texinfo_documents = [
    (master_doc, slug, project, author, slug, project, "Miscellaneous"),
]
