import rclpy as rp
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from my_first_package.my_publisher import TurtlesimPublisher
from my_first_package.my_subscriber import TurtlesimSubscriber

def main(args=None):
	rp.init(args=args)
	#두개의 객체 생성
	pub = TurtlesimPublisher()
	sub = TurtlesimSubscriber()
	#멀티스레드 실행기 설정
	executor = MultiThreadedExecutor()
	#각 노드 등록
	executor.add_node(pub)
	executor.add_node(sub)

	try:
		executor.spin()

	finally:
		executor.shutdown()
		pub.destroy_node()
		sub.destroy_node()
		rp.shutdown()

if __name__=="__main__":
	main()
