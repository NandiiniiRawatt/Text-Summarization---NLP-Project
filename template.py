import os
from pathlib import Path
import logging
from xmlrpc.server import list_public_methods     # to log all the information

logging.basicConfig(level=logging.INFO, format='[%asctime]; %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",             # .github help in deployment of CI/Cd ML files; gitkeep creats a hidden file (empty)
    f"src/{project_name}/__init__.py",        #  to create local package/file, you need to create a constructor file (__init__.py)
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"            # create a notebook
]


for filepath in list_of_files:          # to handel paths 
    filepath = Path(filepath)           # give all the paths one by one  
    filedir, filename = os.path.split(filepath)

    if filedir != "":                                          #folder creation
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists!")



