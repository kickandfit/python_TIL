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

# +
# 데이터 조회
import cx_Oracle

conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
cs = conn.cursor()
rs = cs.execute("select * from sign")

for record in rs:
    print(record[0])
    
cs.close()
conn.close()

# +
#데이터 추가 및 방송 송출 ( 조회, 삭제, 추가)
import cx_Oracle

#데이터 받아오고
# 이부분에 detect.py 코드부분에서 찾아와야함


data = input() # 그 데이터를 data 에 넣어야함
cnt = 0 # 몇 프레임을 기준으로 할 것인가 cnt로 체크함
if data == 'without_helmet':
    conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
    cs = conn.cursor()
    sql = "insert into sign (sign_wo) values (:1)"
    cs.execute(sql,('1'))
    cs.close()
    conn.commit()
    conn.close()
    

conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
cs = conn.cursor()
rs = cs.execute("select * from sign")

for record in rs:
    if record[0] == 1:
        cnt += 1
        print('헬멧 미착용자 탐지, 헬멧 착용 장려 방송을 송출합니다')
        
        # 라즈베리파이 연동 부분 코딩


print(cs.rowcount) 
cs.close()
conn.close()

# 방송이 송출되었다면 0, 아니면 1을 보냄
# 방송이 송출되지 않았다면 방송이 송출될 때까지 1을 보냄
data_1 = int(input())
if data_1 == 0:
    conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
    cs = conn.cursor()
    sql = "delete from sign where sign_wo=1"
    cs.execute(sql)
    rs = cs.execute("select * from sign")
    for record in rs:
        print(record[0])
    print(cs.rowcount) 
    cs.close()
    conn.commit()
    conn.close()
    cnt = 0
# 이부분 수정해야함
else:
    conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
    cs = conn.cursor()
    rs = cs.execute("select * from sign")
    for record in rs:
        print(record[0])
    print(cs.rowcount)   
    cs.close()
    conn.commit()
    conn.close()
# -

import time
import cv2
import torch
import torch.backends.cudnn as cudnn
import numpy as np
import cx_Oracle
from numpy import random
from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import check_img_size, check_requirements, non_max_suppression, scale_coords
from utils.torch_utils import select_device, time_sync

# # MVP ( detect 시 객체 검출 하자마자 데이터 베이스에서 신호 보내기 )

# +
SOURCE = 'C:/Users/moh12/Desktop/runs/test/*.jpg'
WEIGHTS = 'C:/Users/moh12/Desktop/runs/train/yolo_helmet_detections_1/weights/best.pt'
IMG_SIZE = 640
DEVICE = ''
AUGMENT = False
CONF_THRES = 0.25
IOU_THRES = 0.45
CLASSES = None
AGNOSTIC_NMS = False

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
    
    # Load video
    
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
#     print('pred :', pred)
#     print('det :', det)
    s = ''
    s += '%gx%g ' % img.shape[2:]  # print string

    if len(det):
        # Rescale boxes from img_size to img0 size
        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

        # Print results
        for c in det[:, -1].unique():
            
            n = (det[:, -1] == c).sum()  # detections per class
            s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "
#             print(f"{names[int(c)]}", f"{n}",f"{c}") #{names[int(c)]} 이름 , n 이 수
            data = names[int(c)]
            print('data :',data)
            if data == 'without_helmet':
                conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
                cs = conn.cursor()
                sql = "insert into sign (sign_wo) values (:1)"
                cs.execute(sql,('1'))
                cs.close()
                conn.commit()
                conn.close()


                conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
                cs = conn.cursor()
                rs = cs.execute("select * from sign")

                for record in rs:
                    if record[0] == 1:

                        print('헬멧 미착용자 탐지, 헬멧 착용 장려 방송을 송출합니다')
                        print(f'{n} 명이 헬멧을 착용하지 않았습니다.')
                        # if 몇 프레임을 기준으로 할지 정해야함.
                        
                        sign = 1
                        if sign == 1:
                            # 라즈베리파이 연동 부분 코딩
                            
                            conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
                            cs = conn.cursor()
                            sql = "delete from sign where sign_wo=1"
                            cs.execute(sql)
                            rs = cs.execute("select * from sign")
                        
                            print('현재 데이터 베이스 행 수 : ', cs.rowcount) 
                            cnt = 0
                            print('방송을 송출 했습니다.')
                            cs.close()
                            conn.commit()
                            conn.close()
                            cnt = 0
                        # 이부분 수정해야함
                        else:
                            conn = cx_Oracle.connect('system/1234@localhost:1521/xe')
                            cs = conn.cursor()
                            rs = cs.execute("select * from sign")
                            for record in rs:
                                print(record[0])
                            print(cs.rowcount)
                            print('탐지 오차일 확률이 높습니다.')
                            cs.close()
                            conn.commit()
                            conn.close()
                            

                    


#                 print(cs.rowcount) 
#                 cs.close()
#                 conn.close()
#     print(det[-1][-1])
    print(s)

# +
if __name__ == '__main__':
    check_requirements(exclude=('pycocotools', 'thop'))
    with torch.no_grad():
            detect()

 # Read video
# self.mode = 'video'
# ret_val, img0 = self.cap.read()
# if not ret_val:
#     self.count += 1
#     self.cap.release()
#         if self.count == self.nf:  # last video
#             raise StopIteration
#         else:
#             path = self.files[self.count]
#             self.new_video(path)
#             ret_val, img0 = self.cap.read()

#     self.frame += 1
#     print(f'video {self.count + 1}/{self.nf} ({self.frame}/{self.frames}) {path}: ', end='')
# -



# # 영상 처리시 기본 구현 코드 ( 활용하진 않을 것 )

# +
# 비디오 읽기
cap = cv2.VideoCapture(path)
frame = 0
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    
    ret_val, img0 = cap.read()

    if not ret_val:
        cap.release()
    
    frame += 1
    print(f'video ({self.frame}/{self.frames}) {path}: ', end='')

