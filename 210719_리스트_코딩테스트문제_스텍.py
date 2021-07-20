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

# ## 파이썬에서 리스트 ->배열
#
# - 자료구조에서 리스트랑 다르다 꼭알고 있어라

# +
katok = [] # 빈 배열

# 1단계 : 6명 친구 추가
katok.append(None) # 빈칸 1개 확보( 제일 뒤에 )
katok[0] = '다현'
katok.append(None) # 빈칸에 데이터 추가
katok[1] ='정현'
katok.append(None) # 빈칸에 데이터 추가
katok[2] ='쯔위'
katok.append(None) # 빈칸에 데이터 추가
katok[3] ='사나'
katok.append(None) # 빈칸에 데이터 추가
katok[4] ='지효'
katok.append(None) # 빈칸에 데이터 추가
katok[5] ='모모'

# 2단계 미나가 갑자기 카톡을 연속으로 보내서 3등이 됨
# 새로운 친구 삽입
katok.append(None)
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
katok[3] = '미나'

# 3 단계 : 사나가 친구 차단 ( 빈칸을 놔두면 안됨 )

katok[4] = None
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
del(katok[6])
print(katok)


# +
## 함수 선언부
def add_data(friend):
    katok.append( None )
    kLen = len(katok)
    katok[kLen -1] = friend

def insert_data(position, friend):
    katok.append( None )
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend    

def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1,kLen):
        
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

    
# 전역 변수부
katok = []


## 메인 코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')
insert_data(3, '미나')
delete_data(4)
print(katok)
# -

if __name__ == '__main__':

    select = 0
    while (select != 4) :
        select = int(input('선택 1추가 2삽입 3삭제 4종료'))
        if (select == 1):
            data = input('추가 데이터--->')
            add_data(data)
            print (katok)
            break
        elif select ==2 :
            position = input(int('삽입할 위치 입력'))
            friend = input ( '추가할 데이터 입력')
            insert_data(position , fried)
            print (katok)
            break
        elif select ==3:
            position = int(input('삽입할 위치 입력'))
            delete_data(position)
            print (katok)
            break
        elif select == 4:
            print (katok)
            print ('종료합니다')
            break
        else:
            print('다시 입력해주세요')
            continue


# +
class Node():
    def __init__(self):
        self.data = None
        self.link = None
    
    
##메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정현'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# newNode = Node()
# newNode.data= '재남'
# newNode.link= node2.link
# node2.link = newNode

node2.link = node3.link
del (node3)


current = node1
print(current.data, end = " ")
while current.link != None:
    current = current.link
    print(current.data, end = " ")
print()


# +
## 함수, 클래스
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end = " ")
    while current.link != None:
        current = current.link
        print(current.data, end = " ")

        
def insertNode(findData, insertData):
    global memory, head, current, pre
    
    # 첫 노드 앞에 삽입
    
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # 중간 노드 앞에 삽입
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # 찾는 데이터가 없을 때 (= 마지막에 추가)
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData):
    global memory, head, current, pre
    # 첫 노드 삭제
    
    if head.data== deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    #첫 노드 이외 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
## 전역
memory = []
head, current, pre = None, None, None
# 데이터(DB, 웹크롤링, 센서 .....)

dataArray = ['다현', '정현', '쯔위', '사나', '지효']


## 메인
## (1) 연결리스트 생성
## (1-1) 첫 노드 생성

node = Node()
node.data = dataArray[0]
head = node

memory.append(node)

## 1-2 나머지 노드 생성
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)
print()
insertNode('다현', '화사')
printNodes(head)
print()
insertNode('사나', '솔라')
printNodes(head)
print()
insertNode('재남', '문별')
printNodes(head)
print()
deleteNode('화사')
printNodes(head)
print()
deleteNode('쯔위')
printNodes(head)
print()


# +
## 함수, 클래스
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end = " ")
    while current.link != None:
        current = current.link
        print(current.data, end = " ")

        
def insertNode(findData, insertData):
    global memory, head, current, pre
    
    # 첫 노드 앞에 삽입
    
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # 중간 노드 앞에 삽입
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # 찾는 데이터가 없을 때 (= 마지막에 추가)
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData):
    global memory, head, current, pre
    # 첫 노드 삭제
    
    if head.data== deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    #첫 노드 이외 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
