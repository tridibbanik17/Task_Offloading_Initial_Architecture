from rclpy.node import Node


class Sensor(Node):
    """Generic sensor driver node.

    One Sensor instance == one physical sensor == one ROS2 node. Publishes its
    data on a topic via publish(). Sensor-type specialization (camera, lidar,
    imu, ...) is left out of this initial architecture.
    """

    def __init__(self, node_id: str, current_location: str, sensor_id: str) -> None:
        super().__init__(node_id)
        self.current_location = current_location
        self.sensor_id = sensor_id

    def report_location(self) -> None:
        pass

    def publish(self) -> None:
        pass
