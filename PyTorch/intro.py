import torch

x = torch.empty(5,3)
print(x)
'''
tensor([[-1.5972e-21,  4.5860e-41, -2.8723e-20],
        [ 4.5860e-41,  3.8805e+25,  6.5096e+32],
        [ 2.9208e-11,  3.9753e+28,  2.5444e+30],
        [ 3.7893e+22,  3.9737e+28,  6.0657e+23],
        [ 2.9194e-11,  3.7906e+22,  4.1613e-41]])
'''
x = torch.rand(5,3)
print(x)
'''
tensor([[0.3667, 0.8356, 0.1937],
        [0.6451, 0.3781, 0.8523],
        [0.2566, 0.6915, 0.0700],
        [0.0289, 0.4601, 0.0125],
        [0.3195, 0.4799, 0.8237]])
'''
'''
torch.rand() : 0과 1사이의 숫자를 균등하게 생성
torch.rand_like() : 사이즈를 튜플로 입력하지 않고 기존의 Tensor로 정의
torch.randn() : 평균이 0이고 표준편차가 1인 가우시안 정규분포를 이용해 생성
torch.randn_like() : 사이즈를 튜플로 입력하지 않고 기존의 Tensor로 정의
torch.randint() : 주어진 범위 내의 정수를 균등하게 생성, 자료형은 torch.float32
torch.randint_like() : 사이즈를 튜플로 입력하지 않고 기존의 Tensor로 정의
torch.randperm() : 주어진 범위 내의 정수를 랜덤하게 생성
'''
x = torch.zeros(5,3)
print(x)
'''
tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])
'''
