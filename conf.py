"""Read the Docs documentation landing page."""

import re


def build_project(
    *,
    name: str,
    meta: str,
    meta_url: str,
    description: str,
    url: str,
    versions: list[dict],
) -> dict:
    base_url = url.rstrip("/")
    rendered_versions = []
    for version in versions:
        language = version.get("language", "")
        version_name = version.get("version", "latest")
        parts = [base_url]
        if language:
            parts.append(language)
        parts.append(version_name)
        rendered_versions.append(
            {
                "language": language,
                "version": version_name,
                "url": "/".join(parts) + "/",
                "show_language": bool(language and language != "en"),
            }
        )
    return {
        "name": name,
        "meta": meta,
        "meta_url": meta_url,
        "description": description,
        "url": url,
        "versions": rendered_versions,
        "topics": [],
    }


project = "Read the Docs"
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
exclude_patterns = ["_build", ".venv", "README.rst"]
pygments_style = "sphinx"

html_theme = "landing"
html_theme_path = ["_themes"]
html_theme_options = {
    "description": "Documentation landing page and metadata.",
}
html_additional_pages = {
    "index": "landing.html",
}
html_logo = "_themes/landing/static/img/logo.svg"
html_extra_path = ["_extra"]

html_context = {
    "projects": [
        build_project(
            name="Platform documentation",
            meta="readthedocs/readthedocs.org",
            meta_url="https://github.com/readthedocs/readthedocs.org",
            description="Guides, reference, and API docs for Read the Docs.",
            url="https://docs.readthedocs.com/platform",
            versions=[
                {"language": "", "version": "stable"},
            ],
        ),
        build_project(
            name="Development documentation",
            meta="readthedocs/readthedocs.org",
            meta_url="https://github.com/readthedocs/readthedocs.org",
            description="Developer-focused documentation and internal workflows.",
            url="https://docs.readthedocs.com/dev",
            versions=[
                {"language": "", "version": "latest"},
            ],
        ),
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
