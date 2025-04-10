# ------------------------------------------------------------------
# import Package
# 시간을 다루는 패키지
# ------------------------------------------------------------------
from datetime import datetime
from dateutil import parser
# ------------------------------------------------------------------
#
# 어떠한 시점의 시각을 나타내는 것 --> Time Stamp
# ------------------------------------------------------------------

# print(datetime(year=2025,month=4,day=10,hour=11,minute=17,second=00))

# ------------------------------------------------------------------

# date=parser.parse("10th of April, 2025") # 문자열에서 날짜를 파싱해서 date에 저장
# (print(date)) # date 출력
# print(date.strftime('%A')) # 요일

# ------------------------------------------------------------------
# numpy로 넘어오니까 매우 큰 데이터를 처리하다보니 원래 datetime 함수가 매우 느리게 실행됨
# ------------------------------------------------------------------

import numpy as np
# date = np.array('2025-04-10',dtype=np.datetime64)
# print(date)
# print(date+np.arange(12))

# ------------------------------------------------------------------

# print(np.datetime64('2025-04-10'))
# print(np.datetime64('2025-04-10 12:00'))
# print(np.datetime64('2025-04-10 12:00','ns')) # ns 까지 표현

# 다루는 범위에 따라 DataType에 대한 설정이 필요함

# Code	Meaning	Time span (relative)	Time span (absolute)
# Y	Year	± 9.2e18 years	[9.2e18 BC, 9.2e18 AD]
# M	Month	± 7.6e17 years	[7.6e17 BC, 7.6e17 AD]
# W	Week	± 1.7e17 years	[1.7e17 BC, 1.7e17 AD]
# D	Day	± 2.5e16 years	[2.5e16 BC, 2.5e16 AD]
# h	Hour	± 1.0e15 years	[1.0e15 BC, 1.0e15 AD]
# m	Minute	± 1.7e13 years	[1.7e13 BC, 1.7e13 AD]
# s	Second	± 2.9e12 years	[ 2.9e9 BC, 2.9e9 AD]
# ms	Millisecond	± 2.9e9 years	[ 2.9e6 BC, 2.9e6 AD]
# us	Microsecond	± 2.9e6 years	[290301 BC, 294241 AD]
# ns	Nanosecond	± 292 years	[ 1678 AD, 2262 AD]
# ps	Picosecond	± 106 days	[ 1969 AD, 1970 AD]
# fs	Femtosecond	± 2.6 hours	[ 1969 AD, 1970 AD]
# as	Attosecond	± 9.2 seconds	[ 1969 AD, 1970 AD]

# ------------------------------------------------------------------

import pandas as pd
# date = pd.to_datetime("10th of April, 2025")
# print(date)
# print(date.strftime('%A'))
# print(date+pd.to_timedelta(np.arange(12),'D'))

# ------------------------------------------------------------------

# index = pd.DatetimeIndex(['2020-07-04', '2020-08-04',
#                           '2021-07-04', '2021-08-04'])
# data = pd.Series([0, 1, 2, 3], index=index)
# print(data['2020-07-04':'2021-07-04'])
# print(data['2021'])

# ------------------------------------------------------------------
# numpy와 pandas에서 쓰기위해 Timestamp 라는 데이터타입을 만들었음
# ------------------------------------------------------------------