# The utilities for data preprocessing
- data analytics (using kaggle)
- macro
- crawling
- curation


pandas
시리즈(1차원) - 인덱스, 데이터
데이터프레임

컬럼이름으로 고른 다음->인덱스로 고름 train['Embarked'][0]
.loc를 보면 행(index)부터 보고 -> 컬럼으로 고름 train.loc[0, 'Embarked']

자료구조에서 데이터 갖고올때는 꺽쇠모양

concat 시 list로 묶어서 데이터들을 넣어줌. 입력값 하나임

## 탐색적 데이터 분석

tag 찾아주는 아이: beautiful soup

정수, 실수, 문자열(->곱하기, 더하기 됨)
type(변수) -> 자료형 알수 있다.

기본 자료구조
순서:리스트(for) 키:딕셔너리 튜플:안에있는 내용을 바꿀수없음 셋:중복허용안함

형변환 int(), str(), set(), list()

반복문 for문 while문

if문

module class

xlsxwriter ->wb ->sheet->data
xlrd (pandas의 read excel 쓰면됨)

웹 크롤링
bs4(검색가능), request(서버에 리퀘 요청해서 받아옴)

알고리즘
-정렬 알고리즘
	-퀵 정렬 : 피봇 설정하는 게 중요함.
	-삽입 정렬 : 자료 정렬되어있는 상태에서 어떤 자료의 위치를 찾아주는 것.
-스택큐
	-스택 : 먼저 들어온 애가 나중에 나감(선입후출)

셀레니움을 이용해서 매크로 만들기

데이터분석(pandas이용) -> 시리즈(인덱스, 데이터값), 데이터프레임(!)(컬럼, 인덱스, 데이터값)
