import os 
import sys
import yaml
import base64

from cellsegmentation.exception import AppException
from cellsegmentation.logger import logging

def read_yaml_file(filepath:str)-> dict:
    try:
        with open(filepath,'rb') as yaml_file:
            logging.info("read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e
    

def decode_image(imgstring,filename):
    imgdata= base64.b64decode(imgstring)
    with open("./data/"+filename,"wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())
    
#Base64 is a binary-to-text encoding method that converts binary data (such as images, files, or data packets) into a series of printable characters
    