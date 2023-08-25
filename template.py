import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='cellsegmentation'

list_of_files = [
    ".github/workflows/.gitkeep",# we are creating this for ci/cd deployment so that when we deploy it to github it is automatically deployed to cloud
    "data/.gitkeep",#when we will pass the image in web page , it will be stored in this folder, and then processed from here
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath= Path(filepath)#this makes sure that there arent any problems with backward and forward slash

    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating Directory: {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename}is already created")
        

