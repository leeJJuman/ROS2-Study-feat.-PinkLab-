# 메시지 정의를 위한 패키지 만들기
ros2 pkg create --build-type ament_cmake my_first_package_msgs

## 메시지 정의
msg/CmdAndPoseVel.msg 파일에 메시지 정의
##### 인터페이스 생성 의존성 추가 (package.xml)
```
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

## 서비스 메시지 정의
srv/MultiSpawn.srv 파일에 서비스 정의
##### 인터페이스 빌드 규칙 등록 (CMakeLists.txt)
```
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
 "msg/CmdAndPoseVel.msg"
 "srv/MultiSpawn.srv"
 "action/DistTurtle.action"
)
```
