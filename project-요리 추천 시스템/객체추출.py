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

# + colab={"base_uri": "https://localhost:8080/"} id="nrDCzAGXQhHx" executionInfo={"status": "ok", "timestamp": 1632880564388, "user_tz": -540, "elapsed": 345, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="e656076d-ead5-4380-e3d7-31726e25e3f4"
# cd /content/drive/My Drive/yolov5/yolov5_new

# + colab={"base_uri": "https://localhost:8080/"} id="yy8PBzDGQued" executionInfo={"status": "ok", "timestamp": 1632890546820, "user_tz": -540, "elapsed": 3414, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="2a0fb02e-fcce-4de4-c1f3-ed177deac354"
# !python detect.py --weights /content/drive/MyDrive/yolov5/runs/train/vetable_yolov5s_results11/weights/best.pt --img 416 --conf 0.5 --source /content/drive/MyDrive/yolov5/inference/images/test6.jpg

# + id="6W1S30wUQugw" executionInfo={"status": "ok", "timestamp": 1632889082275, "user_tz": -540, "elapsed": 360, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}}
import torch
model = torch.load('/content/drive/MyDrive/yolov5/runs/train/vetable_yolov5s_results11/weights/best.pt')

# + id="LwoklUWrQulR" executionInfo={"status": "ok", "timestamp": 1632890993735, "user_tz": -540, "elapsed": 392, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}}
import time
import cv2
import torch
import torch.backends.cudnn as cudnn
import numpy as np

from numpy import random
from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import check_img_size, check_requirements, non_max_suppression, scale_coords
from utils.torch_utils import select_device, time_sync

# + id="xgL015pb4dEE" executionInfo={"status": "ok", "timestamp": 1632891292652, "user_tz": -540, "elapsed": 470, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}}
SOURCE = '/content/drive/MyDrive/yolov5/inference/images/test8.jpg'
WEIGHTS = '/content/drive/MyDrive/yolov5/runs/train/vetable_yolov5s_results11/weights/best.pt'
IMG_SIZE = 640
DEVICE = ''
AUGMENT = False
CONF_THRES = 0.25
IOU_THRES = 0.45
CLASSES = None
AGNOSTIC_NMS = False


# + id="f-SthX5o4dL7" executionInfo={"status": "ok", "timestamp": 1632891555811, "user_tz": -540, "elapsed": 482, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}}
def detect():
    source, weights, imgsz = SOURCE, WEIGHTS, IMG_SIZE

    # Initialize
    device = select_device(DEVICE)
    half = device.type != 'cpu'  # half precision only supported on CUDA
    print('device:', device)

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    if half:
        model.half()  # to FP16

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once

    # Load image
    img0 = cv2.imread(source)  # BGR
    assert img0 is not None, 'Image Not Found ' + source

    # Padded resize
    img = letterbox(img0, imgsz, stride=stride)[0]

    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    t0 = time_sync()
    pred = model(img, augment=AUGMENT)[0]
    print('pred shape:', pred.shape)

    # Apply NMS
    pred = non_max_suppression(pred, CONF_THRES, IOU_THRES, classes=CLASSES, agnostic=AGNOSTIC_NMS)

    # Process detections
    det = pred[0]
    print('det shape:', det.shape)

    s = ''
    s += '%gx%g ' % img.shape[2:]  # print string

    if len(det):
        # Rescale boxes from img_size to img0 size
        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

        # Print results
        for c in det[:, -1].unique():
            n = (det[:, -1] == c).sum()  # detections per class
            s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "

    print(det[-1][-1])
    print(s)


# + colab={"base_uri": "https://localhost:8080/"} id="FgP-u0Lv4dOH" executionInfo={"status": "ok", "timestamp": 1632891559446, "user_tz": -540, "elapsed": 3638, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}} outputId="1358b304-e6f1-44ec-a4e5-03ad0af295e8"
if __name__ == '__main__':
    check_requirements(exclude=('pycocotools', 'thop'))
    with torch.no_grad():
            detect()

# + id="PXuUaEaI4dQo" executionInfo={"status": "ok", "timestamp": 1632891298000, "user_tz": -540, "elapsed": 6, "user": {"displayName": "\ubc15\ubbfc\ud76c", "photoUrl": "https://lh3.googleusercontent.com/a/default-user=s64", "userId": "06441363839827045067"}}

