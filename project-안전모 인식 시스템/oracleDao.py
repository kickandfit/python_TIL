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
import cx_Oracle

# 조회
def select():
    conn=cx_Oracle.connect("pgm/1234@localhost:1521/xe")
    cursor=conn.cursor() #커서 생성
    sql="select * from product order by product_id"
    cursor.execute(sql)

    for row in cursor:
        for i in range(len(row)):
            if i==3:
                description=row[3].read() #CLOB필드 읽는 방법
            print(row[i], end=" ")
        print()

    cursor.close()
    conn.close()
#select()

# 삽입
def insert(t):
    conn=cx_Oracle.connect("system/1234@localhost:1521/xe")
    cursor=conn.cursor() #커서 생성
    sql="insert into sign values(:1)"
    cursor.execute(sql,t)
    cursor.close()
    conn.commit()
    conn.close()
#insert((11,'위',3000,'비타민 C가 풍부, 다이어트나 미용에 좋음', 'kiwi.jpg'))


#delete((10,))
# -












