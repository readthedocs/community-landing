from __future__ import annotations

from pathlib import Path

from sphinx.application import Sphinx


def _build_html(tmp_path: Path) -> Path:
    project_root = Path(__file__).resolve().parents[1]
    output_dir = tmp_path / "_build" / "html"
    doctree_dir = tmp_path / "_build" / "doctrees"

    app = Sphinx(
        srcdir=str(project_root),
        confdir=str(project_root),
        outdir=str(output_dir),
        doctreedir=str(doctree_dir),
        buildername="html",
        confoverrides={
            "exclude_patterns": ["_build", "README.rst", ".venv", "node_modules"],
        },
        warningiserror=False,
        freshenv=True,
    )
    app.build(force_all=True)
    return output_dir


def test_index_contains_project_cards_and_scripts(tmp_path: Path) -> None:
    output_dir = _build_html(tmp_path)
    index_html = (output_dir / "index.html").read_text(encoding="utf-8")

    assert 'id="docs-projects"' in index_html
    assert "ui three stackable cards" in index_html
    assert "_static/js/jquery-lite.js" in index_html
    assert "_static/js/theme.js" in index_html
    assert "_static/js/data.js" in index_html
    assert "_static/js/readthedocs.js" in index_html


def test_data_js_contains_expected_project_links(tmp_path: Path) -> None:
    output_dir = _build_html(tmp_path)
    data_js = (output_dir / "_static" / "js" / "data.js").read_text(encoding="utf-8")

    assert "readthedocs/readthedocs.org" in data_js
    assert "https://github.com/readthedocs/readthedocs.org" in data_js
    assert "https://docs.readthedocs.com/platform" in data_js
    assert "https://docs.readthedocs.com/dev" in data_js
    assert "'url': '/platform/'" not in data_js
    assert "'url': '/dev/'" not in data_js
