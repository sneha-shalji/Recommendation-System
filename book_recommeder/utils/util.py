import yaml
import sys
from book_recommeder.exception.exception_handler import AppException



def read_yaml_files(file_path: str) -> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e
    

    