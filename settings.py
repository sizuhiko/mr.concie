#!/usr/bin/env python

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ASSISTANT_APP_NAME= os.environ.get("ASSISTANT_APP_NAME")
TTS_LANG= os.environ.get("TTS_LANG")
ASSISTANT_LANGUAGE_CODE= os.environ.get("ASSISTANT_LANGUAGE_CODE")
ASSISTANT_APP_INTERACTION= os.environ.get("ASSISTANT_APP_INTERACTION")
DEVICE_ID= os.environ.get("DEVICE_ID")
DEVICE_MODEL_ID= os.environ.get("DEVICE_MODEL_ID")
VOLUME= int(os.environ.get("VOLUME"))
