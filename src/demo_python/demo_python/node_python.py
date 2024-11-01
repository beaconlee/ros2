import rclpy

from rclpy.node import Node


def main():
    rclpy.init()
    node = Node("beacon_py")
    node.get_logger().info("hello beacon")
    rclpy.spin(node)
    rclpy.shutdown()
