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

# #### 약수 관련 알고리즘 노트

# 약수 관련 노트
# % 를 사용한다
# 개수를 셀 때는 conunt += 1을 이용한다
def solution(left, right):
    count = 0
    answer = 0
    for n in range(left, right+1):
        for num in range(1, right+1):       
            if n%num == 0:# 약수 판별
                count += 1 # 개수 체크
        if count%2 == 0: # 개수가 짝수냐
            answer += n 
            count = 0 # 초기화
        else:
            answer -= n
            count = 0
    return answer


# #### 행렬곱

# +

arr1 = [[1, 4], 
        [3, 2], 
        [4, 1]]
arr2 = [[3, 3], 
        [3, 3]]
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))]for _ in range(len(arr1)) ]
    
    # 이 삼중 for 문이 핵심 아이디어
    for i in range(len(arr1)):
        for j in range(len(arr2[0])): # 이부분
            for k in range(len(arr1[0])): # 이부분
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


# -

# 넘파이 행렬 곱
import numpy as np
arr1 = [[1, 4], 
        [3, 2], 
        [4, 1]]
arr2 = [[3, 3], 
        [3, 3]]
arr1 = np.array(arr1)
arr2 = np.array(arr2)
arr1@arr2


# #### 방금그곡 ( 문자열 라이브러리 )

# +
def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def caltime(musicinfo_): 
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0: 
        total = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    else: 
        total = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])

    return total

def solution(m, musicinfos):
    answer = []
    m = changecode(m)
    for idx, musicinfo in enumerate(musicinfos): 
        musicinfo = changecode(musicinfo)
        musicinfo = musicinfo.split(',')
        time = caltime(musicinfo)

        # 길이가 시간보다 더 긴 경우 
        if len(musicinfo[3]) >= time :
            melody = musicinfo[3][0:time]
        else:             
            # 시간을 계산해서 몫과 나머지로 계산 
            # 다른 사람 풀이 : q, r = divmod(time,len(musicinfo[3]))
            a = time // len(musicinfo[3])
            b = time % len(musicinfo[3])
            melody = musicinfo[3] * a + musicinfo[3][0:b]
        # 노래가 melody에 포함되면 정답후보에 저장 
        if m in melody: 
            answer.append([idx, time, musicinfo[2]])
    # 정답이 있는 경우 
    if len(answer) != 0: 
        # time -> index 기준으로 정렬 
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        return answer[0][2]
    # 정답이 없는 경우
    return "(None)"
