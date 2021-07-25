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

text="Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."


from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import nltk

print(word_tokenize(text))

# ### NLTK 자연어 처리 패키지
# - 교육용으로 개발된 자연어 처리 및 문서 분석용 파이썬 패키지
# - 말뭉치 : 예제 파일 제공
# - 토큰 생성 : 문자열 단위를 토큰(token), 문자열을 토큰으로 나누는 작업
# - 형태소 분석 : 언어학에서 일정한 의미가 있는 가장 작은 말의 단위를 뜻어근, 접두사, 접미사, 품사 등 다양한 언어적 속성으로 파악하고 처리하는 작업
# - 품사 태킹 : 물을 문법적인 기능이나 형태, 뜻에 따라 구분한 것
# - NNP: 단수 고유명사 / VB:동사 / VBP : 동사 현재형
# - TO:to 전치사 / NN : 명사(단수형 혹은 집합형)/ DT: 관형사

pos_tag(word_tokenize(text))

from konlpy.corpus import kolaw
kolaw.fileids()


# ## 한글 형태소 분석(Konlpy)
# #### KoNLPy는 다음과 같은 다양한 형태소 분석, 태깅 라이브러리를 파이썬에서 쉽게 사용할 수 있도록 모아놓았다.
#
# - Hannanum: 한나눔. KAIST Semantic Web Research Center 개발.
#
# - http://semanticweb.kaist.ac.kr/hannanum/
#
# - Kkma: 꼬꼬마. 서울대학교 IDS(Intelligent Data Systems) 연구실 개발.
#
# - http://kkma.snu.ac.kr/
#
# - Komoran: 코모란. Shineware에서 개발.
#
# - https://github.com/shin285/KOMORAN
#
# - Mecab: 메카브. 일본어용 형태소 분석기를 한국어를 사용할 수 있도록 수정.
#
# - https://bitbucket.org/eunjeon/mecab-ko
#
# - Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
#
# - https://github.com/open-korean-text/open-korean-text
#

# ### 자연어 처리 (한글)
# - konlpy 모듈

text = "down 창 회색으로 다 바뀌면 그냥 창끄면 되나요"

# +
from konlpy.tag import Hannanum

han = Hannanum()
han.nouns(text)
# -








