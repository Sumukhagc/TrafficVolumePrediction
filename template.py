import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "TrafficVolumePrediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
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
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]
for file in list_of_files:
    path=Path(file)
    dir_name,filename=os.path.split(file)
    if dir_name!="":
        os.makedirs(dir_name,exist_ok=True)
        logging.info("Directory created at {}".format(dir_name))

    if (not os.path.exists(file) or os.path.getsize(file)==0):
        with open(file,"w") as f:
            logging.info("File created at path {}".format(file))
    
    else:
        logging.info("File already exists")