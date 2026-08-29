from rclpy.node import Node


class Sensor(Node):

    def __init__(self, node_id: str, current_location: str, sensor_id: str) -> None:
        # node_id is passed to rclpy as the node name; read it back via get_name().
        super().__init__(node_id)
        self._current_location = current_location 
        self._sensor_id = sensor_id

    def report_location(self) -> None:
        pass

    def publish(self) -> None:
        pass
