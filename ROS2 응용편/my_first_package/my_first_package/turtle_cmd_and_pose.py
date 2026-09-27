#라이브러리 불러오기
import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from my_first_package_msgs.msg import CmdAndPoseVel # 직접 정의한 메시지 가져오기
from geometry_msgs.msg import Twist

class CmdAndPose(Node):
	def __init__(self):
		super().__init__('turtle_cmd_pose')
		self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10) #위치 정보 구독자 생성, 위치정보 수신 시callback_pose 함수 실행
		self.sub_cmdvel = self.create_subscription(Twist, '/turtle1/cmd_vel', self.callback_cmd, 10) #속도 정보 구독자 생성, 속도정보 수신 시callback_pose 함수 실행
		self.timer_period = 1.0
		self.publisher = self.create_publisher(CmdAndPoseVel, "/cmd_and_pose", 10)
		self.timer = self.create_timer(self.timer_period, self.timer_callback) #타이머 생성
		self.cmd_pose = CmdAndPoseVel() #여러 콜백함수에서 데이터를 모아둘 객체 생성

	def callback_pose(self, msg): #위치정보 구독자 콜백함수 정의
		self.cmd_pose.pose_x = msg.x
		self.cmd_pose.pose_y = msg.y
		self.cmd_pose.linear_vel = msg.linear_velocity
		self.cmd_pose.angular_vel = msg.angular_velocity
		
	def callback_cmd(self, msg): #속도 정보 구독자 콜백함수 정의
		self.cmd_pose.cmd_vel_linear = msg.linear.x
		self.cmd_pose.cmd_vel_angular = msg.angular.z
	
	def timer_callback(self): #타이머 콜백함수 정의
		self.publisher.publish(self.cmd_pose) #모아둔 데이터 토픽으로 발행



def main():
	rp.init()

	turtle_cmd_pose_node=CmdAndPose()
	rp.spin(turtle_cmd_pose_node)

	turtle_cmd_pose_node.destroy_node()
	rp.shutdown()

if __name__=='__main__':
	main()
