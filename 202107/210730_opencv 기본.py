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

# ### Open CV
# - OpenCV(Open Source Computer Vision)은 오픈소스 컴퓨터 비전 라이브러리
# - OpenCV는 단일 이미지나 동영상의 이미지를 원하는 결과를 분석 및 추출하기위한 API
# - 객체, 얼굴, 행동, 인식, 독순, 모션 추척 등의 응용 프로그램에서 사용
# - 사이트: https://docs.opencv.org/4.2.0/d1/dfb/intro.html
#

import cv2
cv2.__version__

# +
cap_img=cv2.VideoCapture(0) # 사용중인 PC에 연결된 웹캠 또는 카메라 영상 연결
cap_img.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # capture.set(option, n), 카메라 속성을 설정
cap_img.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # option: 프레임의 너비와 높이등의 속성을 설정

# 영상 출력을 위한 캡처 화면 반복
while True:
    ret, frame = cap_img.read() #카메라의 상태 및 프레이,ret은 카메라 상태 저장(정상작동 True)
    cv2.imshow('VideoFrame', frame) #cv2.imshow('윈도우 창 제목', 이미지)
    if cv2.waitKey(1)>0: # 키보드의 아무키나 누르면 종료시켜라
        break
cap_img.release() #카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows()#cv2.destroyAllWindows('윈도우 창 제목') 특정 윈도우 창만 닫을 수 있음
# -

# #### 카메라 영상을 파일로 저장
#
# - XVID 코덱 사용()
# - 파일의 확장자 mp4, avi 등

# +
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_cap=cv2.VideoWriter("./data/out_video_1.mp4", fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1 ) # 1은 좌우반전, 0은 상하반전
        out_cap.write(frame)
        
        cv2.imshow('Save_Frame', frame)
        if cv2.waitKey>0:break
        else:braek

cap.release()
out_cap.release()
cv2.destroyAllWindows()
# -

# #### OpenCV를 이용한 동영상 캡처 및 녹화
# - 키값별 숫자: ESC(27), Ctrl+Z(26), Ctrl+C(3), Ctrl+X(24)
#

# +
import datetime
import cv2

cap = cv2.VideoCapture("./data/backkpink.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False #녹화 유/무 설정

while True:
    if (cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT)):
        cap.open("./data/backkpink.mp4")
    
    ret, frame = cap.read()
    cv2.imshow('Backkpink', frame)
    
    now = datetime.datetime.now().strftime('%d_%H-%M-%S')
    key = cv2.waitKey(24) #33ms마다 갱신
    
    if key == 27:
        break
    elif key ==26:
        
        cv2.imwrite('./data/backkpink_'+now+'.png',frame)
        print("캡처완료")
        
    elif key == 18:
        print('녹화시작')
        record = True # 녹화 중으로 변경
        video=cv2.VideoWriter("./data/backkpink_"+str(now)+".mp4", fourcc, 20.0, frame.shape[0])
    elif key == 24:
        print('녹화 중지')
        record = False # 녹화 중지로 변경
        video.release()
        
        
    if record ==True:
        print('녹화중')
        video.write(frame)
        
cap.release()
cv2.destroyAllWindows()

        
# -

# ####  웹캠에서 사람 얼굴 인지하기
# - 다운로드 링크
# https://github.com/opencv/opencv/tree/master/data/haarcascades
#

# +
import numpy as np
import cv2
face_case = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # 좌우 대칭
    faces = face_case.detectMultiScale(frame, #대상 이미지
                                       scaleFactor = 1.05,#이미지에서 얼굴 크기가 서로 다른 것을 보상해주는 값
                                       minNeighbors = 5) # 얼굴 사이에 있는 픽셀 수
    
    if len(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('faces', frame)
    if cv2.waitKey(24)==27:break
    

cap.release()
cv2.destroyAllWindows()
# -










