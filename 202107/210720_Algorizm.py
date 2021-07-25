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
## 함수
def isStackFull(): # 스택이 꽉 찾는데 
    global size, stack, top
    if (top == size -1 ) :
        return True
    else : 
        return False

def push(data):
    global size, stack, top
    if isStackFull(): #== True:를 붙여도 상관은 없는데 촌스러움
        print('스택 꽉!')
        return
    else:
        top += 1
        stack[top] = data
def isStackEmpty():
    global size, stack, top
    if top == -1:
        return True
    else :
        return False
def pop():
    global size, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return None
        
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
def peek():
    global size, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return None
    return stack[top]
        
def init():
    global size, stack, top
    
    if isStackEmpty():
        print('이미 초기화 된 상태입니다')
    else:
        while top != -1:
            stack[top] = None
            top -= 1
        return stack
        
## 전역
size = 5
stack = [None for i in range(size)]
top = -1


## 메인
push('커피');push('녹차');push('꿀물');push('콜라');push('환타');
print(stack)
push('게토레이')


# +
## 함수
## 함수
def isStackFull(): # 스택이 꽉 찾는데 
    global size, stack, top
    if (top == size -1 ) :
        return True
    else : 
        return False

def push(data):
    global size, stack, top
    if isStackFull(): #== True:를 붙여도 상관은 없는데 촌스러움
        print('스택 꽉!')
        return
    else:
        top += 1
        stack[top] = data
        print(stack)
def isStackEmpty():
    global size, stack, top
    if top == -1:
        return True
    else :
        return False
def pop():
    global size, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return None
        
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        print(stack)
        return data
def peek():
    global size, stack, top
    if isStackEmpty():
        print('스택이 비었습니다')
        return None
    else:
        print(stack)
    return stack[top]
        
def init():
    global size, stack, top
    
    if isStackEmpty():
        print('이미 초기화 된 상태입니다')
    else:
        while top != -1:
            stack[top] = None
            top -= 1
        print(stack)
        return stack


## 전역
size = int(input('스택 크기--->'))
stack = [None for _ in range(size)]
top = -1
select = -1


## 메인
while (select != True):
    select = input ('I(삽입), E(추출), V(확인),R(초기화), X(종료)')
    
    if (select == 'I' or select == 'i'):
        push(input('삽입할 데이터를 입력하세요'))
       
    elif (select == 'E' or select == 'e'):
        pop()
        
    elif (select == 'V' or select == 'v'):
        peek()
        
    elif (select == 'R' or select == 'r'):
        init()
        
    elif (select == 'X' or select == 'x'):
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못 입력하였습니다. \n 다시 입력해주세요.')

# +
## 함수



## 전역
size = 5
queue = [None for _ in range(size)]
front , rear = -1, -1

## 메인

# enQueue(삽입)
rear += 1 ; queue[rear] = '화사'
rear += 1 ; queue[rear] = '솔라'
rear += 1 ; queue[rear] = '문별'
print( '출구<---', queue,'<---입구')

# deQueue(출구)

front += 1
data = queue[front]
queue[front] = None
print ('입장 손님-->', data)
front += 1
data = queue[front]
queue[front] = None
print ('입장 손님-->', data)
front += 1
data = queue[front]
queue[front] = None
print ('입장 손님-->', data)


# +
##함수 부분

# def isQueueFull(): #이 버전은 앞이 비어있는 가짜 꽉을 구별을 못합
#     global size, queue, front, rear
#     if ( rear == size -1 ):
#         return True
#     else:
#         False

def isQueueFull(): 
    global size, queue, front, rear
    if ( rear != size -1 ):
        return False
    elif (rear == size - 1) and (front == -1):
        return True
    else:
        for i in range(front+1,size, 1):
            queue[i-1]=queue[i]
            queue[i] = None
        front -=1
        rear -=1
        return False
    
def enQueue(data):
    global size, queue, front, rear
    if isQueueFull():
        return print('큐 꽉!')
    rear += 1
    queue[rear] = data
    return print(queue)
    
def isQueueEmpty():
    global size, queue, front, rear
    if (front == rear):
        print('큐가 비었습니다.')
        return True
    else :
        return False
        
def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        data = queue[front]
        print('큐가 비어있어 출력할 수 없습니다')
        return print('큐가 비어있어 출력할 수 없습니다')
    
    front += 1
    data = queue[front]
    if front != 0:
        queue[front - 1]= None
    return data
        
##전역 변수 부분
size = 5
queue = [None for _ in range(size)]
front , rear = -1, -1

##메인코드 부분
enQueue('값1');enQueue('값2');enQueue('값3');enQueue('값4');enQueue('값5');


# +
#원형 큐 구현
def isQueueFull(): #이 버전은 앞이 비어있는 가짜 꽉을 구별을 못합
    global size, queue, front, rear
    if ( (rear+1)%size == front ):
        return True
    else:
        False
    
def enQueue(data):
    global size, queue, front, rear
    if isQueueFull():
        return print('큐 꽉!')
    rear = (rear+1)%size
    queue[rear] = data
    return print(queue)
    
