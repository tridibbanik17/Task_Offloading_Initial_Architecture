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
from task_offloading.sensor import CameraSensor
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
    sensor = None
    node = None
    try:
        sensor = CameraSensor("camera_sensor", "vehicle_1", "cam_front")
        node = OffloadableNode("perception", "vehicle_1")
        manager = OffloadManager()

        print("All classes instantiated successfully:")
        for obj in (snapshot, record, status, decision, migration, sensor, node, manager):
            print("  -", type(obj).__name__)
    finally:
        if sensor is not None:
            sensor.destroy_node()
        if node is not None:
            node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
