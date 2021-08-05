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

# ####  딥러닝을 위한 텍스트 전처리
# : 용도에 맞게 텍스트를 사전에 처리하는 작업
#
#
# - 토큰화(Tokenization)
# - 정제(Cleaning) and 정규화(Normalization)
#     - 정제(cleaning) : 갖고 있는 코퍼스로부터 노이즈 데이터를 제거
#     - 정규화(Normalization) : 표현 방법이 다른 단어들을 통합시켜서 같은 단어로 만듬
# - 표제어 추출(lemmatization)과 어간 추출(stemming)
#     - 어간(stem) : 단어의 의미를 담고 있는 단어의 핵심 부분
#     - 접사(affix) : 단어에 추가적인 의미를 주는 부분
# - 불용어(stopword)
# - 정규 표현식(Regular Expresiion)
# - 정수 인코딩(Integer Encoding): 텍스트를 숫자로 바꾸는 여러가지 기법(각 단어를 고유한 정수에 맵핑(mapping))
# - 패딩(Padding) : 병렬 연산을 위해서 여러 문장의 길이를 임의로 동일하게 맞춰주는 작업
# - 원-핫 인코딩(One-Hot Encoding) : 자연어 처리에서는 문자를 숫자로 바꾸는 여러가지 기법
# - 데이터의 분리(Splitting Data): 머신 러닝(딥러닝) 모델에 데이터를 훈련시키기 위해서 데이터를 적절히 분리하는 작업

# ### 영어 문장
#
# #### 토큰화(Tokenization)
# - 규칙 1. 하이픈으로 구성된 단어는 하나로 유지한다
# - 규칙 2. doesn't와 같이 어퍼스트로피로 '접어'가 함께하는 단어는 분리해준다

# +
from nltk.tokenize import TreebankWordTokenizer

tokenizer=TreebankWordTokenizer()
text="Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))

# -

# #### 문장 토큰화

from nltk.tokenize import sent_tokenize
text="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print(sent_tokenize(text))


from nltk.tokenize import sent_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))


# ### 한글 문장 토큰화
# #### 한글 토큰화
# - konlpy 모듈 # https://iostream.tistory.com/144 성능비교
#
#     - Kkma, Hannannum, KOMORAN, mecab
#     - morphs : 형태소 추출/ pos : 품사 태킹(Part-of speech tagging) / nouns : 명사추출
# - ckonlpy.Twitter( konlpy는 아님 사전추가)
#

# +
from konlpy.tag import Okt
text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?'

okt = Okt()
okt.pos(text)
# -

print(okt.morphs(text))
print()
print(okt.pos(text))
print()
print(okt.nouns(text))

# +
# #!pip install kss 
# -

# ### 한글 문장 단위로 보기
#
# #### KSS(Korean Sentence Splitter) : 한글 문장 토큰화 도구

# +
import kss

text='딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어려워요. 농담아니에요. 이제 해보면 알걸요?'

print(kss.split_sentences(text))

# -

# ####  한국어 어간 추출
#
# - 언 -----------품사
# - 체언----------명사, 대명사,수사
# - 수식언--------관형사, 부사
# - 관계언--------조사
# - 독립언--------감탄사
# - 용언----------동사, 형용사

# #### 불용어(Stopword) 처리
#
# - 유의미한 단어 토큰만을 선별하기 위해서는 큰 의마가 없는 단어 토큰을 제거하는 작업
# - 한국어 불용어 리스트: https://bab2min.tistory.com/544
#

from nltk.corpus import stopwords  
stopwords.words('english')[:10]
# 영어는 nltk 에서 제공해줌

# +
# 영어 불용어 처리하기
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example)

result = [w for w in word_tokens if w not in stop_words] 

print(word_tokens) 
print(result)


# +
# 한국어 불용어 리스트: https://bab2min.tistory.com/544

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
# 위의 불용어는 명사가 아닌 단어 중에서 저자가 임의로 선정한 것으로 실제 의미있는 선정 기준이 아님
stop_words=stop_words.split(' ')
word_tokens = word_tokenize(example)

result = [w for w in word_tokens if w not in stop_words] 

print(word_tokens) 
print(result)
# -

# ####  정규 표현식(Regular Expression)
#
# - re 모듈
# - [문자] : 대괄호 안의 문자들 중 한 개의 문자와 매치, 예 -> [a-zA-Z가-힣0-9]/ [가나다]
# - [^문자] : 해당 문자를 제외한 문자를 매치
#

# ####  re 모듈에서 지원하는 함수
# - re.sub(정규식, 대체문자, 대상) : 문자열에서 정규 표현식과 일치하는 부분에 대해서 다른 문자열로 대체
# - re.split(정규식, 대상) : 입력된 정규 표현식을 기준으로 문자열들을 분리하여 리스트로 리턴
# - re.findall(정규식, 대상) : 정규 표현식과 매치되는 모든 문자열들을 리스트로 리턴

import re
text="사과 딸기 수박 메론 바나나"
re.split(" ",text)
# text.split(" ") 과 같음


text="""사과
딸기
수박
메론
바나나"""
re.split("\n",text)


# +
text="""이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""  
# \d 모든 숫자를 의마 0-9
print(re.findall("\d+",text))
# # + 가 붙었을때 연속성을 가지는 숫자를 한번에 찾아냄
print()

#숫자 한개한개를 다 뽑아내
print(re.findall('\d',text)) 
print()

# 기호를 제외한 숫자와 문자를 뽑아내
print(re.findall('\w+', text))
print()

# 찾고자 하는 대상에 정규식 표현에 해당하는 데이터가 없다면
# 비어 있는 데이터 출력
print(re.findall('\d+','안녕하세요'))


# +
text='''
정규 표현식 패턴과 일치하는 문자열을 찾아 다른 문자열로 대체. 
Regular expression : A regular expression, regex or regexp[1] 
(sometimes called a rational expression)[2][3] is, 
in theoretical computer science and formal language theory, 
a sequence of characters that define a search pattern. 
'''

#한글 영어 숫자를 남겨 그런데 " "으로 띄어서 남겨 떨어졌으면
print(re.sub('[^가-힣a-zA-Z0-9]'," ", text))
print()

#공백까지 보여줘
print(re.sub('[^가-힣a-zA-Z0-9 ]',"", text))
print()

#그냥 다붙여서 기호빼고 보여줘
print(re.sub('[^가-힣a-zA-Z0-9]',"", text))
print()

#기호만 남겨줘
print(re.sub('[가-힣a-zA-Z0-9 \n\t]',"", text))
print()
# -

# 대문자만 보여줘
re.findall('[A-Z]',text)

# 소문자만 보여줘(하나씩 가져와)
print(re.findall('[a-z]',text))

# 4글자만 뽑아와
re.findall('[가-힣]{4}', text)

#띄어쓰기 전까지 가져와
print(re.findall('[a-z]+', text))


