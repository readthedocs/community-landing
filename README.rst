Read the Docs landing documentation
===================================

This repository hosts the documentation landing page for
``docs.readthedocs.com`` and the metadata files used by crawlers and LLMs
(``llms.txt``, ``robots.txt``, ``sitemap.xml``).

Building
--------

Install Python requirements:

.. code:: console

    uv pip install -r requirements.txt

Build the docs with:

.. code:: console

    make clean html

If you need to rebuild the landing assets, use:

.. code:: console

    npm run build
