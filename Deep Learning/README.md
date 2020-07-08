## 머신러닝과 딥러닝의 차이점
- 머신러닝 : Feature Engineering 에 엄청난 시간 소요
- 딥러닝 : 컴퓨터가 알아서 학습

## 파라미터 구성
- 가중치
- 편향
- Activation Function
  - 회귀 분석 : 항등함수 사용
  - 분류 분석 : softmax 함수(확률 분포로 변경) 사용
- hidden layer의 개수
- 각 layer당 perceptron의 개수

## Optimization
- 손실 함수(목적 함수, 비용 함수)
  - 학습의 지표가 됨
  - 모델의 추론 결과와 실제 정답 간 차이
  - 대표적인 예 : Mean Square Error -> 작은 것은 더 작게, 큰 것은 더 크게
  
- Backpropagation
