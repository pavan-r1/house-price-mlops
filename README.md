# House Price Prediction MLOps

An end-to-end Machine Learning Operations (MLOps) project for predicting house prices using machine learning, with API serving, Docker containerization, data version control, and automated CI/CD using GitHub Actions.

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Training the Model](#training-the-model)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [DVC Setup](#dvc-setup)
- [CI/CD Pipeline](#cicd-pipeline)
- [Testing](#testing)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Project Overview

House Price Prediction MLOps demonstrates how a machine learning application can be developed, packaged, tested, and prepared for deployment using modern MLOps practices.

The system uses housing-related features to estimate property prices. A trained machine learning model can be exposed through a REST API, allowing users or other applications to submit property information and receive a predicted price.

The project brings together machine learning development and software engineering practices to improve reproducibility, maintainability, and deployment consistency.

**Note:** Actual prediction performance depends on the dataset, feature selection, model configuration, and evaluation results.

## Objectives

- Develop a machine learning model for house price prediction.
- Organize training and application code into maintainable modules.
- Provide predictions through a REST API.
- Package the application using Docker.
- Use DVC for data and model-pipeline versioning where configured.
- Automate build and validation steps using GitHub Actions.
- Establish a reproducible workflow for future model improvements.

## Key Features

- **Machine Learning:** Predicts house prices from supported property features.
- **REST API:** Makes model predictions available through HTTP requests.
- **Docker:** Packages the application and its dependencies into a container.
- **DVC:** Supports reproducible data and pipeline management when configured.
- **GitHub Actions:** Automates workflow execution on repository events.
- **Modular Structure:** Separates application code from model-training code.
- **Scalable Foundation:** Can be extended with monitoring, model tracking, and cloud deployment.

## System Architecture

```text
Housing Dataset
      |
      v
Data Preprocessing
      |
      v
Feature Engineering
      |
      v
Model Training and Evaluation
      |
      v
Trained Model Artifact
      |
      v
FastAPI Prediction Service
      |
      v
Docker Container
      |
      v
Deployment Environment
```

GitHub Actions can automate relevant checks and Docker image builds whenever changes are pushed to the repository.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| FastAPI | REST API development |
| Uvicorn | ASGI server |
| Docker | Application containerization |
| DVC | Dataset and pipeline versioning |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI/CD workflow automation |
| Pytest | Automated testing, if configured |

The actual dependencies should match the packages and tools implemented in the repository.

## Project Structure

The following is a suggested structure. Adjust it to match the files that actually exist in your repository.

```text
house-price-mlops/
├── .github/
│   └── workflows/
│       └── docker-image.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── src/
│   ├── train.py
│   └── ...
├── data/
│   └── ...
├── models/
│   └── ...
├── tests/
│   └── ...
├── .gitignore
├── Dockerfile
├── dvc.yaml
├── requirements.txt
└── README.md
```

- `app/`: API application and prediction endpoints.
- `src/`: Training, preprocessing, and supporting scripts.
- `data/`: Dataset files, if stored locally.
- `models/`: Saved model artifacts, if stored locally.
- `.github/workflows/`: GitHub Actions workflow definitions.
- `Dockerfile`: Instructions for building the container image.
- `dvc.yaml`: DVC pipeline stages, when configured.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

Large datasets and model artifacts should be managed according to the repository's storage strategy rather than committed indiscriminately.

## Prerequisites

Install the following tools before running the project:

1. Python 3.10 or later, compatible with the selected dependencies.
2. Git.
3. Docker Desktop or Docker Engine.
4. A GitHub account.
5. DVC, if using DVC-based data or pipeline versioning.

Verify your installations:

```bash
python --version
git --version
docker --version
dvc --version
```

The DVC command is required only if DVC is installed.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pavan-r1/house-price-mlops.git
cd house-price-mlops
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks environment activation, use the appropriate execution-policy configuration for your system or invoke the environment's Python executable directly.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the dataset and model

Place the dataset in the location expected by the training code. Confirm that the configured input columns, target column, and file paths match the actual dataset.

If the project requires a pre-trained model, ensure that the expected model artifact is available before starting the API.

## Training the Model

If the repository contains `src/train.py`, run:

```bash
python src/train.py
```

The training process should perform the steps implemented by the project, such as:

1. Loading the dataset.
2. Validating the input data.
3. Preprocessing the features.
4. Splitting the data into training and validation sets.
5. Training the selected regression model.
6. Evaluating model performance.
7. Saving the trained model and preprocessing artifacts.

Typical regression metrics include:

- **MAE:** Mean Absolute Error.
- **MSE:** Mean Squared Error.
- **RMSE:** Root Mean Squared Error.
- **R²:** Coefficient of determination.

Use the metrics actually calculated by your implementation. Do not assume model accuracy or performance values before running the evaluation.

## Running the API

If your FastAPI entry point is `app/main.py` and the FastAPI application object is named `app`, start the server with:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open the interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

These URLs work when the API is running locally and the application exposes the corresponding documentation routes.

**Important:** Update the Uvicorn module path if your actual API entry point or application variable has a different name.

## API Endpoints

The following endpoints are examples of a typical FastAPI prediction service. They are not guaranteed to exist until implemented in the application.

| Method | Example endpoint | Purpose |
|---|---|---|
| GET | `/` | Application information or health response |
| GET | `/health` | Health check |
| POST | `/predict` | Predict a house price |

### Example prediction request

The request fields must match the input schema defined in the API.

```json
{
  "area": 1500,
  "bedrooms": 3,
  "bathrooms": 2
}
```

The above JSON is illustrative only. Replace the fields with the actual features supported by the trained model.

### Example prediction response

```json
{
  "predicted_price": 7500000
}
```

This response is illustrative, not a verified output from the project. The predicted price and its units depend on the trained model and dataset.

## Docker Setup

Docker allows the application to run in a consistent environment without requiring all Python dependencies to be installed directly on the host machine.

### 1. Build the image

From the directory containing the Dockerfile:

```bash
docker build -t house-price-api:latest .
```

### 2. Run the container

```bash
docker run --rm -p 8000:8000 house-price-api:latest
```

### 3. Test the API

Open:

http://localhost:8000/docs

### 4. Inspect running containers

```bash
docker ps
```

### 5. Stop a running container

If you started the container in detached mode, find its name or ID and run:

```bash
docker stop <container_name_or_id>
```

The Docker image build depends on a valid, non-empty Dockerfile, a correct API entry point, and the required application files.

## DVC Setup

DVC (Data Version Control) helps track datasets and machine learning pipeline stages without requiring large data files to be committed directly to Git.

### 1. Initialize DVC

If DVC has not already been initialized:

```bash
dvc init
```

Do not run initialization again in an already initialized repository unless you understand the effect on its existing configuration.

### 2. Track a dataset

For example, if the dataset is stored at `data/housing.csv`:

```bash
dvc add data/housing.csv
```

This generates a `.dvc` metadata file and updates `.gitignore` to exclude the tracked data file from ordinary Git commits.

### 3. Configure a remote

A DVC remote must be configured before pushing data to remote storage. For example, a local directory can be used for basic testing:

```bash
dvc remote add -d localstorage ../dvc-storage
```

This local remote is suitable only for testing on the same machine or an appropriately shared filesystem. For team collaboration, configure an accessible shared storage provider.

### 4. Save DVC metadata

```bash
git add data/housing.csv.dvc .gitignore .dvc/config
git commit -m "Track housing dataset with DVC"
```

If the paths differ in your repository, stage the files that actually exist.

### 5. Run the pipeline

If `dvc.yaml` contains valid stages:

```bash
dvc repro
```

A DVC pipeline must define its commands, dependencies, outputs, and any required parameters. An empty `dvc.yaml` does not define a runnable pipeline.

## CI/CD Pipeline

GitHub Actions automates selected tasks when code is pushed or a pull request is opened.

A typical pipeline can include:

1. Checking out the source code.
2. Setting up Python or Docker Buildx.
3. Installing dependencies or preparing the Docker build.
4. Running automated tests, if configured.
5. Building the Docker image.
6. Pushing the image to a container registry, if registry authentication and push configuration are set up.

The workflow is defined in `.github/workflows/`.

### Verify a workflow run

1. Open the GitHub repository.
2. Select the **Actions** tab.
3. Open the latest workflow run.
4. Review the individual job logs.
5. Fix any failed step and push a new commit.

A successful Docker image build does not automatically mean that the image was pushed to a registry or that the application was deployed. Those actions require additional workflow configuration.

## Testing

Run the tests that are implemented in the project.

If the repository uses Pytest and contains a test suite:

```bash
pytest -v
```

Useful validation checks include:

- Dataset loading and validation.
- Feature preprocessing.
- Model training and artifact saving.
- Prediction output format.
- API input validation and error handling.
- Docker image build.
- API startup and health checks.

Only report tests as passed after executing them successfully.

## Environment Variables

Store credentials and environment-specific configuration in environment variables instead of hardcoding secrets in source code.

For local development, you may use a `.env` file if the application is configured to load it. Add `.env` to `.gitignore` and provide a sanitized `.env.example` when required.

Example placeholder:

```env
MODEL_PATH=models/house_price_model.pkl
```

This variable is only useful if the application reads `MODEL_PATH`. Adjust the variable name and model path to match the actual code.

Never commit API keys, passwords, access tokens, or production credentials to GitHub.

## Troubleshooting

### Docker error: `The Dockerfile cannot be empty`

**Cause:** Docker cannot build an image from an empty Dockerfile.

**Solution:** Add valid Docker instructions, save the file, and rerun:

```bash
docker build -t house-price-api:latest .
```

### Error: `ModuleNotFoundError`

**Cause:** A required Python package may be missing from the environment.

**Solution:**

```bash
pip install -r requirements.txt
```

If the error persists, add the missing dependency to `requirements.txt` with a compatible version.

### Error: `Could not import module`

**Cause:** The Uvicorn module path may not match the actual Python file or FastAPI object name.

**Solution:** Check the location of the entry-point file and use the correct module path.

### API cannot load the model

**Cause:** The model artifact may not exist at the configured path or may not have been included in the container.

**Solution:** Train the model, configure the correct artifact path, and ensure that the required file is available during the Docker build or runtime.

### GitHub Actions Docker build succeeds but no image is available

**Cause:** The workflow may build the image without pushing it to a registry.

**Solution:** Configure image tagging, registry authentication, and a push-enabled build step if a published image is required.

### DVC cannot reproduce the pipeline

**Cause:** The DVC pipeline may be missing stages, dependencies, outputs, or required input data.

**Solution:** Verify `dvc.yaml`, the dataset paths, and the commands used by each stage.

## Future Improvements

- Add systematic data validation and preprocessing checks.
- Compare multiple regression algorithms.
- Track experiments and metrics using MLflow.
- Add unit tests and API integration tests.
- Configure DVC remote storage for team collaboration.
- Publish versioned Docker images to a container registry.
- Deploy the API to a cloud hosting platform.
- Add prediction logging, monitoring, and data-drift detection.
- Introduce automated model retraining and validation.

## Author

**Pavan R.**

B.E. in Data Science  
T. John Institute of Technology, Bengaluru

GitHub: https://github.com/pavan-r1

## License

Choose and add an appropriate open-source license if you intend to distribute this project publicly. Until a license is added, do not assume that others have permission to reuse or redistribute the code.

---

*This project is intended for educational and demonstration purposes. Predicted property values are estimates produced by the trained model and should not be treated as professional property valuations.*
