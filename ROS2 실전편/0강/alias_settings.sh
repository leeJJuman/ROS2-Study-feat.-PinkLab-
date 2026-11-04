# ROS2 자동완성이 되지 않을 때를 대비
# argcomplete for ros2 & colcon
alias tmp1="eval \"\$(register-python-argcomplete3 ros2)\""
alias tmp2="tmp1; eval \"\$(register-python-argcomplete3 colcon)\""

# ALIAS settings
ID=47
alias sb="source ~/.bashrc; echo \"Bashrc is reloaded!\""

alias ros_domain="export ROS_DOMAIN_ID=\$ID; echo \"ROS_DOMAINID is set to \$ID !\"" #변수지정은 $로
alias active_venv_jazzy="source ~/venv/jazzy/bin/activate; echo \"Venv Jazzy is activated.\""
alias jazzy="active_venv_jazzy; source /opt/ros/jazzy/setup.bash; ros_domain; echo \"ROS2 Jazzy is activated.\""

#sh에서 함수 선언
ws_setting() #입력인자는 $(num)으로 받음
{
	jazzy
	source ~/$1/install/local_setup.bash
	echo "$1 workspace is activated."
}

get_status()
{
	if [ -z $ROS_DOMAIN_ID ]; then
		echo "ROS_DOMAIN_ID : 0"
	else
		echo "ROS_DOMAIN_ID : $ROS_DOMAIN_ID"
	fi

	if [ -z $ROS_LOCALHOST_ONLY ]; then
		echo "ROS_LOCALHOST_ONLY : 0"
	else
		echo "ROS_LOCALHOST_ONLY : $ROS_LOCALHOST_ONLY"
	fi
}

alias  ros2_study="ws_setting \"ros2_study\""

#여러 디바이스가 네트워크로 연결되어있는경우 ROS DOMAIN ID가 여러개이므로 각각 보여줄 수 있게 하는 코드
GREEN='\[\e[1;32m\]'
BLUE='\[\e[1;34m\]' 
NC='\[\e[0m\]'

PS1="${BLUE}(ID: \${ROS_DOMAIN_ID:-0})${GREEN}\u${NC}:${BLUE}\w${NC}\$ "
