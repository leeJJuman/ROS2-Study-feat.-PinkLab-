import rclpy as rp  #ros2 python 라이브러리
from rclpy.node import Node #ros2 노드 생성에 사용
from turtlesim.msg import Pose #turtlesim의 위치 정보 메세지

class TurtlesimSubscriber(Node): #노드 클래스 정의
	def __init__(self):
		super().__init__('turtlesim_subscriber') #노드 이름 등록
		self.subscription = self.create_subscription( #subscribtion 객체 생성
				Pose, #받을 메세지 타입
				'/turtle1/pose', #구독할 토픽, turtle1의 pose 정보 구독
				self.callback, #메세지가 들어오면 실행할 함수
				10 #메세지 크기
			)
	def callback(self,msg):
		print("X: ", msg.x,"Y: ", msg.y) #메세지가 들어오면 터미널에 출력


def main():
	rp.init()

	turtlesim_subscriber = TurtlesimSubscriber()
	rp.spin(turtlesim_subscriber) #계속해서 콜백함수 실행됨

	turtlesim_subscriber.destroy_node() # 사용자가 Ctrl+C를 눌러 sipn이 풀리면 객체 파괴하여 메모리 정리
	rp. shutdown() #ROS2 시스템 종료

if __name__ == '__main__':
	main()
