# -------------------------------------------------
# 패키지 import
# -------------------------------------------------
import pandas as pd
import numpy as np

# -------------------------------------------------
# pandas 버전 확인
# -------------------------------------------------
# print(pd.__version__)

# -------------------------------------------------
# pd.series
# -------------------------------------------------
# pandas.series object = 1차원 배열

# data = pd.Series([0.25,0.5,0.75,1.0])
# print(data) # index와 value, 데이터 타입 출력
# print(data.values) # 배열 원소 출력
# print(data.index) # index 범위 출력
# print(data[1]) # index가 1인 value, 데이터 타입 출력
# print(data[0:4].values) # index가 1인 배열의 원소 출력
# data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d']) # 각 index를 부여할 수 있음
# print(data['b']) # index에 해당하는 값을 출력
# print(data.values)

# -------------------------------------------------
# Series dictionary
# -------------------------------------------------
# population_dict = {'California': 39538223, 'Texas': 29145505,
#                    'Florida': 21538187, 'New York': 20201249,
#                    'Pennsylvania': 13002700} # json 처럼 dictionary 형태로 저장 가능
# population = pd.Series(population_dict)
# print(population)
# print(population['California':'Florida'])

# -------------------------------------------------
# Series 생성
# -------------------------------------------------

