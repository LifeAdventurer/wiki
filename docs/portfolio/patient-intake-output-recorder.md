<h1 align="center">Patient Intake/Output (I/O) Recorder</h1>

<hr>

<h4 align="center">
  <a href="https://lifeadventurer.github.io/patient-intake-output-recorder/getting-started/#installation">Install</a>
  ·
  <a href="https://lifeadventurer.github.io/patient-intake-output-recorder/getting-started/#configuration">Configure</a>
  ·
  <a href="https://lifeadventurer.github.io/patient-intake-output-recorder">Docs</a>
</h4>

This project is a simple tool for recording and tracking essential health
parameters of patients. It provides a user-friendly interface for healthcare
professionals to log various health metrics, including food intake, water
consumption, urine volume, defecation frequency, and weight, along with
corresponding timestamps for each entry. This information can be valuable for
healthcare professionals to monitor and analyze the health status of patients
over time.

Uses [Poetry](https://github.com/python-poetry/poetry) for dependency management
and includes, ruff and pre-commit for linting and formatting.

## Importance for Kidney Disease Management

In particular, it plays a crucial role in managing conditions such as kidney
disease, where strict control over water intake is essential for maintaining
health and preventing complications.

## Getting Started

This guide will walk you through setting up the Patient Intake/Output Recorder
(PIOR) project. Follow the steps below to install dependencies, configure
settings, and start the server.

### Installation

#### Install Dependencies

Patient Intake Output Recorder can be set up with either Poetry (recommended) or
pip. Open a terminal in the project directory and install the dependencies:

=== "Using Poetry"

    ```sh
    poetry install
    ```

=== "Using pip"

    ```sh
    pip install -r requirements.txt
    ```

!!! Note

    Poetry is recommended as it simplifies version management and ensures
    reproducible builds.

### Configuration

#### Backend

1. In the `backend` directory, create a new `config.json` file.
2. Replace `{your_token_here}` and `{your_api_url_here}` with your actual token
   and API URL.

**Example content:**

```json title="backend/config.json"
{
  "token": "{your_token_here}",
  "api_url": "{your_api_url_here}"
}
```

#### Frontend (Patient)

1. In the `patient` directory, create a new `config.json` file.
2. Replace `{your_api_url_here}` with your actual API URL.

**Example content:**

```json title="patient/config.json"
{
  "apiUrl": "{your_api_url_here}"
}
```

#### Frontend (Monitor)

1. In the `monitor` directory, create a new `config.json` file.
2. Replace `{your_api_url_here}` and `{your_web_url_here}` with your actual API
   URL and web URL.

**Example content:**

```json title="monitor/config.json"
{
  "apiUrl": "{your_api_url_here}",
  "webUrl": "{your_web_url_here}"
}
```

### Running the server

Once installed and configured, you can start the server with Uvicorn.

=== "Using Poetry"

    ```sh
    poetry run uvicorn main:app --reload
    ```

=== "Using Python"

    ```sh
    python -m uvicorn main:app --reload
    ```

This command launches the server with hot-reloading enabled, which automatically
restarts the server upon code changes. With these steps completed, your server
should be up and running, ready to handle requests.

## Want to Contribute?

Refer to
[CONTRIBUTING.md](https://github.com/LifeAdventurer/patient-intake-output-recorder/blob/main/CONTRIBUTING.md)

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).
See the
[LICENSE](https://github.com/LifeAdventurer/patient-intake-output-recorder/blob/main/LICENSE)
for more information.
