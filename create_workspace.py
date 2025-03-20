import os
import logging
from pathlib import Path
import subprocess

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_files(file_list):
    """Helper function to create directories and files."""
    for path in file_list:
        filepath = Path(path)
        filedir, filename = os.path.split(filepath)

        # Create directories if they do not exist
        if filedir:
            os.makedirs(filedir, exist_ok=True)

        # Create files only if they do not exist or are empty
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                f.write("")

    logging.info(f"Successfully created {len(file_list)} files and directories.")


def create_virtualenv(project_name):
    """Create a virtual environment inside the project directory."""
    venv_path = os.path.join(project_name, "venv")
    if not os.path.exists(venv_path):
        subprocess.run(["python", "-m", "venv", venv_path])
        print(f"Virtual environment created at {venv_path}.")
    else:
        print("Virtual environment already exists.")


def de_create_workspace(project_name):
    """Creates a workspace for a Data Engineering project."""
    list_of_files = [
        f"{project_name}/src/__init__.py",
        f"{project_name}/src/main.py",
        f"{project_name}/src/utils.py",
        f"{project_name}/src/etl_pipeline.py",
        f"{project_name}/src/data_processing.py",
        f"{project_name}/src/config.py",
        f"{project_name}/tests/test_etl.py",
        f"{project_name}/data/raw_data.csv",
        f"{project_name}/data/processed_data.csv",
        f"{project_name}/logs/pipeline.log",
        f"{project_name}/docs/etl_documentation.md",
        f"{project_name}/exceptions/__init__.py",
        f"{project_name}/exceptions/exceptions.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/logger/logger.py",
        f"{project_name}/README.md",
        f"{project_name}/requirements/requirements.txt",
        f"{project_name}/.gitignore",
        f"{project_name}/Dockerfile",
        f"{project_name}/setup.py",
        f"{project_name}/run.py",
    ]
    create_files(list_of_files)


def ds_create_workspace(project_name):
    """Creates a workspace for a Data Science project."""
    list_of_files = [
        f"{project_name}/src/__init__.py",
        f"{project_name}/src/main.py",
        f"{project_name}/src/utils.py",
        f"{project_name}/src/data_preprocessing.py",
        f"{project_name}/src/model_training.py",
        f"{project_name}/src/config.py",
        f"{project_name}/tests/test_model.py",
        f"{project_name}/data/raw_data.csv",
        f"{project_name}/data/cleaned_data.csv",
        f"{project_name}/models/model.pkl",
        f"{project_name}/notebooks/eda.ipynb",
        f"{project_name}/logs/training.log",
        f"{project_name}/docs/data_science_guide.md",
        f"{project_name}/exceptions/__init__.py",
        f"{project_name}/exceptions/exceptions.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/logger/logger.py",
        f"{project_name}/README.md",
        f"{project_name}/requirements/requirements.txt",
        f"{project_name}/.gitignore",
        f"{project_name}/Dockerfile",
        f"{project_name}/setup.py",
        f"{project_name}/run.py",
    ]
    create_files(list_of_files)


def ml_create_workspace(project_name):
    """Creates a workspace for a Machine Learning project."""
    list_of_files = [
        f"{project_name}/src/__init__.py",
        f"{project_name}/src/main.py",
        f"{project_name}/src/utils.py",
        f"{project_name}/src/training.py",
        f"{project_name}/src/inference.py",
        f"{project_name}/src/config.py",
        f"{project_name}/models/model.h5",
        f"{project_name}/tests/test_training.py",
        f"{project_name}/notebooks/model_experiment.ipynb",
        f"{project_name}/logs/training.log",
        f"{project_name}/docs/ml_documentation.md",
        f"{project_name}/exceptions/__init__.py",
        f"{project_name}/exceptions/exceptions.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/logger/logger.py",
        f"{project_name}/README.md",
        f"{project_name}/requirements/requirements.txt",
        f"{project_name}/.gitignore",
        f"{project_name}/Dockerfile",
        f"{project_name}/setup.py",
        f"{project_name}/run.py",
    ]
    create_files(list_of_files)


def gen_ai_create_workspace(project_name):
    """Creates a workspace for a Generative AI project."""
    list_of_files = [
        f"{project_name}/src/__init__.py",
        f"{project_name}/src/main.py",
        f"{project_name}/src/utils.py",
        f"{project_name}/src/generative_model.py",
        f"{project_name}/src/training.py",
        f"{project_name}/src/inference.py",
        f"{project_name}/src/config.py",
        f"{project_name}/models/gan_model.pth",
        f"{project_name}/tests/test_generative.py",
        f"{project_name}/notebooks/gen_ai_experiment.ipynb",
        f"{project_name}/logs/training.log",
        f"{project_name}/docs/gen_ai_documentation.md",
        f"{project_name}/exceptions/__init__.py",
        f"{project_name}/exceptions/exceptions.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/logger/logger.py",
        f"{project_name}/requirements/requirements.txt",
        f"{project_name}/README.md",
        f"{project_name}/.gitignore",
        f"{project_name}/Dockerfile",
        f"{project_name}/setup.py",
        f"{project_name}/run.py",
    ]
    create_files(list_of_files)


# Example usage
if __name__ == "__main__":
    project_type = input("Enter project type (de, ds, ml, gen_ai): ").strip().lower()
    project_name = input("Enter project name: ").strip()

    if project_type == "de":
        de_create_workspace(project_name)
        create_virtualenv(project_name)
    elif project_type == "ds":
        ds_create_workspace(project_name)
        create_virtualenv(project_name)
    elif project_type == "ml":
        ml_create_workspace(project_name)
        create_virtualenv(project_name)
    elif project_type == "gen_ai":
        gen_ai_create_workspace(project_name)
        create_virtualenv(project_name)
    else:
        print("Invalid project type! Choose from: de, ds, ml, gen_ai.")

    logging.info(
        f"Workspace for {project_type.upper()} project '{project_name}' has been created successfully!"
    )
