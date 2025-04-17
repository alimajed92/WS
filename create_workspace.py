import os
import logging
import subprocess
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def print_welcome():
    box_width = 55
    border = "═" * box_width
    print(f"╔{border}╗")
    print("║{:^55}║".format("🚀 Welcome to the Project Workspace Creator!"))
    print("║{:^55}║".format("This script will help you set up a new project."))
    print(f"╠{border}╣")
    print("║{:^55}║".format("Available project types:"))
    print("║{:^55}║".format("de      → Data Engineering"))
    print("║{:^55}║".format("ds      → Data Science"))
    print("║{:^55}║".format("ml      → Machine Learning"))
    print("║{:^55}║".format("gen_ai  → Generative AI"))
    print(f"╚{border}╝\n")


def run_uv_init(project_name):
    if not os.path.exists(project_name):
        subprocess.run(["uv", "init", project_name], check=True)
        logging.info(f"`uv init` completed for {project_name}")
    else:
        logging.warning(
            f"Directory '{project_name}' already exists. Skipping `uv init`."
        )


def create_virtualenv(project_name):
    cwd = os.getcwd()
    os.chdir(project_name)
    subprocess.run(["uv", "venv"], check=True)
    logging.info(f"Virtual environment created in {project_name}/.venv")
    os.chdir(cwd)


def create_env_files(project_name):
    env_path = os.path.join(project_name, ".env")
    env_example_path = os.path.join(project_name, "env.example")

    with open(env_path, "w") as f:
        f.write("# Local environment variables\n")

    with open(env_example_path, "w") as f:
        f.write("# Example environment variables\nAPI_KEY=\nDB_HOST=\nDB_PORT=\n")

    logging.info("Created .env and env.example")


def create_ignore_files(project_name):
    gitignore_path = os.path.join(project_name, ".gitignore")
    dockerignore_path = os.path.join(project_name, ".dockerignore")

    with open(gitignore_path, "w") as f:
        f.write(
            """\
__pycache__/
*.py[cod]
.venv/
.env
*.log
.ipynb_checkpoints/
.DS_Store
.vscode/
"""
        )

    with open(dockerignore_path, "w") as f:
        f.write(
            """\
__pycache__/
*.py[cod]
*.log
.venv/
.env
.ipynb_checkpoints/
.vscode/
.DS_Store
tests/
notebooks/
"""
        )

    logging.info("Created .gitignore and .dockerignore")


def create_license_file(project_name, author="Your Name"):
    year = datetime.now().year
    license_text = f"""\
MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in     
all copies or substantial portions of the Software.                            

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN      
THE SOFTWARE.
"""
    license_path = os.path.join(project_name, "LICENSE")
    with open(license_path, "w") as f:
        f.write(license_text)
    logging.info("Created LICENSE file (MIT)")


def create_extra_files(project_name, project_type):
    pkg_path = os.path.join(project_name, "src", project_name)

    files = [
        f"{pkg_path}/__init__.py",
        f"{pkg_path}/main.py",
        f"{pkg_path}/utils.py",
        f"{pkg_path}/config.py",
        f"{pkg_path}/logger/__init__.py",
        f"{pkg_path}/logger/logger.py",
        f"{pkg_path}/exceptions/__init__.py",
        f"{pkg_path}/exceptions/exceptions.py",
        f"{project_name}/run.py",
        f"{project_name}/notebooks/.gitkeep",
        f"{project_name}/data/.gitkeep",
        f"{project_name}/models/.gitkeep",
        f"{project_name}/tests/__init__.py",
        f"{project_name}/docs/.gitkeep",
        f"{project_name}/logs/.gitkeep",
        f"{project_name}/Dockerfile",
    ]

    type_specific = {
        "de": [
            f"{pkg_path}/etl_pipeline.py",
            f"{pkg_path}/data_processing.py",
            f"{project_name}/tests/test_etl.py",
            f"{project_name}/docs/etl_documentation.md",
        ],
        "ds": [
            f"{pkg_path}/data_preprocessing.py",
            f"{pkg_path}/model_training.py",
            f"{project_name}/notebooks/eda.ipynb",
            f"{project_name}/tests/test_model.py",
            f"{project_name}/docs/data_science_guide.md",
        ],
        "ml": [
            f"{pkg_path}/training.py",
            f"{pkg_path}/inference.py",
            f"{project_name}/notebooks/model_experiment.ipynb",
            f"{project_name}/tests/test_training.py",
            f"{project_name}/docs/ml_documentation.md",
        ],
        "gen_ai": [
            f"{pkg_path}/generative_model.py",
            f"{pkg_path}/training.py",
            f"{pkg_path}/inference.py",
            f"{project_name}/notebooks/gen_ai_experiment.ipynb",
            f"{project_name}/tests/test_generative.py",
            f"{project_name}/docs/gen_ai_documentation.md",
        ],
    }

    files.extend(type_specific.get(project_type, []))

    for filepath in files:
        full_path = Path(filepath)
        os.makedirs(full_path.parent, exist_ok=True)
        if not full_path.exists():
            full_path.write_text("")
    logging.info("Project-specific files created successfully.")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print_welcome()
    project_type = input("Enter project type (de, ds, ml, gen_ai): ").strip().lower()
    project_name = input("Enter project name: ").strip()
    author_name = input("Enter author name for LICENSE file: ").strip()

    if project_type not in {"de", "ds", "ml", "gen_ai"}:
        print("❌ Invalid project type! Choose from: de, ds, ml, gen_ai.")
        exit(1)

    run_uv_init(project_name)
    create_virtualenv(project_name)
    create_env_files(project_name)
    create_ignore_files(project_name)
    create_license_file(project_name, author=author_name)
    create_extra_files(project_name, project_type)

    logging.info(
        f"✅ Workspace for {project_type.upper()} project '{project_name}' created successfully."
    )
