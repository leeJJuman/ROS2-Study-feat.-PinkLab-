패키지 만들기
ros2 pkg create --build-type ament_cmake my_first_package_msgs

colcon build --packages-select my_first_package



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
