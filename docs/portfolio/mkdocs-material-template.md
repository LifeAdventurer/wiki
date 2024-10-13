# A Material for MkDocs Documentation Template

This template uses MkDocs with the Material theme to create elegant, responsive, and well-structured documentation for your projects.

## Getting Started

This repository is a [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
You can create your repository by clicking the `Use this template` button on the upper right corner.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python (version 3.8 or higher)
- Poetry (recommended)
- or pip

## Installation

### Using Poetry (recommended)

1. Clone the repository:
    ```shell
    git clone https://github.com/<username>/<repo-name>.git
    cd <repo-name>
    ```
2. Install dependencies:
    ```shell
    poetry install
    ```
3. Activate the virtual environment:
    ```shell
    poetry shell
    ```

### Using pip

1. Clone the repository:
    ```shell
    git clone https://github.com/<username>/<repo-name>.git
    cd <repo-name>
    ```
2. Create and activate a virtual environment:
    ```shell
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Preview the documentation:
    ```shell
    mkdocs serve
    ```
    Your documentation site will be available at `https://localhost:8000/`.

2. Build the documentation for deployment:
    ```shell
    mkdocs build
    ```
    The static site will be generated in the `site` directory.
3. Deploy to GitHub Pages:
    ```shell
    mkdocs gh-deploy
    ```
    This command will deploy your site to the `gh-pages` branch of your repository and make it available on GitHub Pages.

## Configuration

Configure your documentation by editing the `mkdocs.yml` file. This file contains various settings such as theme, extension, and navigation structure. For more information, refer to the [Material for MkDocs Documentation](https://squidfunk.github.io/mkdocs-material/)

## Acknowledgements

This template is built using the following open-source projects:

- [MkDocs](https://github.com/mkdocs/mkdocs/): A fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
- [Material for MkDocs](https://github.com/squidfunk/mkdocs-material): A Material Design theme for MkDocs, created by Martin Donath (Squidfunk).

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
