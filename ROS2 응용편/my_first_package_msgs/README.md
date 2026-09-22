# 메시지 정의를 위한 패키지 만들기
ros2 pkg create --build-type ament_cmake my_first_package_msgs

## 메세지 정의
CmdAndPoseVel.msg 파일에 메세지 definition 작성

## package.xml 폴더에 작성
```
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
