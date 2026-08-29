from rclpy.node import Node


class Sensor(Node):
    def __init__(self, node_id: str, current_location: str, sensor_id: str) -> None:
        super().__init__(node_id)
        self.current_location = current_location
        self.sensor_id = sensor_id

    def report_location(self) -> None:
        pass

    def publish_camera(self) -> None:
        pass

    def publish_lidar(self) -> None:
        pass

    def publish_imu(self) -> None:
        pass
