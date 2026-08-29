"""
Instantiates every class to confirm the class structure loads correctly.
No behaviour is exercised - method bodies are stubs.
"""

import rclpy

from task_offloading.value_types import (
    StateSnapshot,
    NodeRecord,
    NodeStatus,
    Decision,
    Migration,
)
from task_offloading.sensor import CameraSensor, LidarSensor, ImuSensor
from task_offloading.offloadable_node import OffloadableNode
from task_offloading.offload_manager import OffloadManager


def main() -> None:
    # Plain dataclasses - no ROS2 runtime needed.
    snapshot = StateSnapshot(1, b"", b"", ["/sensor/data"], 0.0)
    record = NodeRecord("perception", "vehicle_1", "active", 0.0, 0.0, 0.0)
    status = NodeStatus("perception", "vehicle_1", "active", 0.0, 0.0, True)
    decision = Decision(True, "perception", "edge_server_a", "cpu high")
    migration = Migration("perception", "vehicle_1", "edge_server_a", "in_progress", 0.0)

    # ROS2 nodes require an initialized context.
    rclpy.init()
    ros_nodes = []
    try:
        camera = CameraSensor("camera_sensor", "vehicle_1", "cam_front")
        lidar = LidarSensor("lidar_sensor", "vehicle_1", "lidar_top")
        imu = ImuSensor("imu_sensor", "vehicle_1", "imu_main")
        node = OffloadableNode("perception", "vehicle_1")
        manager = OffloadManager()
        ros_nodes = [camera, lidar, imu, node]

        print("All classes instantiated successfully:")
        for obj in (snapshot, record, status, decision, migration,
                    camera, lidar, imu, node, manager):
            print("  -", type(obj).__name__)
    finally:
        for ros_node in ros_nodes:
            ros_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
