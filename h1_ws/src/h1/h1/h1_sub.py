import rclpy
from rclpy.node import Node
import numpy as np

from std_msgs.msg import String
from unitree_go.msg import LowState

class H1Subscriber(Node):
    def __init__(self):
        # setup subscriber
        super().__init__("h1_subscriber")
        self.low_state_sub = self.create_subscription(
            LowState, "h1_fake/low_state", self.low_state_sub_callback, 10
        )
        self.low_state_sub

        # setup robot state
        self.last_call_time = self.get_clock().now()
        self.vel = np.array([0.0, 0.0, 0.0])

    def low_state_sub_callback(self, msg):
        # update velocity
        acc = np.array(msg.imu_state.accelerometer)
        acc[2] -= 9.81 # gravity
        dt = (self.get_clock().now() - self.last_call_time).nanoseconds / 1e9
        self.vel += acc * dt
        self.last_call_time = self.get_clock().now()
        self.get_logger().info(f"imu a: {acc}, estimate v: {self.vel}")
        

def main(args=None):
    rclpy.init(args=args)

    h1_sub = H1Subscriber()

    rclpy.spin(h1_sub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    h1_sub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
