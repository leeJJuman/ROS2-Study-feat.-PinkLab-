# ROS2 실전편 0강 

- ROS2 실전편 첫번째 강의부터 3번째 강의까지의 기록

## Ubuntu 24.04 noble 설치
```bash
sudo do-release-upgrade
```

## ROS2 Jazzy 설치

1. 구글에 Jazzy install 검색 후 첫번째 링크
2. installation의 Ubuntu 선택
3. System Setup의 Set locale 코드 터미널에 붙어녛기
```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```
4. Enable required repositories 에서 아래 코드 붙여넣기 
```bash
sudo apt update && sudo apt install curl -y
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
sudo dpkg -i /tmp/ros2-apt-source.deb
```
5. ros2 jazzy 다운로드
```bash
sudo apt install ros-jazzy-desktop
```
6. 설치 완료 후 환경 설정
```bash
source /opt/ros/jazzy/setup.bash
```

## bashrc 세팅

- .bashrc 파일에 아래 코드 추가
```sh
source ~/alias_settings.sh
```
- alias_settings.sh 의 코드 및 주석에 추가로 설명