def addNode(addData):
    global memory, head, current, pre
    if len(memory) == 0:
        node = Node()
        node.data = addData
        head = node
        memory.append(node)
    else:
        current = head
        while current.link != None:
            current = current.link
        node = Node()
        node.data = addData
        current.link = node
        
def findNode(findData):
    global memory, head, current, pre
    current = head
    while current.link != None:
        current = current.link
        if current.data ==findData:
            print(findData+'를 찾았습니다')
            return
    print('해당데이터를 찾을 수 없습니다')
    
            
## 전역
memory = []
head, current, pre = None, None, None
# 데이터(DB, 웹크롤링, 센서 .....)
select = -1

## 메인
while (select != 5):
    select = int(input('선택 1추가 2삽입 3삭제 4찾기 5종료'))
    
    if select == 1 :
        addData = input('추가할 데이터 입력')
        addNode(addData)
        printNodes(head)
        
    elif select == 2:
        findData = input('삽입할 위치 전의 데이터 입력')
        insertData = input('삽입할 데이터 입력')
        insertNode(findData,insertData)
        printNodes(head)
        
    elif select == 3:
        deleteData = input('삭제할 데이터입력')
        deleteNode(deleteData)
        printNodes(head)
        
    elif select ==4:
        findData = input('찾을 데이터 입력')
        findNode(findData)
        printNodes(head)
        
    elif select ==5:
        print('프로그램을 종료합니다')
        break
        
    else :
        print('다시 입력하세요.')
        continue

# +
ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)

def replaceData(numData): # numData	2차원 정수 배열
    retData = [] # 조건에 따라서 전처리된 2차원 배열

    ###########   여기부터 코딩 (1) ---------------->
    retData = numData
    for i in range(len(numData)):
        for j in range(len(numData)):
            if numData[i][j] < 0:
                retData[i][j] = 0
            elif numData[i][j] > 100:
                retData[i][j] = numData[i][j] % 100
            else:
                retData[i][j] = numData[i][j]



    ###########   <-------------- 여기까지 코딩 (1)

    return retData


# 2x2 크기의 배열의 최대합을 구한다.
def getMaxSum(numData): # 요구 사항에 맞춰 처리된 2차원 정수 배열
    maxSum = 0 # 최대합

    ###########   여기부터 코딩 (2) ---------------->
    preSum = 0
    retData = replaceData(numData)
    for i in range(len(numData)-1):
        for j in range(len(numData)-1):
            preSum = retData[i][j] +retData[i][j+1] +retData[i+1][j]+retData[i+1][j+1]
            if preSum > maxSum:
                maxSum = preSum
        



    ###########   <-------------- 여기까지 코딩 (2)

    return maxSum

## 전역 변수 선언 부분
numData =[] # 5x5 배열
ARRAY_LENGTH = 5 # 배열의 행과 열 크기(고정)

def main() :
        global numData

        loadData() # 2차원 배열 읽어오기

        ## 원본 출력
        print(' ----- 초기 배열 -----')
        printData()

        # 1. 데이터 치환 작업
        numData = replaceData(numData)
        print(' ----- 치환 후 배열 -----')
        printData()

        # 2. 최대 합 구하기.(2x2 크기)
        maxSum = getMaxSum(numData)
        print('최대 영역의 합: %d' % maxSum)

       
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global numData

    ###########
    # 제공 데이터 세트 1 
    # 5x5 숫자 배열. 
    ###########
    numData = \
    [
        [ 5, 7, -5, 100, 73 ],
        [ 35, 23, 4, 190, 33 ],
        [ 49, 85, 662, 39, 81 ],
        [ 124, -59, 86, 46, 52 ],
        [ 27, 7, 8, 33, -56 ] 
    ]
    
    

def printData() :
        for i in range(0, ARRAY_LENGTH) :
                for k in range(0, ARRAY_LENGTH) :
                        try :
                                print("%5d" % numData[i][k], end='')
                        except :
                                pass
                print()
        print('--------------------------------------')

## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()

# +
stack = [None, None, None,None,None]
top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
print('바닥 |', stack)

data = stack[top]
stack[top] = None # top을 뺀자리에 쓰레기가 남으니까 지워준다
top -= 1
print('추출--->', data)

data = stack[top]
stack[top] = None 
top -= 1
print('추출--->', data)

print('바닥 |', stack)
# -


