import rclpy as rp  #ros2 python 라이브러리
from rclpy.node import Node #ros2 노드 생성에 사용
from turtlesim.msg import Pose #turtlesim의 위치 정보 메세지

class TurtlesimSubscriber(Node):
	def __init__(self):
		super().__init__('turtlesim_subscriber')
		self.subscription = self.create_subscription(
				Pose, #받을 메세지 타입
				'/turtle1/pose', #구독할 토픽
				self.callback, #메세지가 들어오면 실행할 함수
				10 #메세지 크기
			)
	def callback(self,msg):
		print("X: ", msg.x,"Y: ", msg.y)


def main():
	rp.init()

	turtlesim_subscriber = TurtlesimSubscriber()
	rp.spin(turtlesim_subscriber)

	turtlesim_subscriber.destroy_node()
	rp. shutdown()

if __name__ == '__main__':
	main()