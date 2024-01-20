import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from unitree_go.msg import LowState


class H1FakePublisher(Node):
    def __init__(self):
        super().__init__("h1_fake_publisher")
        self.low_state_pub = self.create_publisher(LowState, "h1_fake/low_state", 10)
        timer_period =  1.0 # seconds
        self.low_state_pub_timer = self.create_timer(timer_period, self.low_state_pub_callback)

    def low_state_pub_callback(self):
        state_msg = LowState()
        self.low_state_pub.publish(state_msg)
        self.get_logger().info("Publishing low state message ...")

def main(args=None):
    rclpy.init(args=args)

    h1_fake_pub = H1FakePublisher()

    rclpy.spin(h1_fake_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    h1_fake_pub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
