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

# #### 단어의 빈도수 계산하기
#
# - counter 사용
# - 계수 정렬과 같은 메모리 비효율성을 초래할 수  있음
# ( 희소 행렬 문제 )
# - 단어 별로 체킹함으로 문장 단위에서 의미가 무시되는 단점

# ####  정수 인코딩(integer Encoding)
#
# - Bag of Word(BOW)
#

# #### 람다(lambda)식
#
#
# lambda 인자 : 표현식
#
# - def aa(x,y) : return x + y
#     - aa(10,20)
#
# - 람다로 표현하기
#     - (lambda x, y : x+y)(10,20)

# #### Out -of -Vocabulary(단어 집합에 없는 단어) -> OOV : 6
#
# - 즉 word_to_index에 포함되지 않은 원본의 모든 단어들을 처리
# - index 맵핑 -> [1,5] , [1, ??, 5], [1, 3, 5]
# - ?? -> Out-Of-Vocabulary(단어 집합에 없는 단어) -> OOV : 6

# +
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

# 문장 토큰화
text = sent_tokenize(text)
print(text)

vocab = {} # 파이썬의 dictionary 자료형
sentences = []
stop_words = set(stopwords.words('english'))

for i in text:
    sentence = word_tokenize(i) # 단어 토큰화를 수행합니다.
    result = []

    for word in sentence: 
        word = word.lower() # 모든 단어를 소문자화하여 단어의 개수를 줄입니다.
        if word not in stop_words: # 단어 토큰화 된 결과에 대해서 불용어를 제거합니다.
            if len(word) > 2: # 단어 길이가 2이하인 경우에 대하여 추가로 단어를 제거합니다.
                result.append(word)
                if word not in vocab:
                    vocab[word] = 0  # 단어가 vocab에 없으면 추가 단어(keys) 추가
                vocab[word] += 1
    sentences.append(result) 

print(sentences) # 3글자 이상의 단어
print()
print(vocab) # 단어의 빈도수


# 빈도수가 높은 순서대로 정렬
# 딕셔너리.items()는 key,value를 튜플로 묶고 리스트로 바꿔주는 함수다

vocab_sorted = sorted(vocab.items(), key = lambda x:x[1], reverse = True)
print(vocab_sorted)

# 높은 빈도수를 가진 단어일수록 낮은 정수 인덱스 부여
word_to_index = {}
i=0
for (word, frequency) in vocab_sorted :
    if frequency > 1 : # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
        i=i+1
        word_to_index[word] = i
print(word_to_index)

vocab_size = 5
words_frequency = [w for w,c in word_to_index.items() if c >= vocab_size + 1] # 인덱스가 5 초과인 단어 제거
for w in words_frequency:
    del word_to_index[w] # 해당 단어에 대한 인덱스 정보를 삭제
print(word_to_index)

word_to_index['OOV'] = len(word_to_index) +1

encoded = []

for s in sentences:
    temp = []
    for w in s:
        try:
            temp.append(word_to_index[w])
        except KeyError:
            temp.append(word_to_index['OOV'])
    encoded.append(temp)
print(encoded)
# -

# ####  Collections.counter 사용하기

from collections import Counter
print(sentences)


words = sum(sentences, [])
print(words)


vocab = Counter(words)
print(vocab)

vocab_size = 5
vocab = vocab.most_common(vocab_size) # 등장 빈도수가 높은 상위 5개의 단어만 저장
vocab


# 높은 빈도수를 가진 단어일수록 낮은 정수 인덱스 부여
word_to_index = {}
i=0
for (word, frequency) in vocab_sorted :
    if frequency > 1 : # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
        i=i+1
        word_to_index[word] = i
print(word_to_index)

# +
word_to_index['OOV'] = len(word_to_index) +1

encoded = []

for s in sentences:
    temp = []
    for w in s:
        try:
            temp.append(word_to_index[w])
        except KeyError:
            temp.append(word_to_index['OOV'])
    encoded.append(temp)
print(encoded)

# +
from collections import Counter
print(sentences)

words = sum(sentences, [])
print(words)

vocab = Counter(words)
print(vocab)

vocab_size = 5
vocab = vocab.most_common(vocab_size) # 등장 빈도수가 높은 상위 5개의 단어만 저장
vocab

# 높은 빈도수를 가진 단어일수록 낮은 정수 인덱스 부여
word_to_index = {}
i=0
for (word, frequency) in vocab_sorted :
    if frequency > 1 : # 정제(Cleaning) 챕터에서 언급했듯이 빈도수가 적은 단어는 제외한다.
        i=i+1
        word_to_index[word] = i
print(word_to_index)

word_to_index['OOV'] = len(word_to_index) +1

encoded = []

for s in sentences:
    temp = []
    for w in s:
        try:
            temp.append(word_to_index[w])
        except KeyError:
            temp.append(word_to_index['OOV'])
    encoded.append(temp)
print(encoded)
# -

# ## 원-핫 인코딩(one-hot encoding)
#
# - 매우 중요
# - 단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고, 다른 인덱스에 0을 부여하는 단어의 벡터 표현 방식
#     1. 각 단어에 고유한 인덱스를 부여합니다(cf. 정수 인코딩)
#     2. 표현하고 싶은 단어의 인덱스의 위치에 1을 부여하고, 다른 단어의 인덱스에 0 을 부여한다

# 'barber' 'secret' 'hug' 'kept' 'person'
#    1        0       0     0       1  ----> 첫번째 문장
#    1        0       1     0       1  ----> 두번째 문장

# +
from konlpy.tag import Okt  
okt=Okt()  
token=okt.morphs("나는 자연어 처리를 배운다")  
print(token)

word2index={}
for voca in token:
     if voca not in word2index.keys():
            word2index[voca]=len(word2index)
print(word2index)

def one_hot_encoding(word, word2index):
    one_hot_vector = [0]*(len(word2index))
    index=word2index[word]
    one_hot_vector[index]=1
    return one_hot_vector


# -

from konlpy.tag import Okt  
okt=Okt()  
token=okt.morphs("나는 자연어 처리를 배운다")  
print(token)


word2index={}
for voca in token:
     if voca not in word2index.keys():
            word2index[voca]=len(word2index)
print(word2index)


def one_hot_encoding(word, word2index):
    one_hot_vector = [0]*(len(word2index))
    index=word2index[word]
    one_hot_vector[index]=1
    return one_hot_vector



one_hot_encoding("자연어",word2index)

# ####  케라스(Keras)를 이용한 원-핫 인코딩(One-Hot Encoding)
#
# - to_categorical()을 지원
# - 정수 인코딩과 원-핫 인코딩을 순차적으로 진행

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

# +
text="나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

t = Tokenizer()
t.fit_on_texts([text])
print(t.word_index) # 각 단어에 대한 인코딩 결과 출력
# 갈래가 3개니까 맨앞 점심 2 햄버거 2 그러나 순서가 점심이 빠르니 2번
# 이런식으로 다해줌
# -

sub_text="점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded = t.texts_to_sequences([sub_text])[0]
print(encoded)

one_hot = to_categorical(encoded)
print(one_hot)
# 인덱스는 0부터 붙음
# 따라서 처음 : 점심 인덱스 2번 벡터 1 나머지 0
# 다음 : 먹으러 인덱스 5번 벡터 1 나머지 0


