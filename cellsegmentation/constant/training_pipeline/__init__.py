ARTIFACTS_DIR :str ='artifacts'#main folder

DATA_INGESTION_DIR_NAME:str ='data_ingestion'

DATA_INGESTION_FEATURE_STORE_DIR:str ='feature_store'#this will contain the unziped file

DATA_DOWNLOAD_URL:str ='https://drive.google.com/file/d/12td791izDSn8XDN2AW9ZL_4a8-uSKigl/view?usp=drive_link'


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov8s-seg.pt"

MODEL_TRAINER_NO_EPOCHS: int = 30


