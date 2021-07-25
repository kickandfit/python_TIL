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
import matplotlib.pyplot as plt
import numpy as np

# np로 생성된 숫자는 array임으로 배열로 바꿔줘야한다
lst_data1 = [np.random.randint(10,51) for i in range(10) ]
lst_data2 = [np.random.randint(10,51) for i in range(10) ]


#여러개 차트 한 화면에 출력(두개의 행으로 출력)

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(lst_data1, 'k')
ax2.plot(lst_data2, 'r')

plt.show()

# +
#여러개 차트 한 화면에 출력(두개의 열으로 출력)

fig = plt.figure(figsize = (12, 3))

ax1 = fig.add_subplot(1,2,1) # .add_subplot( 행개수, 열개수, 위치값)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(lst_data1, 'k')
ax2.plot(lst_data2, 'r')

plt.show()

# +
#여러개 차트 한 화면에 출력(여러개의 행/열으로 출력)
# 위치값은 행*열을 한 수에서 왼쪽 부터 번호가 1, 2, ...
# 단수로 각각의 위치를 잡아가면서 만들어주는 것

fig = plt.figure()

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,1,2)
ax4 = fig.add_subplot(3,3,7)
ax5 = fig.add_subplot(3,3,8)
ax6 = fig.add_subplot(3,3,9)

ax1.plot(lst_data1, 'k')
ax2.plot(lst_data2, 'r')
ax3.plot(lst_data1, 'g')
ax4.plot(lst_data2, 'b')
ax5.pie(lst_data1)
ax6.pie(lst_data2)


plt.show()

# +
#복수형 2행 2열을 만들어줘라
fig, ax_lst = plt.subplots(2,2)

ax_lst[0][0].plot(lst_data1)
ax_lst[1][1].plot(lst_data2)
plt.show()
# -


