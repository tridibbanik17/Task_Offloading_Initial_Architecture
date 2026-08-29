from abc import abstractmethod

from rclpy.node import Node


class Sensor(Node):
    """Generic sensor driver node.

    One Sensor instance == one physical sensor == one ROS2 node. It holds the
    fields common to every sensor and defines a single publish() contract.
    Concrete sensor types (camera, lidar, imu, ...) subclass this and implement
    publish() for their own data, so a node only ever publishes its own stream.
    """

    def __init__(self, node_id: str, current_location: str, sensor_id: str) -> None:
        super().__init__(node_id)
        self.current_location = current_location
        self.sensor_id = sensor_id

    def report_location(self) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        """Publish this sensor's data on its topic. Implemented per sensor type."""
        raise NotImplementedError


class CameraSensor(Sensor):
    def publish(self) -> None:
        pass


class LidarSensor(Sensor):
    def publish(self) -> None:
        pass


class ImuSensor(Sensor):
    def publish(self) -> None:
        pass
