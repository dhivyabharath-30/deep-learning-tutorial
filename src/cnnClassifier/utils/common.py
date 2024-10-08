import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  """read yaml file and return

    Args:
      path_to_yaml (str): path like input
      
    Raises:
      ValueError: if yaml file is empty
      e: empty file

    Returns:
      ConfigBox: ConfigBox type
  """
  try:
    with open(path_to_yaml) as yaml_file:
      content = yaml.safe_load(yaml_file)
      logger.info(f"yaml file: {path_to_yaml} loaded successfully")
      return ConfigBox(content)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
    raise e


def decodeImage(imgstring, fileName):
  imgdata = base64.b64decode(imgstring)
  with open(fileName,'wb') as f:
    f.write(imgdata)
    f.close
    
def encodeImageIntoBase64(croppedImagePath):
  with open(croppedImagePath,"rb") as f:
    return base64.b64encode(f.read())
      