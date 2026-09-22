# 패키지 만들기 실습


### 패키지 만들기
ros2 pkg create --build-type ament_python --node-name my_first_node my_first_package

### 빌드
colcon build #새로 생성하거나 수정할 시 실행

### reload bash
source ./install/local_setup.bash #빌드후 실행

### 만든 노드 실행
ros2 run my_first_package my_first_node

### package에서 topic 구독하기
ros2 run my_first_package my_subsriber

### package에서 topic 발행하기
ros2 run my_first_package my_publisher

### 

만든 액션 실행
ros2 action send_goal /dist_turtle my_first_package_msgs/action/DistTurtle "{linear_x: 0, angular_z: 0, dist: 0}"


피드백 포함하기
ros2 action send_goal --feedback /dist_turtle my_first_package_msgs/action/DistTurtle "{linear_x: 0, angular_z: 0, dist: 0}"

파라미터 리스트
ros2 param list

파라미터 값 조회
ros2 param get /turtlesim background_g

파라미터 값 변경
ros2 param set /turtlesim background_r 250
파라미터 dump
ros2 param dump /turtlesim > ./turtlesim.yaml
파라미터 불러오기
ros2 param load /turtlesim ./turtlesim.yaml

토픽 기록
ros2 bag record -o turtle_test -a

기록한거 재생
ros2 bag play turtle_test/

rqt에서 사용가능
