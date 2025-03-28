import numpy as np

# Broadcasting

# a = np.array([0,1,2])
# b = np.array([5,5,5])

# 연산 과정에서 차원이 다르다면?
# --> 차원이 낮은 것을 높은 차원으로 변환함 ex. newexis처럼?
# ---> 나머지 차원의 원소 개수만큼 복사해서 크기를 맞춰서 연산한다.

# print(a+b)
# print(a+5)
#
#
# m = np.ones((3,3))
# print(m)

# -------------------------------

# a = np.arange(3)
# b = np.arange(3)[:,np.newaxis]
# b = np.arange(3)[np.newaxis,:] # 보통 이렇게 함

# print(a)
# print(b)


# 1,3 array + 3,1 array를 연산하려면 각 행,열의 크기를 맞추기 위해 3,3 array로 바꿔서 계산한다.
# 강제로 복사하면서 늘린다.
# print(a+b)

# M = np.ones((2,3)) # 2행 3열을 1로 채움
# a = np.arange(3) # 0,1,2 배열 만들기


# 둘의 차원이 다르기 때문에 a array를 2행 3열로 바꾼 뒤에 연산한다? --> 1인 경우만 바꿈
# [0,1,2]를 강제로 늘려서 [[0,1,2]
#                      [0,1,2]로 바꾼다
# 차원이 같아졌기에 그대로 연산하면 됨.
# print(M+a)



# M = np.ones((3,2)) # 2행 3열을 1로 채움
# a = np.arange(3) # 0,1,2 배열 만들기

# 브로드캐스팅 불가 연산
# 3,2 array와 1,3 array는 연산이 불가함. 최소공배수로 맞출수는 없기 때문임
# print(M+a)

# -------------------------------

# broad casting을 하는 가장 큰 이유 --> 모든 행,열에 대해 연산 해야함
# 실수 연산이니까 정확하지 않음. 그러므로 표준편차의 합이 0이 나올수가 없음.

X = np.random.random((10,3))

Xmean = X.mean(0)
print(Xmean)
X_centered = X - Xmean
print(X_centered.mean(0))

