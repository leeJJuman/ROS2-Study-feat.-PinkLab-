from my_first_package_msgs.srv import MultiSpawn #직접 정의한 서비스 타입 불러오기
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn

import time
import numpy as np
import rclpy as rp
from rclpy.node import Node

class MultiSpawning(Node):
	def __init__(self):
		super().__init__("multi_spawn") #노드이름 지정
		self.server = self.create_service(MultiSpawn, 'multi_spawn', self.callback_service) #서비스 서버 생성
		self.teleport = self.create_client(TeleportAbsolute, "/turtle1/teleport_absolute") #서비스 클라이언트 생성
		self.spawn = self.create_client(Spawn, '/spawn') #Request 객체 생성
		self.req_teleport = TeleportAbsolute.Request()
		self.req_spawn = Spawn.Request()
		self.center_x=5.54
		self.center_y=5.54
		
	def calc_position(self, n, r): #위치 계산 함수
		gap_theta=2*np.pi/n
		theta = [gap_theta*n for n in range(n)]
		x=[r*np.cos(th) for th in theta]
		y=[r*np.sin(th) for th in theta]
		return x,y,theta
	
	def callback_service(self, request, response): #서비스 콜백함수 정
		x,y,theta = self.calc_position(request.num, 3)

		for n in range(len(theta)): #계산된 상대좌표에 실제좌표를 더함
			self.req_spawn.x=x[n]+self.center_x 
			self.req_spawn.y=y[n]+self.center_y
			self.req_spawn.theta = theta[n]

			self.spawn.call_async(self.req_spawn) #설정된 위치에 거북이 생성요청
			time.sleep(0.1)
		response.x=x
		response.y=y
		response.theta=theta
		return response

def main(args=None):
	rp.init(args=args)
	multi_spawn = MultiSpawning()
	rp.spin(multi_spawn)
	rp.shutdown()

if __name__=="__main__":
	main()
