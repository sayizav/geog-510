# AI Coding Guidelines for GEOG-510

## Project Overview
This repository contains the source for "Geographic Software Design" (GEOG-510), a university course website built with Jupyter Book. It teaches Python programming for geospatial analysis using libraries like geemap, leafmap, and rasterio.

## Architecture
- **Content Structure**: All book content lives in `book/` with subdirectories for sections (about/, geospatial/, labs/, python/, software/).
- **File Pairing**: Each chapter has paired `.ipynb` (Jupyter notebook) and `.myst` (MyST markdown) files synced via jupytext.
- **Build System**: Uses Jupyter Book for static site generation, configured in `_config.yml` and `_toc.yml`.

## Key Workflows
- **Sync Notebooks**: After editing a `.ipynb` file, run `jupytext --to myst <filename>.ipynb` to update the paired `.myst` file.
- **Build Book**: Run `jupyter-book build book/` from the root directory to generate the site in `book/_build/html/`.
- **Serve Locally**: Run `jupyter-book serve book/_build/html/` to preview the site at http://localhost:8000.
- **Environment Setup**: Use pixi or venv; install dependencies with `pip install -r requirements.txt`.

## Conventions
- **Execution**: Notebooks in `book/geospatial/` are excluded from build-time execution (see `_config.yml` exclude_patterns) due to data dependencies or interactivity.
- **Formatting**: Use MyST markdown syntax for book content; avoid raw HTML.
- **Numbering**: Python and Geospatial sections use numbered chapters (configured in `_toc.yml`).
- **Labs**: Assignments in `book/labs/` are student deliverables; maintain as-is unless updating course content.

## Examples
- To add a new geospatial library demo: Create paired files in `book/geospatial/`, add to `_toc.yml`, and ensure it's excluded from execution if interactive.
- For Python basics: Follow the pattern in `book/python/` with explanatory text in `.myst` and executable code in `.ipynb`.

## Dependencies
- Core: jupyter-book, jupytext
- Geospatial: geemap, leafmap, geopandas, rasterio, etc. (see requirements.txt)

Focus on maintaining the educational flow and technical accuracy for students.