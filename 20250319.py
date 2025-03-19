from datetime import datetime

import numpy as np
import pandas as pd

# rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
# inches = rainfall / 254.0
# inches.shape

# x = np.array([1,2,3,4,5]) # 각 원소별로 boolean으로 반환 = True or False
# print(x<3)
# print(x>3)
# print(x<=3)
# print(x>=3)
# print(x!=3)
# print(x==3)

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3,4)) # 3행 4열의 랜덤 정수 배열 생성
print(x)
print(x<6)