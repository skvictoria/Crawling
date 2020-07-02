import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

data = sns.load_dataset("titanic")
data.to_excel("titanic.xlsx")

titanic['survived'] # survived column의 전체를 보여줌
titanic['survived'].value_counts(normalize = True) # 몇프로 죽고, 몇프로 살았는지

sns.countplot(titanic['survived'])

################# 데이터 정렬방법 ######################
# A, B, C, D, E, F
math = [92, 94, 93, 95, 82, 99]
sorted(math) # 리스트 정렬

math_s = pd.Series(math, index = "A, B, C, D, E, F".split(", "))
#sorted(math_s) # 리스트 형태 -> 우리한테는 의미가 없음

math_s.sort_values(ascending=False) #Series 정렬
math_s[math_s > 90]

math = [92, 89, 90, 91, 82, 99]
eng = [88, 99, 76, 90, 92, 85]
kor = [100, 99, 89, 91, 89, 90]

grade_df = pd.DataFrame({"수학":math, "영어":eng, "국어":kor}, index = "A, B, C, D, E, F".split(", ")) # 리스트를 데이터 프레임 형태로 바꿔줌
###########################################################

############# 데이터 접근방법 ##############################
a = grade_df['수학']['A']
type(a) # numpy.int64
grade_df.loc['A']
grade_df.iloc[0]

grade_df[ grade_df['수학'] > 90 ]  # 데이터 filtering 방법
########################################################

