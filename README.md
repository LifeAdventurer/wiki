# Wiki

A documentation site built with MkDocs and Material theme.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Install uv

If you don't have uv installed, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install dependencies

```bash
uv sync
```

### Run the development server

```bash
uv run mkdocs serve
```

### Build the site

```bash
uv run mkdocs build
```

## Development

To install development dependencies:

```bash
uv sync --group dev
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
