# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import os # 현재 쓰고 있는 운영체제 자체를 의미한다
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = "C:/Windows/Fonts/malgun.ttf" 
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# +
filePath='./subway/'
fileName=os.listdir(filePath) # subway 폴더와 모든 파일 및 하위 폴더 정보를 리스트 형으로 가져와 저장

print(fileName)


# +
def Csv_reset(fn):
    import pandas as pd
    import csv

    f = open('c:/pydata/Data/subway/'+fn, encoding = 'utf-8')
    data = csv.reader(f)

    # '\ufeff"사용일자"', '노선명', '역명', 
    # '승차총승객수', '하차총승객수', '등록일자'
    next(data)
    data_lst=[]

    for row in data:
        data_lst.append(row[0:6])

    df = pd.DataFrame(data_lst, columns= ['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'])
    df.to_csv('c:/pydata/Data/subway/'+fn, encoding = 'cp949', index = False)
    f.close()
    
def file_read():
    filePath='c:/pydata/Data/subway/'
    fileName=os.listdir(filePath) # subway 폴더와 모든 파일 및 하위 폴더 정보를 리스트 형으로 가져와 저장

    df1 = pd.DataFrame()
    df2 = pd.DataFrame()

    for fn in fileName:
        # try/except 예외처리 try에서 error가 발생하면 except 에서 수행해

        try: # 정상코드, 수행
            df2 = pd.read_csv(filePath+fn, encoding = 'cp949')

        except: #try구문에서 에러 발생시, 처리하기 위한 구문
            Csv_reset(fn)
            df2 = pd.read_csv(filePath+fn, encoding = 'cp949')
            
        df1 = pd.concat([df1, df2])
    df1=df1.reset_index(drop=False)
    return df1


# -

df3 = file_read()
print(df3)


# +
def subway_sch(dfdata, subway_name):
    df2=dfdata[dfdata['역명']==subway_name]
    df2 = df2.astype({'승차총승객수': 'int64','사용일자':'str'})
    df2.plot(x='사용일자', y='승차총승객수')
    plt.show()

# def subway_sch(dfdata, subway_name):
#     df2=dfdata[dfdata['역명']==subway_name]
#     df2 = df2.astype({'승차총승객수': 'int64','사용일자':'str'})
#     df2 = df2.groupby('사용일자')['승차총승객수','하차총승객수'].sum()
#     df2.plot()
#     plt.show()


# -

subway_name = input('조회할 역 입력:')
df2 = subway_sch(df3, subway_name)





#
#


#