def isQueueEmpty():
    global size, queue, front, rear
    if (front == rear):
        print('큐가 비었습니다.')
        return True
    else :
        return False
        
def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        data = queue[front]
        print('큐가 비어있어 출력할 수 없습니다')
        return print('큐가 비어있어 출력할 수 없습니다')
    
    front = (front +1)%size
    data = queue[front]
    queue[front]= None
    return data
        
##전역 변수 부분
size = 5
queue = [None for _ in range(size)]
front , rear = 0, 0 # 이부분에 따라 원형인지 일반 큐인지 구분
#꽉 찬 경우는 rear 다음이 front면 꽉찬경우
#한칸은 비워놔야 하는것이 point 즉 size 5 개면 데이터는  4개까지 들어감
#원형 큐는 맨마지막 값 + 1이 front

# +
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3


node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data)
print(node1.right.data)
print(node1.left.left.data)
print(node1.left.right.data)
print(node1.right.left.data)


# +
##함수, 클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


##전역변수
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
node, root = None, None
memory = []


node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    
    
    current = root
    while True: #자리를 잡을때까지
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            
            if current.right == None:
                current.right =node
                break
            current = current.right
    memory.append(node)

print('이진탐색 트리 완료')

## 검색에 아주 빠름!
findName = '마마무'

current = root
while True:
    if findName == current.data:
        print('아싸~',findName,"찾았음!")
        break
    if findName < current.data:
        if current.left == None:
            print('엉엉', findName,'못찾았음')
            break
        current = current.left
    else:
        if current.right == None:
            print('엉엉', findName,'못찾았음')
            break
        current = current.right


# +
## 함수, 클래스
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        



## 전역
A, B, C, D = 0, 1, 2, 3
G1 = Graph(4)

## 메인

G1.graph[A][B] = 1
G1.graph[A][C] = 1
G1.graph[A][D] = 1

G1.graph[B][A] = 1
G1.graph[B][C] = 1

G1.graph[C][B] = 1
G1.graph[C][A] = 1
G1.graph[C][D] = 1

G1.graph[D][A] = 1
G1.graph[D][C] = 1

for i in range(4):
    for k in range(4):
        print(G1.graph[i][k], end=' ')
    print()
print('-------------------------')
G2 = Graph(4)
G2.graph[A][B]=1
G2.graph[B][A]=1

G2.graph[B][D]=1
G2.graph[D][B]=1

G2.graph[C][D]=1
G2.graph[D][C]=1

for i in range(4):
    for k in range(4):
        print(G2.graph[i][k], end=' ')
    print()


# +
# 재귀(Recrusion)
# 함수
def openBox(count):
   

    print('상자 열기')
    if count == 0:
        print('선물 넣기')
    if count > 0:
     
        openBox(count -1)
        print('상자 닫기!')
        
        


# 메인 코드부
openBox(5)


# -

# 함수
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num - 1)
addNumber(5)


# +
def Factorial(num):
    if num <= 1:
        return 1
    return num*Factorial(num-1)

Factorial(3)


# +
def countDown(num):
    if num <= 1:
        print(num)
        return print('로켓발사!')
    print(num)
    return countDown(num -1)
    
countDown(5)

# +
layer = 5
def printStar(num):
    global layer
    print( '*'*num)
    if num == layer:
        return
    return printStar(num+1)

printStar(1)


# -

def printStar(layer):
    if layer > 0:
        printStar(layer-1)
        print("*"*layer)
printStar(5)


# +
def num(n):
    print(n)
    if n > 0 :
        num(n-1)
        print(n)
        
num(3)


# +
# 함수
def FindMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx]> ary[i]):
            minIdx = i
    return minIdx
# 전역
testAry = [55, 88, 33, 77]
minPos = FindMinIndex(testAry)
print('최솟값-->', testAry[minPos])
#메인



# +
## 함수
def FindMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx]> ary[i]):
            minIdx = i
    return minIdx

## 전역
import random
before = [random.randint(50,200) for _ in range(10)]
after = []


##
print('정렬 전-->', before)
for _ in range(len(before)):
    minPos = FindMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)


# +
## 함수
def selctionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = 0
        for k in range(i+1, n) :
            if (ary[minIdx]> ary[k]):
                minIdx = k
        ary[i],ary[minIdx] = ary[minIdx], ary[i]
    return ary
## 전역
import random
size = 100
dataAry = [random.randint(50,200) for _ in range(size)]

## 메인

print('정렬 전-->', dataAry)
dataAry = selctionSort(dataAry)
print('정렬 후-->', dataAry)


# +
## 이진검색

## 함수
def binarySerach(ary, fData):
    pos =-1
    start = 0
    end = len(ary)-1
    while (start<=end):
        mid = (start + end) // 2
        if ary[mid] == fData:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else :
            end = mid - 1
    
    
    return pos

## 전역
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 180]
findData = 162

## 메인
print('배열-->', dataAry)
position = binarySerach(dataAry, findData)
if position == -1:
    print('없어요')
else:
    print(findData, '는', position, '위치에 있어요')
# -


