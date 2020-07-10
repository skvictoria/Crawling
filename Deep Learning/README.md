## 머신러닝과 딥러닝의 차이점
- 머신러닝 : Feature Engineering 에 엄청난 시간 소요
  - 머신러닝의 종류 : 지도학습, 비지도학습, 강화학습
    -  지도학습 : 회귀분석, 분류분석
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
  
- Propagation
  - Forward Propagation
  - Back Propagation
    - 특정 edge가 특정 edge에 미치는 영향도 계산 - chain rule 사용

- Gradient Descent
  - 학습률을 지정해준다.
  - ex. Adam, Adagrad...
  
- Procedure
  - 데이터가 설계한 모델에 들어간다.
  - activation(sigma(weight * data) + bias)
  - 

## 정리
- 머신러닝 종류 - 지도학습, 비지도, 강화
- 지도학습 - 회귀분석, 분류분석

딥러닝 - 최적화 과정(학습과정)
1. 데이터가 설계한 모델에 들어감
2. activation(weight * x + bias)
3. 손실함수 = (y hat(예측값)-정답값), 특정한 weight가 손실함수까지 거쳤던 과정을 계산그래프로 그림
4. 오차역전파법은 미분을 구하는 것. 경사하강법 같은 Optimizer

> 퍼셉트론 - weight, bias, activation function으로 구성
> weight : perceptron이 detection하고자하는 영향을 조절
> bias: 임계값 조절
> activation : perceptron이 비선형성을 갖출 수 있도록
  - step function
  - sigmoid(오차역전파법 전파)
  - relu

> tensorflow(로레벨로 코딩)를 backend로 한 keras(이미 만들어져 있는 layer 추가해서..)

1. dnn(fully connected layer 여러개 연결)
2. cnn
3. serial data 처리에 특화되어있는 rnn 모델
cnn 장점 : 필터정보들을 이미지(시각화)해서 각각의 필터들이 이미지에 어떻게 반응했는가를 볼 수 있음.
