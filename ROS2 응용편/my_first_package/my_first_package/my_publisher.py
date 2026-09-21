import rclpy as rp    #ros2 python 라이브러리
from rclpy.node import Node #ros2 노드 생성에 사용
from geometry_msgs.msg import Twist #속도 정보를 전달하는 메세지 타입

class TurtlesimPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Twist, #보낼 메세지 타입
            '/turtlesim/turtle1/cmd_vel', #메세지를 보낼 토픽
            10)#크기
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback) #0.5초마다 timer_callback() 실행

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.publisher.publish(msg)

def main(args=None):
    rp.init(args=args)

    turtlesim_publisher = TurtlesimPublisher()
    rp.spin(turtlesim_publisher)

    turtlesim_publisher.destroy_node()
    rp. shutdown()

if __name__ == '__main__':
    main()