import os
from pathlib import Path
import logging

#logging info
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s] : %(message)s:')

#project name
project_name = "text_summarization"

#list of all files required
list_of_files = [
    ".github/workflows/.gitkeep", #required for CI/CD deployment
    f"src/{project_name}/__init__.py", #constructor
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", #contains all utilities
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", #contains model related parameters
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" #notebook experiments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #separates and retrns file directory(folders) and the files in it

    #check if filedir is empty
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
