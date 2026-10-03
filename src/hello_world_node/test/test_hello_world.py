
from hello_world_node.hello_world import HelloWorldNode
import rclpy


def test_hello_world_node():
    rclpy.init()
    hello_world_node = None
    try:
        hello_world_node = HelloWorldNode()
        assert hello_world_node.get_name() == 'wrong_name'
    finally:
        if (hello_world_node is not None):
            hello_world_node.destroy_node()
        if (rclpy.ok()):
            rclpy.shutdown()
