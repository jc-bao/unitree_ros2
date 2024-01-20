import rclpy
from rclpy.node import Node
import numpy as np

from std_msgs.msg import String
from unitree_go.msg import LowCmd, MotorCmd


class H1CmdPublisher(Node):
    def __init__(self):
        super().__init__("h1_command_publisher")
        self.low_cmd_pub = self.create_publisher(LowCmd, "h1_cmd", 10)
        timer_period =  1/5.0 # seconds
        self.low_cmd_pub_timer = self.create_timer(timer_period, self.low_cmd_pub_callback)

    def low_cmd_pub_callback(self):
        cmd_msg = LowCmd()
        qs = np.random.randn(20)/10
        for i in range(20):
            cmd_msg.motor_cmd[i].q = qs[i]
        self.low_cmd_pub.publish(cmd_msg)
        qs_send = [cmd_msg.motor_cmd[i].q for i in range(20)]
        self.get_logger().info(f"Publishing low cmd message ...\\ {qs_send}")

def main(args=None):
    rclpy.init(args=args)

    h1_cmd_pub = H1CmdPublisher()

    rclpy.spin(h1_cmd_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    h1_cmd_pub.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
