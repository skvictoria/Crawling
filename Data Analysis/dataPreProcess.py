import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def dataPreprocessing(path=r'C:\Users\6\Desktop\알고리즘 기법을 활용한 문제해결_프로그램 및 실습파일\2018년 2차_졸업생의 진로 현황(전체).xlsx', sheet_name='2018_졸업생의 진로 현황(중)'):
    
    raw_df = pd.read_excel(path,sheet_name)
    raw_df2 = raw_df[['지역','정보공시 \n 학교코드', '학교명', '졸업자.2','(특수목적고)외고ㆍ국제고 진학자.2', '(특수목적고)과학고 진학자.2' ]]
    raw_df2.columns = ['지역', '학교코드', '학교명', '졸업자', '외고', '과고']
    raw_df3 = raw_df2.drop(0).reset_index().dropna()
    for col in ['졸업자', '외고', '과고']:
        raw_df3[col] = pd.to_numeric(raw_df3[col])
        
    return raw_df3
    
    
def str_split(x):
    if type(x) == str:
        return x.split(' ')[0]
    else:
        return None
        
