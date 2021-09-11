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
from collections import Counter
from collections import defaultdict
id_lst = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
report = set(report)
report = list(report)

# id_report = {}
id_report = defaultdict(list)
for i in range(len(report)):
    
    id_report[report[i].split()[0]].append( report[i].split()[1])
check = []

for i in id_report:
    check.append(i)
for a in id_lst:
    if a not in check:
        id_report[a] = []

new_report = []
for a in id_report:
    print(id_report[a])
    new_report+= id_report[a]
new_report,id_report
stop = Counter(new_report)
stop
stop_lst = []
for name in stop:
    if  stop[name] >= k:
        stop_lst.append(name)
stop_lst
result_report = {}
cnt = 0
for name in id_report:
    for s_name in stop_lst:
#         print(id_report[name], s_name)
        if s_name in id_report[name]:
#             print(s_name)
            cnt += 1
#         print(cnt)
        result_report[name] = cnt
    cnt = 0
result_report
answer = []
if len(result_report) != 0:
    for i in id_lst:
        answer.append(result_report[i])
else:
    for i in id_lst:
        answer.append(0)
answer

# +
n , k = 1000000, 8
rev_base = ''

while n > 0:
    n, mod = divmod(n, k)
    rev_base += str(mod)

num_str = rev_base[::-1]

import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+ 1)):
        
        if x % i == 0:
            return False
    return True

cnt = 0
check  = []
start = 0


answer = 0

for i in range(len(num_str)):
    end = i
    
    if int(num_str[end]) != 0 and is_prime_number(int(num_str[start:end+1])):
        if end+1 < len(num_str):   
            if '0' not in num_str[start:end+1] and num_str[end+1] == '0' :         

                check.append(int(num_str[start:end+1]))
#                 print(check, num_str[start:end+1], 'start : ', start)
                start = i
    if end+1 <len(num_str):
        if int(num_str[end]) == 0 and int(num_str[end+1]) != 0:
            if i+1 < len(num_str):
                start = i+1

    if end == len(num_str)-1:
#         print(num_str[start:end+1])
        if '0' not in num_str[start:end+1] and is_prime_number(int(num_str[start:end+1])):
            check.append(int(num_str[start:end+1]))
    print(check, num_str[start:end+1], 'start : ', start)        

#     print(start, end = ' ')
# print(cnt, check)
# print('메롱',answer)
# 211020101011
print(len(check))
print(num_str)

# +
from collections import defaultdict
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
data = []
for i in range(len(records)):
    data.append(records[i].split())
data
car_dict = defaultdict(list)

for i in range(len(data)):
    car_dict[data[i][1]].append(data[i][0])
    car_dict[data[i][1]].append(data[i][2])
car_dict
start_t = 0
end_t = 0
sum_t = 0

tot_t = 0
tot_t_dict = defaultdict(int)
print()
# range가 벗어나는 경우를 어떻게 해야할지 생각해야해
for i in car_dict:

    try:
        for num in range(len(car_dict[i])//2):
            if car_dict[i][(2*num)+1] =='IN':
               
                if car_dict[i][(2*num)+3] == 'OUT':
                   
                # 주차 시간 계산하기
                    start_t = int(car_dict[i][2*num][:2])*60 + int(car_dict[i][2*num][3:])
                    end_t = int(car_dict[i][2*num+2][:2])*60 + int(car_dict[i][2*num+2][3:])
                    sum_t = end_t - start_t
                    tot_t += sum_t
                    
#         print('누적 시간 :', tot_t, '차량 :', i)
        tot_t_dict[i]= tot_t
        sum_t , tot_t, start_t, end_t = 0, 0, 0, 0  
#             if tot_t <= fees[0]:
#                     money += int(fees[1])
#             print('요금 :' ,money, '누적 시간 :', tot_t)
    except:
        start_t = int(car_dict[i][2*num][:2])*60 + int(car_dict[i][2*num][3:])
        end_t = 23*60+59
        sum_t = end_t - start_t
        tot_t += sum_t
        
#         print('누적 시간 :', tot_t,'차량 :', i )
        tot_t_dict[i]= tot_t
        sum_t , tot_t, start_t, end_t = 0, 0, 0, 0 

# fees = [180, 5000, 10, 600]
# 주차요금 계산하기
money_dict = defaultdict(int)
rest_t = 0
add_t = 0
for a in tot_t_dict:
#     print(a, end= ' ')
    if tot_t_dict[a] <= fees[0]:
        money_dict[a] += fees[1]
    else:
        rest_t = tot_t_dict[a] - fees[0]
        if rest_t % fees[2] == 0:
            add_t = rest_t // fees[2]
        else:
            add_t = rest_t // fees[2]+1
        
        money_dict[a] += fees[1]+ add_t*fees[3]
money_dict = dict(money_dict)
sdict = sorted(money_dict.items())
answer= []
for i in sdict:
    answer.append(i[1])
answer

# +
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]


# 0 은 안쓸거야
new_info = []

for i in range(len(info)-1,-1,-1):
#     print(i, end = ' ')
    new_info.append(info[i])

api_score = 0
api_score1 = 0
for i in range(len(new_info)):
    api_score1 += i*new_info[i]

rai_score = 0
rai_info = []


start = 1
sub_list = []

start = 1
cnt = 0
for i in range(len(new_info)-start, -1, -1):
    api_score = api_scopre1
    if new_info[i] == 0:
        
        rai_score += i
        cnt += 1
        if cnt <= n :
            continue
        else:
            break
    else:
        rai_score += i
        api_score -= i
        cnt += new_info[i]
    
    if rai_score> api_score:
        sub_list.append(rai_score - api_score)
    

    
api_score, new_info
# -

[0,2,2,0,1,0,0,0,0,0,0]
