import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

project_name="hate"

list_of_files = [
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_transformation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_evaluation.py',
    f'{project_name}/components/model_pusher.py',
    f'{project_name}/configuration/gcloud_syncer.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifact_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/train_pipeline.py',
    f'{project_name}/pipeline/predict_pipeline.py',
    f'{project_name}/ml/__init__.py',
    f'{project_name}/ml/model.py',
    'app.py',
    'demo.py',
    'requirements.txt',
    'Dockerfile',
    'setup.py',
    '.dockerignore',
    

    
    
    ]


for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    if not os.path.exists(filedir):
        os.makedirs(filedir)
        logging.info(f"Creating directory: {filedir}")
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")