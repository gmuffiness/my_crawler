import numpy as np
import csv
import pandas as pd
import openpyxl

# 16 x 3 형태의 평균 0, 표준편차 1인 표준정규분포를 따르는 난수 생성.
array1 = np.random.randn(16,3)
# 만든 변수에 모두 3을 더해서 평균 3, 표준편차 1인 표준정규분포가 되도록 만듦.
array1 = array1 + 3
# array 형태를 list로 바꿈.
array1 = array1.tolist()
print(array1)

# 엑셀로 만들기
xlsx = pd.DataFrame(array1)
xlsx.to_excel('./pandas_result.xlsx',index=False) # index : 첫 열에 숫자 붙여주기

# csv로 만들기
# f = open(f'random_num2.csv', 'w', encoding='ANSI', newline='')
# csvWriter = csv.writer(f)
# # csvWriter.writerow(['단가id','차량명','부품명','부품등급','판매가격'])
# for postObject in array1:
#     csvWriter.writerow(postObject)
# f.close()

print('complete')