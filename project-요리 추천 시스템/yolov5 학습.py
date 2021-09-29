# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + colab={"base_uri": "https://localhost:8080/"} id="TWDbScyWR-vm" executionInfo={"status": "ok", "timestamp": 1632877602081, "user_tz": -540, "elapsed": 534, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="70ad3e9e-fd1b-48dc-ef4f-2e6a46b68a07"
from google.colab import drive
drive.mount('/content/drive')

# + colab={"base_uri": "https://localhost:8080/"} id="r2XTQjmwR9ij" executionInfo={"status": "ok", "timestamp": 1632814094079, "user_tz": -540, "elapsed": 105325, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="252567c8-d5a7-41c0-de7a-103f9673d286"
# !unzip -qq "/content/drive/MyDrive/dataset.zip" -d "/content/drive/MyDrive/"

# + colab={"base_uri": "https://localhost:8080/"} id="KEx15yKwR_cf" executionInfo={"status": "ok", "timestamp": 1632814121636, "user_tz": -540, "elapsed": 382, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="ec0fa42f-bfba-46c3-bbcf-9c4643379834"
# cd /content/drive/MyDrive/yolov5

# + colab={"base_uri": "https://localhost:8080/"} id="GafQN3vvSIZi" executionInfo={"status": "ok", "timestamp": 1632814144160, "user_tz": -540, "elapsed": 3563, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="7ccf17c5-2298-4d39-e141-6154e9f02bcc"
# !pip install -r requirements.txt

# + colab={"base_uri": "https://localhost:8080/"} id="EtDvUEyUSIbc" executionInfo={"status": "ok", "timestamp": 1632833921275, "user_tz": -540, "elapsed": 19697685, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="e1177c30-9b09-4a72-e0dc-bd17f3dac039"
# !python train.py --img 640 --batch 16 --epochs 50 --data /content/drive/MyDrive/yolov5/data/dataset.yaml --cfg /content/drive/MyDrive/yolov5/models/yolov5s.yaml --weights yolov5s.pt --name vetable_yolov5s_results

# + colab={"base_uri": "https://localhost:8080/"} id="J57_1z5bfhzf" executionInfo={"status": "ok", "timestamp": 1632834940566, "user_tz": -540, "elapsed": 9070, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="73678f26-fda0-4134-db07-b3e30c261c26"
# !pip install -r requirements.txt
from IPython.display import Image, clear_output
import torch
import os
 
# !python detect.py --weights  /content/drive/MyDrive/yolov5/runs/train/vetable_yolov5s_results11/weights/best.pt --img 416 --conf 0.5 --source /content/drive/MyDrive/yolov5/inference/images/test1.jpg

# + colab={"base_uri": "https://localhost:8080/"} id="4bYmHMPUhdSp" executionInfo={"status": "ok", "timestamp": 1632835047276, "user_tz": -540, "elapsed": 6002, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="fcdb5b74-c158-4a03-d66b-56308ebadca7"
# !git clone https://github.com/ultralytics/yolov5 yolov5_new  # clone latest

# + colab={"base_uri": "https://localhost:8080/"} id="QToo_gJ7jQQY" executionInfo={"status": "ok", "timestamp": 1632835049480, "user_tz": -540, "elapsed": 238, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="29f9aa60-4115-470f-be18-e276d7986cc0"
# cd yolov5_new

# + colab={"base_uri": "https://localhost:8080/"} id="Hs3gzeAhjQTD" executionInfo={"status": "ok", "timestamp": 1632835403765, "user_tz": -540, "elapsed": 5552, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="da4d2149-6c17-402b-cc2d-1eee654e1f95"
# !python detect.py --weights  /content/drive/MyDrive/yolov5/runs/train/vetable_yolov5s_results11/weights/best.pt --img 416 --conf 0.5 --source /content/drive/MyDrive/images/val/계란2.jpg

# + id="erJxaqoCjQWo"

