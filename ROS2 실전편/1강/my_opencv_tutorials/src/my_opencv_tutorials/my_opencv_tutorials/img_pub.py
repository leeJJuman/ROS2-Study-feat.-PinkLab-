#라이브러리 정의
import rclpy 
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge 
import cv2

class ImgPublisher(Node):
    def __init__(self):
        super().__init__('img_publisher')
        self.publisher = self.create_publisher(Image, '/image_raw', 10)

        self.declare_parameter('width', 640)
        self.width = self.get_parameter('width').value
        self.declare_parameter('height', 480)
        self.height = self.get_parameter('height').value
        self.declare_parameter('camera_device', 0)
        self.camera_device = self.get_parameter('camera_device').value
        self.declare_parameter('frame_rate', 30)
        self.frame_rate = self.get_parameter('frame_rate').value

        self.cap = cv2.VideoCapture(self.camera_device)
        self.cv_bridge = CvBridge()
        time_period = 1.0 / self.frame_rate
        self.timer = self.create_timer(time_period, self.time_callback)

        self.get_logger().info("Video Width : " + str(self.width))
        self.get_logger().info("Video Height : " + str(self.height))
        self.get_logger().info("Video Camera Device : " + str(self.camera_device))
        self.get_logger().info("Video Frame Rate : " + str(self.frame_rate))       

    def time_callback(self): #time period마다 가져온 이미지 프레임을 ROS2 데이터로 변환 후 publish
        ret, frame = self.cap.read() #opencv
        frame = cv2.resize(frame, (self.width, self.height)) #파라미터에서 가져온 width, height로 이미지 크기 조정
        img = self.cv_bridge.cv2_to_imgmsg(frame, encoding='bgr8')  #ros
        self.publisher.publish(img)
        cv2.waitKey(1)

def main() :
    rclpy.init()
    node = ImgPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()
