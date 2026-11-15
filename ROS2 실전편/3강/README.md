# ROS2 실전편 3강 공부기록

- ROS2 실전편 3강을 공부한 기록입니다.

<img width="1700" height="953" alt="image" src="https://github.com/user-attachments/assets/f30dba25-a56c-47b0-86e4-2d6aea2c6377" />
- domain id가 다를 경우 구독할 수 없음

<img width="1700" height="953" alt="image" src="https://github.com/user-attachments/assets/415fe553-4b6e-45c8-8ef0-11767fd3b338" />
- domain id가 같을 경우 구독

## 하나의 노드에서 서로 다른 ROS_DOMAIN_ID에 토픽 발행해보기 (domain_test.py 실습)
<img width="1700" height="953" alt="image" src="https://github.com/user-attachments/assets/487f4d7f-c0f2-4285-99c6-5b87f7a059f1" />

## 하나의 노드에서 서로 다른 ROS_DOMAIN_ID를 가진 turtlesim 다루기

- domain_test_turtle.py
<img width="1850" height="942" alt="image" src="https://github.com/user-attachments/assets/3d957743-d268-4a66-b7ec-c93b3ae26be6" />
- 실행 결과 ROS_DOMAIN_ID가 1인 경우 시계방향, 2인경우 반시계방향으로 돌게된다.

- domain_test_service.py
<img width="1850" height="942" alt="image" src="https://github.com/user-attachments/assets/1e4fe2a7-feb4-417c-96c7-527321aebad1" />
- 실행 결과 ROS_DOMAIN_ID가 1인 경우 x=2, 2인경우 x=8로 이동하게 된다.

- domain_test_action.py
<img width="1850" height="942" alt="image" src="https://github.com/user-attachments/assets/55f9d2b1-9bab-4ad4-ae72-32709894cda1" />
- 실행 결과 ROS_DOMAIN_ID가 1인 경우 90도, 2인경우 270도로 돌게 된다.

## ROS_DOMAIN_BRIDGE 사용 실습
```bash
sudo apt update && sudo apt install ros-jazzy-domain-bridge -y
```
- domain_bridge 사용을 위한 패키지 설치
- 
<img width="1672" height="942" alt="image" src="https://github.com/user-attachments/assets/ae9813a7-182e-42c5-8f16-d9f7bb211629" />
- ```bash
  ros2 run domain_bridge domain_bridge ~/ros_domain/my_bridge.yaml
  ```
  실행 후 정상스럽게 구독되는 것 확인 가능
