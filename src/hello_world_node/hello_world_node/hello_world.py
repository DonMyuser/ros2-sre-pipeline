import rclpy

from rclpy.node import Node


class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('hello_world_node')
        self.create_timer(3.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello world')


def main(args=None):
    hello_world_node = None
    try:
        rclpy.init(args=args)
        hello_world_node = HelloWorldNode()
        rclpy.spin(hello_world_node)
    except (KeyboardInterrupt):
        pass
    finally:
        if (hello_world_node is not None):
            hello_world_node.destroy_node()
        if (rclpy.ok()):
            rclpy.shutdown()


if __name__ == '__main__':
    main()
