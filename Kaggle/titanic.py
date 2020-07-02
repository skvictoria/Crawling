import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# train set과 test set 불러와서 dtypes 확인

train = pd.read_csv(r'C:\Users\6\Downloads\titanic\train.csv', engine = 'python', encoding='utf-8')
test = pd.read_csv(r'C:\Users\6\Downloads\titanic\test.csv', engine = 'python', encoding='utf-8')

train.dtypes

######################## 결측 확인 # -> train data와 test data 모두 채워줘야 함.###########################



train.isna().sum()
# 결측된 데이터가 age가 177개나 된다. 그럼 결측률은 어떨까?

train.isna().sum()/len(train)*100
# 나이의 결측률이 19프로이므로 우리가 알아서 메꿀수 있을것. 그러나 cabin의 결측률은 어마무시하므로 데이터분석 할때 빼자.

# survived (다른것도 넣을 수 있음) 가 0과 1밖에 없는게 확실한지 확인
train['Survived'].unique()
###########################################################################################################

############################### 데이터 분석해보기 ##########################
sns.distplot(train['Age']) # age distplot
plt.plot(train['Age'].sort_values().reset_index()['Age']) #앞과 같은 결과
#########################################################################

###########################결측값 채워주기#########################################

total = pd.concat([train, test]).reset_index()
del total['index']

total.isna().sum()/len(total)*100 # 채워야 하는 결측값

## Fare 결측값 채우기
total['Fare']= total['Fare'].fillna(total['Fare'].median())
train.isna().sum() # fare가 다 채워졌다.

## Embarked 결측값 채우기
total['Embarked'].value_counts() # S가 압도적으로 많으므로 fillna에서 S를 넣어주자.
total['Embarked']= total['Embarked'].fillna('S')

## age 결측값 채우기
total.groupby(['Sex', 'Embarked']).mean()
total.groupby(['Sex', 'Pclass']).mean() # 이게 더 구분을 세게 해준다.

total.loc[ (total['Age'].isna() )& (total['Sex']=='female') & (total['Pclass']==1),'Age'] = 37.037594
total.loc[ (total['Age'].isna() )& (total['Sex']=='female') & (total['Pclass']==2),'Age'] = 27.499223
total.loc[ (total['Age'].isna() )& (total['Sex']=='female') & (total['Pclass']==3),'Age'] = 22.185329
total.loc[ (total['Age'].isna() )& (total['Sex']=='male') & (total['Pclass']==1),'Age'] = 41.029272
total.loc[ (total['Age'].isna() )& (total['Sex']=='male') & (total['Pclass']==2),'Age'] = 30.815380
total.loc[ (total['Age'].isna() )& (total['Sex']=='male') & (total['Pclass']==3),'Age'] = 25.962264

## 결측값 많은 'Cabin'은 없애버리기
del total['Cabin']
###############################################################################################




