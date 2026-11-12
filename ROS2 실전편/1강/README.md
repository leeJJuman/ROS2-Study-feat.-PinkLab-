# ROS2 실전편 1강 공부내용 정리

- 핑크랩 R2R 실전편 강의를 듣고 정리한 기록입니다.
 
## 개발환경 세팅

### USB_CAM 패키지 설치
```bash
sudo apt install ros-jazzy-usb-cam
```
### USB 카메라 켜기
```bash
ros2 run usb_cam usb_cam_node_exe 
```
- 카메라를 찾아서 ros2 에서 쓸 수 있는 topic 으로 발행

### 카메라 확인
1. 토픽을 발행한 상태에서 새로운 터미널 열기
2. rqt 명령어 실행
3. Plungins -> Visualization -> Image View
4. Refresh Topics -> 왼쪽에서 /image_raw 선택

## 멀티캐스트
- 한 번의 송신으로 메시지나 정보를 목표한 여러 컴퓨터에 동시에 전송하는 것
- 멀티캐스트로 인하여 카메라 송출이 느려질 수 있음
### 해결방안
터미널에 아래 명령어
```bash
export ROS_LOCALHOST_ONLY=1
```
- 네트워크로 내 토픽 발행하지 않는다는 의미
- 다른 디바이스와 통신 불가

## 패키지 생성
```bash
ros2 pkg create --build-type ament_python my_opencv_tutorials
```

## pip 관련 설정
```bash
python3 -m pip config set global.break-system-packages true
```

## opencv 라이브러리 설치
```bash
pip3 install opencv-python
```

## cv-bridge 설치
```bash
 sudo apt install ros-jazzy-cv-bridge
```
- ROS와 OpenCV의 이미지 데이터타입을 이어주기 위해 cv-bridge 다운로드

## cv-bridge를 이용하여 opencv로 얻은 카메라 데이터를 ros2 topic 으로 발행

```bash
ros2 run my_opencv_tutorials img_pub
```

## 파라미터 적용하기

- config 폴더 만들고 cv_params.yaml 파일생성 (파라미터를 반영하고싶을땐 cv_params.yaml 파일에서 값 수정)
- launch 폴더에 bringup_cv.launch.xml 파일 생성
- setup.py의 data_files에 아래 코드 추가
 ```python
('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.*'))),
('share/' + package_name + '/config', glob.glob(os.path.join('config', '*.yaml'))),
```
- img_pub.py 파일 생성 (코드의 설명은 주석에)

```bash
ros2 launch my_opencv_tutorials bringup_cv.launch.xml 
```
- 반영되었는지 확인

## HSV

- cv_params.yaml 파일에 아래 내용 추가
```yaml
hsv_converter:
    ros__parameters:
        saturation_scale: 1.0
        value_scale: 1.0
```
- launch폴더에 hsv_converter.launch.xml 파일 생성
- setup.py의 entry_points에 아래 코드 추가
```python
'convert_hsv = my_opencv_tutorials.convert_hsv:main',
```
- 터미넗에서 아래 코드 실행
```bash
ros2 launch my_opencv_tutorials hsv_converter.launch.xml 
```
- rqt 열고 Plugins -> Configuration -> Dynamic Reconfigure -> Refresh -> hsv_converter -> 슬라이더 조정
- image_hsv를 확인하며 파라미터 변경이 잘 반영되는지 확인

## Canny Edge Detector

- cv_params.yaml 파일에 아래 내용 추가
```yaml
edge_detect:
    ros__parameters:
        threshold1: 100
        threshold2: 200
```
- launch폴더에 edge_detect.launch.xml 파일 생성
- setup.py의 entry_points에 아래 코드 추가
```python
'edge_detect = my_opencv_tutorials.edge_detect:main',
```
- 터미넗에서 아래 코드 실행
```bash
ros2 launch my_opencv_tutorials edge_detect.launch.xml 
```

## Cartoon Styler

- cv_params.yaml 파일에 아래 내용 추가
```yaml
cartoon_styler:
    ros__parameters:
        sigma_color: 20
        sigma_space: 9
```
- launch폴더에 cartoon_styler.launch.xml 파일 생성
- setup.py의 entry_points에 아래 코드 추가
```python
'cartoon = my_opencv_tutorials.cartoon:main',
```
- 터미넗에서 아래 코드 실행
```bash
ros2 launch my_opencv_tutorials cartoon_styler.launch.xml 
```

## Optical Flow node

- launch폴더에 optical_flow.launch.xml 파일 생성
- setup.py의 entry_points에 아래 코드 추가
```python
'optical_flow = my_opencv_tutorials.optical_flow:main',
```
- 터미넗에서 아래 코드 실행
```bash

```
