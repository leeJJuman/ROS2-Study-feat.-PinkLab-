# 패키지 만들기 실습
패키지를 직접 만들며 실습해본 코드들을 정리한 기록입니다.

패키지 생성부터 노드, topic 구독 및 발행, 메시지 출력, 서비스 서버 및 서비스 생성 액션 서버 및 액션 생성 등이 포함되어있습니다. 

아래는 터미널 명령어들을 정리하였고 폴더내의 각 코드의 주석에서 상세하게 분석할 수 있습니다.
### 패키지 만들기
ros2 pkg create --build-type ament_python --node-name my_first_node my_first_package

### 빌드
- colcon build #새로 생성하거나 수정할 시 실행
- colcon build --package-select my_first_package #원하는 패키지만 빌드

### reload bash
source ./install/local_setup.bash #빌드후 실행

### 만든 노드 실행
ros2 run my_first_package my_first_node

### package에서 topic 구독하기
ros2 run my_first_package my_subsriber

### package에서 topic 발행하기
ros2 run my_first_package my_publisher

### 토픽 구독하여 메시지 출력하기
ros2 run my_first_package turtle_cmd_and_pose #메시지 정의는 my_first_package_msgs 참조

### 노드 구조 시각적으로 확인
rqt_graph #실시간으로 노드가 어떤 관계에 놓여있는지 확인 가능

### 서비스 
ros2 run my_first_package my_service_server #서비스 서버 실행
ros2 service call /multi_spawn_my_first_package_msgs/srv/MultiSpawn "{num: 1}" #service call

### 액션
ros2 run my_first_package dist_turtle_action_server #액션 서버 실행
ros2 action send_goal /dist_turtle my_first_package_msgs/action/DistTurtle "{linear_x: 0, angular_z: 0, dist: 0}" #액션 실행
ros2 action send_goal --feedback /dist_turtle my_first_package_msgs/action/DistTurtle "{linear_x: 0, angular_z: 0, dist: 0}" #피드백 포함하기

### 멀티스레드
ros2 run my_first_package my_multi_thread #멀티스레드 실행

### 파라미터
ros2 param list #파라미터 리스트 조회

ros2 param get /turtlesim background_g #파라미터 값 조회

ros2 param set /turtlesim background_r 250 #파라미터 값 변경

ros2 param dump /turtlesim > ./turtlesim.yaml #파라미터 dump

ros2 param load /turtlesim ./turtlesim.yaml #파라미터 불러오기

### bag
ros2 bag record -o turtle_test -a #토픽 기록

ros2 bag play turtle_test/ #기록된 토픽 재생

### 엔트리포인트 설정
```
'my_first_node = my_first_package.my_first_node:main',
'my_subscriber = my_first_package.my_subscriber:main',
'my_publisher = my_first_package.my_publisher:main',
'turtle_cmd_and_pose = my_first_package.turtle_cmd_and_pose:main',
'my_service_server = my_first_package.my_service_server:main
'dist_turtle_action_server = my_first_package.dist_turtle_action_server:main',
'my_multi_thread = my_first_package.my_multi_thread:main'
```
새 노드를 추가할때마다 setup.py에서 추가해주기
