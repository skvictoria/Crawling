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

del total['Cabin'] # 결측값 많은 'Cabin'은 없애버리기
del total['Ticket'] # 티켓은 안쓰니까 없애버리기
###############################################################################################


############################## 머신러닝에 넣을 수 있도록 모든 데이터를 숫자로 바꿔주기 (One-Hot Encoding) #########
'''
def temp(x):
    if x =='male':
        return 0
    else:
        return 1
    
total['Sex'] = total['Sex'].apply(temp)
'''
total['Sex_1'] = total['Sex'].apply(lambda x :1 if x =='male' else 0) # 앞에꺼 왜 안되는지 모르겠는데 이렇게 해야 됐었음.

################################################################################################


###################### 유효한 데이터로 만들어주기 #####################
# 가족들은 묶어주기
total['Family'] = total['SibSp']+total['Parch']

# 가족들에 대해 살펴보자.
total.groupby(['Family']).mean() # 혼자 탔을때는 생존률 적은데 가족이 조금 있을때는 생존률 높다. 너무 많으면 생존률 낮다.
sns.countplot(data = total, x = 'Family', hue = 'Survived') # 더 잘 보이게 그래프로 볼 수 있음

# 따라서 맵을 만들어준다. 우리는 Alone, Small, Big로 분류하였다.
family_map = {0:'Alone', 1:'Small', 2:'Small', 3:'Small', 4:'Big', 5:'Big', 6:'Big', 7:'Big', 10:'Big'}
total['Family'] = total['Family'].map(family_map)


# 이름 바꿔주기
total['Status'] = total['Name'].apply(lambda x:x.split(',')[1].split('.')[0].strip())
total['Status'].unique()
total['Status'].value_counts()
    # 이를 봤을 때 Mr, Miss, Mrs, Master, Other로 Status를 분류할 수 있다.
temp_map = {'Mr':'Mr', 'Mrs':'Mrs', 'Miss':'Miss', 'Master':'Master', 'Don':'Others', 'Rev':'Others', 'Dr':'Others', 'Mme':'Mrs', 'Ms':'Miss',
       'Major':'Others', 'Lady':'Others', 'Sir':'Others', 'Mlle':'Miss', 'Col':'Others', 'Capt':'Others', 'the Countess':'Others',
       'Jonkheer':'Others', 'Dona':'Others'}

total['Status'] = total['Status'].map(temp_map)
total['Status'].value_counts()


# 나이 바꿔주기 -> 문제점: 나이 범위가 너무 커서 거리를 구하거나 할 때 거리가 크게 나온다. 그래서 이걸 정규화시켜주거나 / 가족들 데이터 바꿔준 것처럼 index를 바꿔줄 필요가 있다.
sns.distplot(total['Age'])
    # 정규화 시켜주는 방법
sns.distplot((total['Age']-total['Age'].mean())/total['Age'].std()) # 우리가 많이 쓰는 의미의 정규화
sns.distplot((total['Age']-total['Age'].min())/(total['Age'].max()-total['Age'].min())) # 최대와 최소를 가져와서 쓰는 정규화

    # index를 바꿔주는 방법
sns.distplot(total[total['Survived']==1]['Age'])
sns.distplot(total[total['Survived']==0]['Age'])

plt.xlim([0,17]) # 0에서 17까지
plt.show()

sns.distplot(total[total['Survived']==1]['Age'])
sns.distplot(total[total['Survived']==0]['Age'])

plt.xlim([17,31]) # 17에서 31까지
plt.show()

sns.distplot(total[total['Survived']==1]['Age'])
sns.distplot(total[total['Survived']==0]['Age'])

plt.xlim([31,57]) # 31에서 57까지
plt.show()

sns.distplot(total[total['Survived']==1]['Age'])
sns.distplot(total[total['Survived']==0]['Age'])

plt.xlim([57,80]) # 57에서 80까지
plt.show()

# 앞에서 나이를 4개의 구간으로 나눌 수 있다는 것을 살펴보았다.
def temp(x):
    if x<17:
        return 'baby'
    elif x<31:
        return 'young'
    elif x<57:
        return 'midage'
    else:
        return 'old'

# 이를 적용해준다.    
total['Age_chng'] = total['Age'].apply(temp)
total['Age_chng']
#################################################################

######### test와 train set 분리하기 #############################
total.isna().sum()
total_train = total.dropna()
total_test = total[total['Survived'].isna()]

##############################################################

################# 머신러닝 돌리기 #############################
from sklearn import neighbors

knn_model = neighbors.KNeighborsClassifier(n_neighbors = 10) # 모델 불러오기
target = total_train['Survived'] # 우리가 목표로 하는 타겟

temp_f = total_train[['Family', 'Age_chng', 'Status', 'Embarked', 'Sex_1', 'Pclass']]
features = pd.get_dummies(temp_f , columns = ['Family', 'Age_chng', 'Status', 'Embarked', 'Sex_1', 'Pclass'], drop_first = True)
temp_f = total_test[['Family', 'Age_chng', 'Status', 'Embarked', 'Sex_1', 'Pclass']]
test_features = pd.get_dummies(temp_f , columns = ['Family', 'Age_chng', 'Status', 'Embarked', 'Sex_1', 'Pclass'], drop_first = True)

knn_model.fit(features, target)
