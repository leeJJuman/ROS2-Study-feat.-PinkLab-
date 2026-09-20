# ROS2 입문편 공부내용 정리

유튜브 PinkLab 채널의 ROS2 입문편을 공부하며 정리한 기록입니다.
입문편은 개발환경 세팅과 터미널에서 ROS2를 사용해보는 것이 대부분이었습니다.

## 개발환경 세팅

- ubuntu 22.04
  
  ROS2를 공부하기에 적절한 개발환경인 ubuntu 세팅
  
- ROS2 Humble
  
  ubuntu 22.04와 호환되는 버전인 ROS2 Humble 세팅

- Terminator

  터미널에서 창을 나누는 기능을 사용할수있는 Terminator 세팅

- IDE

  Sublime text

  VSCode

  Jupyter Notebook

    코드를 짤 때 사용할 IDE 세팅

## 터미널 명렁어 및 단축키 정리

<img width="480" height="270" alt="image" src="https://github.com/user-attachments/assets/c496cd7a-73e0-417e-93f9-b5cad86ed2c0" />

leejjman #사용자이름

dlwjdwnman #PC이름

~  #홈 경로

Ctrl+Alt+T #터미널 켜기

exit #터미널창 나가기

ls #현재 홈경로의 폴더나 파일이름 출력

clear #현재 터미널 정리

sudo apt update #업데이트

sudo apt terminator # 터미네이터 설치

pwd #현재경로 출력

mkdir 폴더명 # 폴더명 이름의 폴더 생성

sudo - #관리자 권한으로

sudo rm -r 폴더명 # 관리자권한으로 폴더명 폴더를 지움 (-r은 옵션, rm이 폴더를 지울수있게함)

cd 폴더명 - #폴더간 이동

ex) cd Doc 상태에서 Tab # Documents 자동으로 완성

ex) cd D 상태에서 탭 두번 # D로 시작하는 폴더 목록 보여줌

cd 상태에서 cd - #홈으로 돌아감

cd .. - #한단계 상위폴더로 이동

../.. - #두단계 상위

@ --version - # @의 버전 확인

subl . #현재 경로의 sublime Text 열기

echo #파이썬의 print와 같은역할

echo $SHELL #현재의 Shell 확인

subl ~/.bashrc #sublime으로 bashrc열기

alias #alias목록 조회

source ~/.bashrc # bashrc를 reload

### Turtlesim

ros2 run turtlesim turtlesim_node #turtlesim 켜기

ros2 run <PKG Name> <Node Name>

ros2 node list #node list 출력

ros2 node info /turtlesim #turtlesim 노드가 무엇을 제공하는지 출력

#### Service

ros2 service list #service list 출력

ros2 service list -t # 데이터 타입을 포함하여 출력

ros2 service type /turtle1/teleport_absolute # turtle1의 teleport_absolute의 type 출력

ros2 interface show turtlesim/srv/TeleportAbsolute #TeleportAbsolute service의 request 출력

ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 2,y: 2,theta: 1.57}" #TA 서비스 call 

#서비스 사용시  list로 확인-> type확인 -> request확인 -> service call

spawn - 새로운 거북이 만듦


#### Topic

ros2 topic list #topic list 출력

ros2 topic type /turtle1/pose #turtle1 의 topic 'pose'의 데이터 타입 출력

ros2 topic list -t #데이터 타입을 포함하여 출력

ros2 topic list -v #발행하고있는 topic 출력

ros2 interface show turtlesim/msg/Pose # Pose의 생긴모양 출력

ros2 topic echo /turtle1/pose # pose 값 출력 (topic echo = 구독)

rqt_graph # 현재 토픽/노드 구조 확인

cmd_vel #주행명령

ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear:{x: 2,y: 0,z: 0},angular:{x: 0,y: 0,z: 0}}" # pub --once 한번만 실행, pub --rate 1 1Hz마다 실행 

#구독 멈추기 -> Ctrl+C

#토픽 사용시 list로 확인 -> type 확인 -> request 확인 ros2 interface show (type으로 출력된 것)          -> topic pub *중첩 발행 가능


#### action

ros2 run turtlesim turtle_teleop_key # 키보드로 거북이 조종 (turtlesim_node와 같이 실행해야함)

ros2 action list # action list 출력

ros2 topic list -t #데이터 타입을 포함하여 출력

ros2 interface show turtlesim/action/RotateAbsolute # 생긴모양 확인

ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 3.14}"  #액션의 목표 지정
