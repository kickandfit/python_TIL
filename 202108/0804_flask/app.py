from flask import Flask, render_template, url_for, request
from flask_ngrok import run_with_ngrok   # https://ngrok.com/docs
from werkzeug.utils import secure_filename
import os
import urllib3
import json
import base64
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import time

## 플라스크 인스턴스 생성
app=Flask(__name__)
run_with_ngrok(app)


def search_object(fn, fdir):  # AI API로 객체 정보와 정보에 따른 범위를 그려주고 이미지를 저장

    openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
    accessKey = "fdf16766-d73d-48be-a4b3-c03276a6cfb2"  # 개인 인증키
    imageFilePath = fdir + fn  +".jpg"# 대상 이미지
    type = "jpg"

    file = open(imageFilePath, "rb")
    imageContents = base64.b64encode(file.read()).decode("utf8")
    file.close()

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "type": type,
            "file": imageContents
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    json_data = json.loads(response.data)
    prn_data = json_data['return_object']

    df1 = pd.DataFrame(prn_data['data'])

    np.array(prn_data['data'], dtype='str')

    df1 = df1.astype({'confidence': 'float', 'x': int, 'y': int, 'width': int, 'height': int})

    img = Image.open(fdir + fn + '.jpg')
    draw = ImageDraw.Draw(img)

    for i in range(len(df1)):
        x = df1.iloc[i, 2]
        y = df1.iloc[i, 3]
        w = df1.iloc[i, 4]
        h = df1.iloc[i, 5]

        if df1.iloc[i, 0] == 'person':
            color = (255, 0, 0)
        elif df1.iloc[i, 0] == 'car':
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        draw.line([(x, y), (x, y + h), (x + w, y + h), (x + w, y), (x, y)], fill=color, width=2)
        draw.text((x, y - 15), df1.iloc[i, 0], fill='red')

    img.save('./static/img/' + fn + 'fix.jpg')   # urllib.quote()
    return fn + 'fix.jpg'


## 메인 홈페이지 접속
@app.route("/", methods=['GET'])
def index_main_loading():
    return render_template("index.html")


## 파일 업로드 및 분석후 출력
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        fname=file.filename
        file.save(os.path.join("static/img/", fname))
        time.sleep(10)

        fn = file.filename[:-4]
        fdir="./static/img/"
        fn=search_object(fn, fdir)

        f_name = os.path.join("/img/", fn)
        return render_template('index.html', f_name=f_name)

if __name__ == "__main__":
    app.run()

